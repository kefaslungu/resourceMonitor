"""Isolate the CPU command bodies from NVDA for reporting regression tests."""

import ast
from pathlib import Path
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from test_cpu_temperature import sensor


SOURCE = Path(__file__).resolve().parents[1] / "addon/globalPlugins/resourceMonitor/__init__.py"


def commandEnvironment(translate=lambda text: text):
	tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
	functions = [
		node
		for node in tree.body
		if isinstance(node, ast.FunctionDef) and node.name in ("formatGpuTemperature", "tryTrunk")
	]
	plugin = next(
		node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "GlobalPlugin"
	)
	names = {"script_announceProcessorInfo", "_collectCpuTemperature", "_finishCpuReport"}
	methods = []
	for node in plugin.body:
		if isinstance(node, ast.FunctionDef) and node.name in names:
			node.decorator_list = []
			methods.append(node)
	module = ast.Module(
		body=[
			*ast.parse("from __future__ import annotations").body,
			*functions,
			ast.ClassDef(name="Commands", bases=[], keywords=[], body=methods, decorator_list=[]),
		],
		type_ignores=[],
	)
	ast.fix_missing_locations(module)
	environment = {
		"_": translate,
		"config": SimpleNamespace(conf={"resourceMonitor": {"gpuTempUnit": "celsius"}}),
		"TemperatureUnavailable": sensor.TemperatureUnavailable,
		"scriptHandler": SimpleNamespace(getLastScriptRepeatCount=Mock(return_value=0)),
		"ui": SimpleNamespace(message=Mock()),
		"api": SimpleNamespace(copyToClip=Mock()),
		"psutil": SimpleNamespace(
			cpu_percent=lambda percpu=False: [10, 20] if percpu else 2.5, cpu_count=lambda: 2
		),
		"queueHandler": SimpleNamespace(
			eventQueue=object(), queueFunction=lambda queue, fn, *args: fn(*args)
		),
	}
	exec(compile(module, str(SOURCE), "exec"), environment)
	commands = environment["Commands"]()
	commands._cpuReportClosed = threading.Event()
	commands._cpuReportPending = False
	commands._cpuReportCopy = False
	commands._cpuTemperature = SimpleNamespace(
		collect=Mock(
			return_value=[
				sensor.CpuTemperature("Example CPU", "Core (Tctl/Tdie)", 45.4),
			]
		)
	)
	return commands, environment


class CpuReportingTests(unittest.TestCase):
	def test_cpu_load_precedes_temperature_without_model_name(self):
		commands, environment = commandEnvironment()
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with("CPU load: 2.5% temperature: 45.4 degrees Celsius.")

	def test_existing_temperature_preference_is_used(self):
		commands, environment = commandEnvironment()
		environment["config"].conf["resourceMonitor"]["gpuTempUnit"] = "fahrenheit"
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with(
			"CPU load: 2.5% temperature: 113.7 degrees Fahrenheit."
		)

	def test_translator_can_reorder_the_combined_report(self):
		message = "CPU load: {load}% temperature: {temperature}."
		commands, environment = commandEnvironment(
			lambda text: "TEMP={temperature}; LOAD=%{load}" if text == message else text
		)
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with("TEMP=45.4 degrees Celsius; LOAD=%2.5")

	def test_failure_still_reports_cpu_load(self):
		commands, environment = commandEnvironment()
		commands._cpuTemperature.collect.side_effect = sensor.TemperatureUnavailable("driverUnavailable")
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with("CPU load: 2.5%. CPU temperature unavailable.")

	def test_original_cpu_command_never_queries_temperature(self):
		commands, environment = commandEnvironment()
		commands.script_announceProcessorInfo(None)
		environment["ui"].message.assert_called_once_with("2.5% average CPU load, Core 1: 10%, Core 2: 20%.")
		commands._cpuTemperature.collect.assert_not_called()

	def test_copy_and_termination(self):
		commands, environment = commandEnvironment()
		commands._cpuReportCopy = True
		commands._collectCpuTemperature(2.5)
		environment["api"].copyToClip.assert_called_once_with(
			"CPU load: 2.5% temperature: 45.4 degrees Celsius.", notify=True
		)
		commands._cpuReportClosed.set()
		commands._collectCpuTemperature(2.5)
		environment["api"].copyToClip.assert_called_once()
		environment["ui"].message.assert_not_called()


if __name__ == "__main__":
	unittest.main()
