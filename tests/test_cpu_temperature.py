import importlib.util
import json
from pathlib import Path
import sys
import unittest


source = Path(__file__).resolve().parents[1] / "addon/globalPlugins/resourceMonitor/cpuTemperature.py"
spec = importlib.util.spec_from_file_location("cpuTemperature", source)
sensor = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = sensor
spec.loader.exec_module(sensor)


def reading(name, value, cpu="Ryzen"):
	return {"cpu": cpu, "name": name, "celsius": value}


def output(*readings):
	return json.dumps({"version": 1, "status": "ok", "sensors": readings})


class TemperatureTests(unittest.TestCase):
	def test_amd_die_is_preferred_to_ccd_and_control_temperature(self):
		result = sensor.parseTemperatures(
			output(
				reading("CCD1 (Tdie)", 60),
				reading("Core (Tctl)", 80),
				reading("Core (Tctl/Tdie)", 65),
			)
		)
		self.assertEqual([(item.sensor, item.celsius) for item in result], [("Core (Tctl/Tdie)", 65)])

	def test_intel_package_and_bom_are_supported(self):
		result = sensor.parseTemperatures("\ufeff" + output(reading("CPU Package", 52.5, "Intel")))
		self.assertEqual(result[0].celsius, 52.5)

	def test_ccd_is_not_reported_as_cpu_package(self):
		with self.assertRaises(sensor.TemperatureUnavailable):
			sensor.parseTemperatures(output(reading("CCD1 (Tdie)", 62)))

	def test_invalid_and_failed_zero_readings_are_rejected(self):
		for value in (0, -1, 151, True, "55", float("nan"), float("inf")):
			with self.subTest(value=value), self.assertRaises(sensor.TemperatureUnavailable):
				sensor.parseTemperatures(output(reading("CPU Package", value)))

	def test_protocol_errors_are_reported(self):
		for text in ("garbage", "[]", "null", '{"version":2}', '{"version":1,"status":"ok","sensors":null}'):
			with self.subTest(text=text), self.assertRaises(sensor.TemperatureUnavailable):
				sensor.parseTemperatures(text)

	def test_driver_failure_is_not_lost(self):
		with self.assertRaises(sensor.TemperatureUnavailable) as error:
			sensor.parseTemperatures('{"version":1,"status":"driverUnavailable","sensors":[]}')
		self.assertEqual(error.exception.reason, "driverUnavailable")

	def test_missing_helper_does_not_launch_anything(self):
		provider = sensor.CpuTemperatureProvider()
		provider._helper = Path(__file__).with_name("does-not-exist.exe")
		with self.assertRaises(sensor.TemperatureUnavailable) as error:
			provider.collect()
		self.assertEqual(error.exception.reason, "helperMissing")

	def test_closed_provider_does_not_start_a_new_host(self):
		provider = sensor.CpuTemperatureProvider()
		provider.close()
		with self.assertRaises(sensor.TemperatureUnavailable) as error:
			provider.collect()
		self.assertEqual(error.exception.reason, "closed")


if __name__ == "__main__":
	unittest.main()
