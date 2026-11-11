"""Exercise NVDA command bodies without starting NVDA or the sensor host."""

import ast
from collections import Counter
import gettext
from pathlib import Path
import string
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from test_cpu_temperature import sensor


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "addon/globalPlugins/resourceMonitor/__init__.py"
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"))


def commandEnvironment(translate):
	functions = [
		node
		for node in TREE.body
		if isinstance(node, ast.FunctionDef) and node.name in ("formatTemperature", "tryTrunk")
	]
	plugin = next(
		node for node in TREE.body if isinstance(node, ast.ClassDef) and node.name == "GlobalPlugin"
	)
	names = {
		"script_announceProcessorInfo",
		"script_announceProcessorTemperature",
		"_collectCpuTemperature",
		"_cpuTemperatureFailureMessage",
		"_finishCpuReport",
	}
	methods = []
	for original in plugin.body:
		if isinstance(original, ast.FunctionDef) and original.name in names:
			node = ast.parse(ast.unparse(original)).body[0]
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
		"threading": SimpleNamespace(Thread=Mock(return_value=SimpleNamespace(start=Mock()))),
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
				sensor.CpuTemperature(
					"AMD Ryzen 5 7500F",
					"Core (Tctl/Tdie)",
					45.4,
				)
			]
		)
	)
	return commands, environment


class CpuReportingTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		with (ROOT / "addon/locale/tr/LC_MESSAGES/nvda.mo").open("rb") as catalog:
			cls.turkish = gettext.GNUTranslations(catalog)

	def test_requested_turkish_reading(self):
		commands, environment = commandEnvironment(self.turkish.gettext)
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with(
			"CPU yükü: %2.5 sıcaklık: 45.4 santigrat derece.",
		)

	def test_english_fallback_and_fahrenheit(self):
		commands, environment = commandEnvironment(gettext.NullTranslations().gettext)
		environment["config"].conf["resourceMonitor"]["gpuTempUnit"] = "fahrenheit"
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with(
			"CPU load: 2.5% temperature: 113.7 degrees Fahrenheit.",
		)

	def test_translators_can_reorder_report_and_unit(self):
		translations = {
			"CPU load: {load}% temperature: {temperature}.": "{temperature} | {load}%",
			"{value} {unit}": "{unit}: {value}",
		}
		commands, environment = commandEnvironment(lambda text: translations.get(text, text))
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with("degrees Celsius: 45.4 | 2.5%")

	def test_failure_message_is_localized(self):
		commands, environment = commandEnvironment(self.turkish.gettext)
		commands._cpuTemperature.collect.side_effect = sensor.TemperatureUnavailable("driverUnavailable")
		commands._collectCpuTemperature(2.5)
		environment["ui"].message.assert_called_once_with(
			"CPU yükü: %2.5. CPU sıcaklığı alınamadı: PawnIO sürücüsüne erişilemiyor.",
		)

	def test_original_command_does_not_start_sensor_host(self):
		commands, environment = commandEnvironment(gettext.NullTranslations().gettext)
		commands.script_announceProcessorInfo(None)
		environment["ui"].message.assert_called_once_with(
			"2.5% average CPU load, Core 1: 10%, Core 2: 20%.",
		)
		environment["threading"].Thread.assert_not_called()
		commands._cpuTemperature.collect.assert_not_called()

	def test_new_command_copies_requested_result(self):
		commands, environment = commandEnvironment(self.turkish.gettext)
		commands._cpuReportCopy = True
		commands._collectCpuTemperature(2.5)
		environment["api"].copyToClip.assert_called_once_with(
			"CPU yükü: %2.5 sıcaklık: 45.4 santigrat derece.",
			notify=True,
		)
		environment["ui"].message.assert_not_called()

	def test_new_translation_placeholders_are_preserved(self):
		messages = [
			"{value} {unit}",
			"CPU load: {load}% temperature: {temperature}.",
			"CPU load: {load}%. {status}",
		]

		def fields(text):
			return Counter(field for _, field, _, _ in string.Formatter().parse(text) if field is not None)

		for message in messages:
			with self.subTest(message=message):
				self.assertIn(message, self.turkish._catalog)
				self.assertEqual(fields(message), fields(self.turkish.gettext(message)))


if __name__ == "__main__":
	unittest.main()
