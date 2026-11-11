# Resource Monitor CPU temperature bridge. GPL-2.0-or-later.
"""Read the bundled sensor host without loading hardware drivers into NVDA."""

from ctypes import c_void_p, windll, wintypes
from dataclasses import dataclass
import json
import math
import os
from pathlib import Path
import subprocess
import threading
import uuid


class TemperatureUnavailable(Exception):
	def __init__(self, reason: str):
		super().__init__(reason)
		self.reason = reason


@dataclass(frozen=True)
class CpuTemperature:
	cpu: str
	sensor: str
	celsius: float


def parseTemperatures(output: str) -> list[CpuTemperature]:
	try:
		result = json.loads(output.lstrip("\ufeff"))
	except (ValueError, TypeError) as error:
		raise TemperatureUnavailable("invalidData") from error
	if not isinstance(result, dict) or result.get("version") != 1:
		raise TemperatureUnavailable("invalidData")
	if result.get("status") != "ok":
		raise TemperatureUnavailable(str(result.get("status", "invalidData")))
	sensors = result.get("sensors")
	if not isinstance(sensors, list):
		raise TemperatureUnavailable("invalidData")
	byCpu: dict[str, list[CpuTemperature]] = {}
	for sensor in sensors:
		if not isinstance(sensor, dict):
			continue
		cpu, name, value = sensor.get("cpu"), sensor.get("name"), sensor.get("celsius")
		if not isinstance(cpu, str) or not isinstance(name, str):
			continue
		if isinstance(value, bool) or not isinstance(value, (int, float)):
			continue
		if not math.isfinite(value) or not 0 < value <= 150:
			continue
		byCpu.setdefault(cpu, []).append(CpuTemperature(cpu, name, float(value)))
	# Do not silently substitute a CCD or motherboard sensor for the package/die sensor.
	preferred = ("Core (Tctl/Tdie)", "Core (Tdie)", "CPU Package", "Core (Tctl)")
	selected = []
	for readings in byCpu.values():
		for name in preferred:
			match = next((item for item in readings if item.sensor == name), None)
			if match is not None:
				selected.append(match)
				break
	if not selected:
		raise TemperatureUnavailable("noSensors")
	return selected


class CpuTemperatureProvider:
	def __init__(self):
		self._helper = Path(__file__).parent / "sensors" / "ResourceMonitor.CpuSensor.exe"
		self._pipe = f"ResourceMonitor.CpuSensor.{os.getpid()}.{uuid.uuid4().hex}"
		self._started = False
		self._closed = threading.Event()
		self._lock = threading.Lock()

	def _request(self, command: str) -> str:
		result = subprocess.run(
			[str(self._helper), command, self._pipe],
			capture_output=True,
			encoding="utf-8-sig",
			errors="replace",
			creationflags=subprocess.CREATE_NO_WINDOW,
			timeout=15 if command == "--read" else 2,
			check=False,
		)
		if result.returncode:
			raise TemperatureUnavailable("unavailable")
		return result.stdout

	def collect(self) -> list[CpuTemperature]:
		with self._lock:
			if self._closed.is_set():
				raise TemperatureUnavailable("closed")
			if not self._helper.is_file():
				raise TemperatureUnavailable("helperMissing")
			if not self._started:
				# Windows owns the UAC prompt; only the separate sensor host is elevated.
				launch = windll.shell32.ShellExecuteW
				launch.argtypes = (
					wintypes.HWND,
					wintypes.LPCWSTR,
					wintypes.LPCWSTR,
					wintypes.LPCWSTR,
					wintypes.LPCWSTR,
					wintypes.INT,
				)
				launch.restype = c_void_p
				code = launch(
					None,
					"runas",
					str(self._helper),
					f"--serve {os.getpid()} {self._pipe}",
					str(self._helper.parent),
					0,
				)
				if not code or code <= 32:
					raise TemperatureUnavailable("accessDenied")
				self._started = True
			try:
				return parseTemperatures(self._request("--read"))
			except (OSError, subprocess.SubprocessError) as error:
				self._started = False
				raise TemperatureUnavailable("unavailable") from error

	def close(self) -> None:
		self._closed.set()

		# Also handles reload during an in-progress UAC prompt: wait for collect's lock.
		def stop() -> None:
			with self._lock:
				if self._started:
					try:
						self._request("--stop")
					except (OSError, subprocess.SubprocessError, TemperatureUnavailable):
						pass

		threading.Thread(target=stop, name="resourceMonitorCpuStop", daemon=True).start()
