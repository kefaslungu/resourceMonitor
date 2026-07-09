# Resource Monitor for NVDA
# Presents GPU information
# Copyright 2026 Kevin Derome, Joseph Lee, released under GPL

import os
import os.path
import shutil
import subprocess
from dataclasses import dataclass


@dataclass
class GpuTelemetry:
	utilization: str
	temperature: str


# Prevents a conhost.exe console window from flashing on screen when running
# nvidia-smi/where.exe, and avoids NVDA's UIAHandler logging errors while it
# tries (and fails) to probe a console window that closes almost immediately.
_CREATE_NO_WINDOW = 0x08000000


class BaseGpuProvider:
	def collect(self) -> list[GpuTelemetry] | None:
		raise NotImplementedError


class NvidiaGpuProvider(BaseGpuProvider):
	def __init__(self):
		super().__init__()
		self._nvidiaSmiPath = None
		self._nvidiaSmiPathResolved = False

	def _findNvidiaSmiPath(self) -> str | None:
		candidates = []
		for commandName in ("nvidia-smi", "nvidia-smi.exe"):
			found = shutil.which(commandName)
			if found:
				candidates.append(found)
		try:
			whereResult = subprocess.run(
				["where.exe", "nvidia-smi"],
				capture_output=True,
				text=True,
				timeout=2,
				check=False,
				creationflags=_CREATE_NO_WINDOW,
			)
			for line in whereResult.stdout.splitlines():
				path = line.strip().strip('"')
				if path:
					candidates.append(path)
		except (OSError, subprocess.TimeoutExpired):
			pass
		windowsDir = os.environ.get("WINDIR", r"C:\Windows")
		candidates.append(os.path.join(windowsDir, "System32", "nvidia-smi.exe"))
		candidates.append(os.path.join(windowsDir, "Sysnative", "nvidia-smi.exe"))
		for envVar in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)"):
			basePath = os.environ.get(envVar)
			if not basePath:
				continue
			candidates.append(
				os.path.join(basePath, "NVIDIA Corporation", "NVSMI", "nvidia-smi.exe")
			)
		seen = set()
		for path in candidates:
			normalizedPath = os.path.normcase(os.path.abspath(path))
			if normalizedPath in seen:
				continue
			seen.add(normalizedPath)
			if os.path.isfile(path):
				return path
		return None

	def collect(self) -> list[GpuTelemetry] | None:
		if not self._nvidiaSmiPathResolved:
			self._nvidiaSmiPath = self._findNvidiaSmiPath()
			self._nvidiaSmiPathResolved = True
		if not self._nvidiaSmiPath:
			return None
		try:
			result = subprocess.run(
				[
					self._nvidiaSmiPath,
					"--query-gpu=utilization.gpu,temperature.gpu",
					"--format=csv,noheader,nounits",
				],
				capture_output=True,
				text=True,
				timeout=5,
				check=True,
				creationflags=_CREATE_NO_WINDOW,
			)
		except (subprocess.CalledProcessError, OSError, subprocess.TimeoutExpired):
			return []
		lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
		if not lines:
			return []
		items: list[GpuTelemetry] = []
		for line in lines:
			gpuData = [part.strip() for part in line.split(",")]
			if len(gpuData) < 2:
				continue
			items.append(GpuTelemetry(utilization=gpuData[0], temperature=gpuData[1]))
		return items


def getGpuProviders() -> list[BaseGpuProvider]:
	return [NvidiaGpuProvider()]
