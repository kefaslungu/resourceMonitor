# Resource Monitor for NVDA
# Presents basic info on CPU load, memory, disk usage, and other resource information.
# Copyright 2013-2026 Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome
# released under GPL.
# This add-on uses Psutil, licensed under 3-Clause BSD License which is compatible with GPL.
# psutil is included in NVDA 2024.2 and later.

import functools
import os.path
import winsound
from ctypes import addressof, byref, POINTER, wintypes
from datetime import datetime
from typing import Any
import api
import config
import globalPluginHandler
import queueHandler
import scriptHandler
import inputCore
import ui
import winVersion
import wx
from gui import blockAction, guiHelper
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel
import psutil

# Windows Server systems prior to Server 2025 do not include wlanapi.dll.
try:
	from . import wlanapi

	wlanapiAvailable = True
except OSError:
	wlanapiAvailable = False
import addonHandler
from .gpu import BaseGpuProvider, getGpuProviders

addonHandler.initTranslation()


MODULE_DIR = os.path.dirname(__file__)

# Register this add-on's settings with NVDA's configuration system.
confspec = {
	"gpuTempUnit": "string(default=celsius)",
}
config.conf.spec["resourceMonitor"] = confspec


def message(text: str, fileName: str) -> None:
	ui.message(text)
	path = os.path.join(MODULE_DIR, fileName)
	if os.path.exists(path):
		winsound.PlaySound(path, winsound.SND_ASYNC)


try:
	SECURITY_TYPE = {
		wlanapi.DOT11_AUTH_ALGO_80211_OPEN: _("No authentication (Open)"),
		wlanapi.DOT11_AUTH_ALGO_80211_SHARED_KEY: "WEP",
		wlanapi.DOT11_AUTH_ALGO_WPA: "WPA-Enterprise",
		wlanapi.DOT11_AUTH_ALGO_WPA_PSK: "WPA-PSK",
		wlanapi.DOT11_AUTH_ALGO_RSNA: "WPA2-Enterprise",
		wlanapi.DOT11_AUTH_ALGO_RSNA_PSK: "WPA2-PSK",
		wlanapi.DOT11_AUTH_ALGO_WPA3_ENT_192: "WPA3-Enterprise-192bit",
		wlanapi.DOT11_AUTH_ALGO_WPA3_SAE: "WPA3-SAE",
		wlanapi.DOT11_AUTH_ALGO_OWE: "OWE",
		wlanapi.DOT11_AUTH_ALGO_WPA3_ENT: "WPA3-Enterprise",
	}

	@wlanapi.WLAN_NOTIFICATION_CALLBACK
	def notifyHandler(pData: Any, pCtx: Any):
		if pData.contents.NotificationSource != wlanapi.WLAN_NOTIFICATION_SOURCE_ACM:
			return
		match pData.contents.NotificationCode:
			case wlanapi.wlan_notification_acm_connection_complete:
				notificationData = wlanapi.WLAN_CONNECTION_NOTIFICATION_DATA.from_address(pData.contents.pData)
				if notificationData.wlanReasonCode != wlanapi.ERROR_SUCCESS:
					return
				ssid = notificationData.dot11Ssid.SSID
				queueHandler.queueFunction(
					queueHandler.eventQueue,
					message,
					_("Connected to {}").format(ssid.decode("utf-8")),
					"connect.wav",
				)
			case wlanapi.wlan_notification_acm_disconnected:
				ssid = wlanapi.WLAN_CONNECTION_NOTIFICATION_DATA.from_address(
					pData.contents.pData
				).dot11Ssid.SSID
				queueHandler.queueFunction(
					queueHandler.eventQueue,
					message,
					_("Disconnected from {}").format(ssid.decode("utf-8")),
					"disconnect.wav",
				)
			case wlanapi.wlan_notification_acm_interface_arrival:
				queueHandler.queueFunction(
					queueHandler.eventQueue, message, _("A wireless device has been enabled"), "connect.wav"
				)
			case wlanapi.wlan_notification_acm_interface_removal:
				queueHandler.queueFunction(
					queueHandler.eventQueue,
					message,
					_("A wireless device has been disabled"),
					"disconnect.wav",
				)
			case _:
				pass
except NameError:
	pass


def customResize(array: Any, newSize: Any):
	return (array._type_ * newSize).from_address(addressof(array))


# Styles of size calculation/string composition, do not change!
# Traditional style, Y, K, M, G, B, ...
traditional = [
	(1024.0**10.0, "Q"),
	(1024.0**9.0, "R"),
	(1024.0**8.0, "Y"),
	(1024.0**7.0, "Z"),
	(1024.0**6.0, "E"),
	(1024.0**5.0, "P"),
	(1024.0**4.0, "T"),
	(1024.0**3.0, "G"),
	(1024.0**2.0, "M"),
	(1024.0**1.0, "K"),
	(1024.0**0.0, "B"),
]

# Alternative style (displayed with most PCs): MB, KB, GB, YB, ZB, ...
alternative = [
	(1024.0**10.0, " QB"),
	(1024.0**9.0, " RB"),
	(1024.0**8.0, " YB"),
	(1024.0**7.0, " ZB"),
	(1024.0**6.0, " EB"),
	(1024.0**5.0, " PB"),
	(1024.0**4.0, " TB"),
	(1024.0**3.0, " GB"),
	(1024.0**2.0, " MB"),
	(1024.0**1.0, " KB"),
	(1024.0**0.0, (" byte", " bytes")),
]

# Verbose style: Kilobytes, Megabytes, Gigabytes, ...
verbose = [
	(1024.0**10.0, " quettabytes"),
	(1024.0**9.0, " ronnabytes"),
	(1024.0**8.0, " yottabytes"),
	(1024.0**7.0, " zettabytes"),
	(1024.0**6.0, " exabytes"),
	(1024.0**5.0, (" petabyte", " petabytes")),
	(1024.0**4.0, (" terabyte", " terabytes")),
	(1024.0**3.0, (" gigabyte", " gigabytes")),
	(1024.0**2.0, (" megabyte", " megabytes")),
	(1024.0**1.0, (" kilobyte", " kilobytes")),
	(1024.0**0.0, (" byte", " bytes")),
]

# International Electrotechnical Commission (IEC) style: Ki, Mi, Gi, Ti, ...
iec = [
	(1024.0**10.0, "Qi"),
	(1024.0**9.0, "Ri"),
	(1024.0**8.0, "Yi"),
	(1024.0**7.0, "Zi"),
	(1024.0**6.0, "Ei"),
	(1024.0**5.0, "Pi"),
	(1024.0**4.0, "Ti"),
	(1024.0**3.0, "Gi"),
	(1024.0**2, "Mi"),
	(1024.0**1.0, "Ki"),
	(1024.0**0.0, ""),
]

# International System of Units (Si) style: each unit is 1000 of another (i.e. 1000 KB is 1 MB)
si = [
	(1000.0**10.0, "Q"),
	(1000.0**9.0, "R"),
	(1000.0**8.0, "Y"),
	(1000.0**7.0, "Z"),
	(1000.0**6.0, "E"),
	(1000.0**5.0, "P"),
	(1000.0**4.0, "T"),
	(1000.0**3.0, "G"),
	(1000.0**2.0, "M"),
	(1000.0**1.0, "K"),
	(1000.0**0.0, "B"),
]


def size(bytes: int, system: list[tuple[float, Any]] = traditional) -> str:
	for factor, suffix in system:
		if float(bytes) >= float(factor):
			break
	amount = float(bytes / factor)
	if isinstance(suffix, tuple):
		singular, multiple = suffix
		if float(amount) == 1.0:
			suffix = singular
		else:
			suffix = multiple
	return "{:.2F}{}".format(float(amount), suffix)


def tryTrunk(n: float) -> int | float:
	# This method basically removes decimal zeros, so 5.0 will just be 5.
	# If the number ends in anything other than a 0,
	# nothing happens (if the trunkated number is not equal to the decimal).
	if n == int(n):
		return int(n)
	return n


def formatGpuTemperature(celsiusText: str) -> str:
	# GPU providers report temperature in degrees Celsius as text.
	# Convert it to the user's preferred unit (Celsius or Fahrenheit) for display.
	try:
		celsius = float(celsiusText)
	except (TypeError, ValueError):
		return celsiusText
	unit = config.conf["resourceMonitor"]["gpuTempUnit"]
	if unit == "fahrenheit":
		value = celsius * 9.0 / 5.0 + 32.0
		# Translators: Fahrenheit temperature unit symbol appended to a GPU temperature value.
		symbol = _("degrees Fahrenheit")
	else:
		value = celsius
		# Translators: Celsius temperature unit symbol appended to a GPU temperature value.
		symbol = _("degrees Celsius")
	return "{} {}".format(tryTrunk(round(value, 1)), symbol)


def formatGpuMemory(usedMibText: str, totalMibText: str) -> str | None:
	# GPU providers report memory used/total in MiB as text (nvidia-smi's "nounits" output).
	try:
		usedMib = float(usedMibText)
		totalMib = float(totalMibText)
	except (TypeError, ValueError):
		return None
	if totalMib <= 0:
		return None
	usedBytes = usedMib * 1024.0 * 1024.0
	totalBytes = totalMib * 1024.0 * 1024.0
	# Translators: Shows GPU memory usage (example: 2.00 GB of 8.00 GB used (25%)).
	return _("{used} of {total} used ({percent}%)").format(
		used=size(usedBytes, alternative),
		total=size(totalBytes, alternative),
		percent=tryTrunk(round(usedBytes / totalBytes * 100, 1)),
	)


class ResourceMonitorSettingsPanel(SettingsPanel):
	# Translators: Category title for Resource Monitor settings in NVDA's settings dialog.
	title = _("Resource Monitor")

	def makeSettings(self, settingsSizer: wx.BoxSizer) -> None:
		settingsSizerHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: Label for a combo box to select the unit used to report GPU temperature.
		gpuTempUnitLabelText = _("GPU &temperature unit:")
		# Translators: An option in the GPU temperature unit combo box.
		self._gpuTempUnitLabels = [_("Celsius"), _("Fahrenheit")]
		self._gpuTempUnitValues = ["celsius", "fahrenheit"]
		self.gpuTempUnitList = settingsSizerHelper.addLabeledControl(
			gpuTempUnitLabelText,
			wx.Choice,
			choices=self._gpuTempUnitLabels,
		)
		try:
			currentIndex = self._gpuTempUnitValues.index(config.conf["resourceMonitor"]["gpuTempUnit"])
		except ValueError:
			currentIndex = 0
		self.gpuTempUnitList.SetSelection(currentIndex)

	def onSave(self) -> None:
		selection = self.gpuTempUnitList.GetSelection()
		if selection == wx.NOT_FOUND:
			selection = 0
		config.conf["resourceMonitor"]["gpuTempUnit"] = self._gpuTempUnitValues[selection]


@functools.lru_cache(maxsize=1)
def getWinVer() -> str:
	# Obtain current Windows version.
	# Windows version info (major.minor.build.servicePack.productType) comes from winVersion.getWinVer.
	currentWinVer = winVersion.getWinVer()
	# Announce actual machine architecture (x86/32-bit, AMD64, ARM64).
	arch = currentWinVer.processorArchitecture
	# All publicly released Windows releases are represented by a winVersion.WinVersion instance.
	# NVDA uses client release names for "releaseName" attribute.
	# Specifically, NVDA obtains Windows 10/11 release names from Windows Registry.
	winverName = currentWinVer.releaseName
	# Report "Windows Server version" on servers.
	if currentWinVer.productType != "workstation":
		winverName = f"Windows Server {winverName.rpartition(' ')[-1]}"
	# Announce build.revision.
	buildRevision = f"{currentWinVer.build}.{currentWinVer.revision}"
	# Translators: Presents Windows version (example output: "Windows 10 22H2 (AMD64) build 19045.5247").
	info = _("{winVersion} ({cpuBit}) build {build}").format(
		winVersion=winverName, cpuBit=arch, build=buildRevision
	)
	return info


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: The gestures category for this add-on in input gestures dialog (2013.3 or later).
	scriptCategory = _("Resource Monitor")

	def __init__(self):
		super().__init__()
		self._gpuProviders: list[BaseGpuProvider] = getGpuProviders()
		NVDASettingsDialog.categoryClasses.append(ResourceMonitorSettingsPanel)
		if not wlanapiAvailable:
			self._client_handle = None
			return
		self._negotiated_version = wintypes.DWORD()
		self._client_handle = wintypes.HANDLE()
		try:
			wlanapi.WlanOpenHandle(
				wlanapi.CLIENT_VERSION_WINDOWS_VISTA_OR_LATER,
				None,
				byref(self._negotiated_version),
				byref(self._client_handle),
			)
			wlanapi.WlanRegisterNotification(
				self._client_handle,
				wlanapi.WLAN_NOTIFICATION_SOURCE_ACM,
				True,
				notifyHandler,
				None,
				None,
				None,
			)
		except OSError:
			pass

	def terminate(self):
		super().terminate()
		self._gpuProviders.clear()
		if ResourceMonitorSettingsPanel in NVDASettingsDialog.categoryClasses:
			NVDASettingsDialog.categoryClasses.remove(ResourceMonitorSettingsPanel)
		if not self._client_handle:
			return
		self._negotiated_version = None
		try:
			wlanapi.WlanRegisterNotification(
				self._client_handle,
				wlanapi.WLAN_NOTIFICATION_SOURCE_NONE,
				True,
				notifyHandler,
				None,
				None,
				None,
			)
			wlanapi.WlanCloseHandle(
				byref(self._client_handle),
				None,
			)
			self._client_handle = None
		except OSError:
			pass

	@scriptHandler.script(
		# Translators: Input help mode message about overall system resource info command in Resource Monitor
		description=_("Presents used ram and average processor load."),
		gesture="KB:NVDA+shift+e",
		speakOnDemand=True,
	)
	def script_announceResourceSummary(self, gesture: inputCore.InputGesture):
		# Faster to build info on the fly rather than keep appending to a string.
		# Translators: presents the overall summary of resource usage, such as CPU load and RAM usage.
		info = [
			_("{ramPercent}% RAM used, CPU at {cpuPercent}%.").format(
				ramPercent=tryTrunk(psutil.virtual_memory()[2]), cpuPercent=tryTrunk(psutil.cpu_percent())
			)
		]
		ui.message(" ".join(info))

	@scriptHandler.script(
		# Translators: Input help mode message about processor info command in Resource Monitor.
		description=_(
			"Presents the average processor load and the load of each core. "
			"If pressed twice, copies the information to the clipboard."
		),
		gesture="KB:NVDA+shift+1",
		speakOnDemand=True,
	)
	def script_announceProcessorInfo(self, gesture: inputCore.InputGesture):
		averageLoad = psutil.cpu_percent()
		# Lists load for each core
		perCpuLoad = psutil.cpu_percent(percpu=True)
		coreLoad = [
			# Translators: Shows average load of CPU cores (example: core 1, 50%).
			_("Core {coreNumber}: {corePercent}%").format(coreNumber=core, corePercent=tryTrunk(cpuLoad))
			# Start counting at 1, and even then, all items will be visited.
			for core, cpuLoad in enumerate(perCpuLoad, start=1)
		]
		# Only display average CPU load on single-core systems.
		if psutil.cpu_count() == 1:
			# Translators: Shows average load of the processor on single-core systems.
			info = _("{avgLoad}% CPU load.").format(avgLoad=tryTrunk(averageLoad))
		else:
			# Translators: Shows average load of the processor and the load for each core on multi-core systems.
			info = _("{avgLoad}% average CPU load, {cores}.").format(
				avgLoad=tryTrunk(averageLoad), cores=", ".join(coreLoad)
			)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about memory info command in Resource Monitor.
		description=_(
			"Presents the used and total space for both physical and virtual ram. "
			"If pressed twice, copies the information to the clipboard."
		),
		gestures=["KB:NVDA+shift+2", "KB:NVDA+shift+5"],
		speakOnDemand=True,
	)
	def script_announceRamInfo(self, gesture: inputCore.InputGesture):
		memory = psutil.virtual_memory()
		physicalRamUsed, physicalRamTotal = memory.used, memory.total
		# Translators: Shows RAM (physical memory) usage.
		info = _("Physical: {physicalUsed} of {physicalTotal} used ({physicalPercent}%). ").format(
			physicalUsed=size(physicalRamUsed, alternative),
			physicalTotal=size(physicalRamTotal, alternative),
			physicalPercent=tryTrunk(round(physicalRamUsed / physicalRamTotal * 100, 1)),
		)
		virtualMemory = psutil._psutil_windows.virtual_mem()
		virtualRamUsed, virtualRamTotal = virtualMemory[2] - virtualMemory[3], virtualMemory[2]
		# Translators: Shows virtual memory usage.
		info += _("Virtual: {virtualUsed} of {virtualTotal} used ({virtualPercent}%).").format(
			virtualUsed=size(virtualRamUsed, alternative),
			virtualTotal=size(virtualRamTotal, alternative),
			virtualPercent=tryTrunk(round(virtualRamUsed / virtualRamTotal * 100, 1)),
		)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help message about drive info command in Resource Monitor.
		description=_(
			"Presents the used and total space of the fixed (built-in), removable, and mapped network drives on this computer. "
			"If pressed twice, copies the information to the clipboard."
		),
		gesture="KB:NVDA+shift+3",
		speakOnDemand=True,
	)
	def script_announceDriveInfo(self, gesture: inputCore.InputGesture):
		# Goes through all registered drives, including mapped network drives, and gives info on each one.
		# psutil.disk_partitions() defaults to all=False, which silently excludes mapped network
		# drives on Windows (they're not considered "physical" devices). Passing all=True brings
		# them back in.
		info = []
		for drive in psutil.disk_partitions(all=True):
			# Get info on each one.
			# If and only if Windows says the disk is ready do we query it, in order to avoid
			# a core stack freeze when no disk is inserted into a slot, or a mapped network
			# drive has never been connected.
			# This can be checked by looking for a file system.
			if not drive.fstype:
				continue
			isNetworkDrive = "remote" in drive.opts.split(",")
			try:
				driveInfo = psutil.disk_usage(drive[0])
			except OSError:
				# The drive is registered but currently can't be reached, e.g. an offline
				# mapped network drive whose host is unreachable.
				if isNetworkDrive:
					# Translators: Reported when a mapped network drive is currently unreachable.
					info.append(_("{driveName} (network drive): not available.").format(driveName=drive[0]))
				continue
			# Translators: word used to describe a mapped network drive.
			driveType = _("network") if isNetworkDrive else drive[2]
			info.append(
				# Translators: Shows drive letter, type of drive (fixed, removable, or network),
				# used capacity and total capacity of a drive
				# (example: C drive, ntfs; 40 GB of 100 GB used (40%).
				_("{driveName} ({driveType} drive): {usedSpace} of {totalSpace} used ({percent}%).").format(
					driveName=drive[0],
					driveType=driveType,
					usedSpace=size(driveInfo[1], alternative),
					totalSpace=size(driveInfo[0], alternative),
					percent=tryTrunk(driveInfo[3]),
				)
			)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(" ".join(info))
		else:
			api.copyToClip(" ".join(info), notify=True)

	def _getWlanInfo(self) -> str:
		if not self._client_handle:
			return _("No wireless devices")

		wlan_ifaces = POINTER(wlanapi.WLAN_INTERFACE_INFO_LIST)()
		wlanapi.WlanEnumInterfaces(self._client_handle, None, byref(wlan_ifaces))

		if wlan_ifaces.contents.NumberOfItems == 0:
			wlanapi.WlanFreeMemory(wlan_ifaces)
			return _("No wireless devices")

		for i in customResize(wlan_ifaces.contents.InterfaceInfo, wlan_ifaces.contents.NumberOfItems):
			if i.isState != wlanapi.wlan_interface_state_connected:
				info = _("No wireless connections")
				continue

			wlan_available_network_list = POINTER(wlanapi.WLAN_AVAILABLE_NETWORK_LIST)()
			wlanapi.WlanGetAvailableNetworkList(
				self._client_handle, byref(i.InterfaceGuid), 0, None, byref(wlan_available_network_list)
			)
			for n in customResize(
				wlan_available_network_list.contents.Network,
				wlan_available_network_list.contents.NumberOfItems,
			):
				if n.Flags & wlanapi.WLAN_AVAILABLE_NETWORK_CONNECTED:
					info = _(
						"Connected to {}, signal strength: {}%, security type: {}"
					).format(
						n.dot11Ssid.SSID.decode(),
						n.wlanSignalQuality,
						SECURITY_TYPE.get(n.dot11DefaultAuthAlgorithm),
					)
					break
			wlanapi.WlanFreeMemory(wlan_available_network_list)
		wlanapi.WlanFreeMemory(wlan_ifaces)
		return info

	@scriptHandler.script(
		# Translators: Input help mode message about obtaining the ssid of the wireless network,
		# and the strength of the network.
		description=_(
			"Announces the system's wireless network name (SSID), connection strength, and security  protocol. "
			"If pressed twice, copies the information to the clipboard."
		),
		gesture="kb:NVDA+shift+4",
		speakOnDemand=True,
	)
	def script_wlanStatusReport(self, gesture: inputCore.InputGesture):
		info = self._getWlanInfo()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about Windows version command in Resource Monitor.
		description=_(
			"Announces the version of Windows you are using. "
			"If pressed twice, copies the information to the clipboard."
		),
		gesture="KB:NVDA+shift+6",
		speakOnDemand=True,
	)
	def script_announceWinVer(self, gesture: inputCore.InputGesture):
		# Unlike other resource usage information, current Windows version info is static.
		info = getWinVer()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	def getUptime(self) -> str:
		bootTimestamp = psutil.boot_time()
		if bootTimestamp == 0.0:
			raise TypeError
		uptime = datetime.now() - datetime.fromtimestamp(bootTimestamp)
		hours, remainingMinutes = divmod(uptime.seconds, 3600)
		minutes, seconds = divmod(remainingMinutes, 60)
		uptimeComponents = []
		uptimeComponents.append(
			# Translators: system uptime in days.
			ngettext("{days:d} day", "{days:d} days", uptime.days).format(days=uptime.days)
		)
		uptimeComponents.append(
			# Translators: system uptime in hours.
			ngettext("{hours:d} hour", "{hours:d} hours", hours).format(hours=hours)
		)
		uptimeComponents.append(
			# Translators: system uptime in minutes.
			ngettext("{minutes:d} minute", "{minutes:d} minutes", minutes).format(minutes=minutes)
		)
		uptimeComponents.append(
			# Translators: system uptime in seconds.
			ngettext("{seconds:d} second", "{seconds:d} seconds", seconds).format(seconds=seconds)
		)
		return ", ".join(uptimeComponents)

	@scriptHandler.script(
		# Translators: Input help mode message about obtaining the system's uptime
		description=_(
			"Announces the system's uptime. "
			"If pressed twice, copies the information to the clipboard."
		),
		gesture="kb:NVDA+shift+7",
		speakOnDemand=True,
	)
	def script_announceUptime(self, gesture: inputCore.InputGesture):
		try:
			uptime = self.getUptime()
			if scriptHandler.getLastScriptRepeatCount() == 0:
				ui.message(uptime)
			else:
				api.copyToClip(uptime, notify=True)
		except TypeError:
			# Translators: Obtaining uptime failed
			ui.message(_("Failed to get the system's uptime."))

	def _getGpuInfo(self) -> str:
		hasProvider = False
		hasFailure = False
		for provider in self._gpuProviders:
			telemetry = provider.collect()
			if telemetry is None:
				continue
			hasProvider = True
			if not telemetry:
				hasFailure = True
				continue
			gpuInfoParts = []
			for index, item in enumerate(telemetry, start=1):
				gpuInfoParts.append(
					_("GPU {gpuNumber}: usage {usage}%, temp {temperature}.").format(
						gpuNumber=index,
						usage=item.utilization,
						temperature=formatGpuTemperature(item.temperature),
					)
				)
			if gpuInfoParts:
				return " ".join(gpuInfoParts)
			hasFailure = True
		if not hasProvider:
			return _("No GPU information available.")
		if hasFailure:
			return _("Unable to get GPU information.")
		return _("No GPU data available.")

	@scriptHandler.script(
		# Translators: Input help mode message about GPU usage and temperature command.
		description=_(
			"Announces GPU usage and temperature. "
			"If pressed twice, copies the information to the clipboard."
		),
		speakOnDemand=True,
	)
	# Do not report GPU info in secure mode
	# (for NVIDIA, GPU info is obtained by parsing output from another program,
	# potentially introducing security issues such as parsing problems).
	@blockAction.when(blockAction.Context.SECURE_MODE)
	def script_announceGpuInfo(self, gesture: inputCore.InputGesture):
		try:
			info = self._getGpuInfo()
			if scriptHandler.getLastScriptRepeatCount() == 0:
				ui.message(info)
			else:
				api.copyToClip(info, notify=True)
		except Exception:
			# Translators: Message reported when the GPU command fails unexpectedly.
			ui.message(_("Failed to get GPU information."))

	def _getGpuMemoryInfo(self) -> str:
		hasProvider = False
		hasFailure = False
		for provider in self._gpuProviders:
			telemetry = provider.collect()
			if telemetry is None:
				continue
			hasProvider = True
			if not telemetry:
				hasFailure = True
				continue
			gpuMemoryParts = []
			for index, item in enumerate(telemetry, start=1):
				memoryInfo = formatGpuMemory(item.memoryUsed, item.memoryTotal)
				if not memoryInfo:
					continue
				gpuMemoryParts.append(
					# Translators: Shows GPU memory usage (example: GPU 1: 2.00 GB of 8.00 GB used (25%)).
					_("GPU {gpuNumber}: {memoryInfo}.").format(
						gpuNumber=index,
						memoryInfo=memoryInfo,
					)
				)
			if gpuMemoryParts:
				return " ".join(gpuMemoryParts)
			hasFailure = True
		if not hasProvider:
			return _("No GPU information available.")
		if hasFailure:
			return _("Unable to get GPU memory information.")
		return _("No GPU data available.")

	@scriptHandler.script(
		# Translators: Input help mode message about GPU memory (VRAM) command.
		description=_(
			"Announces GPU memory usage. "
			"If pressed twice, copies the information to the clipboard."
		),
		speakOnDemand=True,
	)
	# Do not report GPU info in secure mode
	# (for NVIDIA, GPU info is obtained by parsing output from another program,
	# potentially introducing security issues such as parsing problems).
	@blockAction.when(blockAction.Context.SECURE_MODE)
	def script_announceGpuMemoryInfo(self, gesture: inputCore.InputGesture):
		try:
			info = self._getGpuMemoryInfo()
			if scriptHandler.getLastScriptRepeatCount() == 0:
				ui.message(info)
			else:
				api.copyToClip(info, notify=True)
		except Exception:
			# Translators: Message reported when the GPU memory command fails unexpectedly.
			ui.message(_("Failed to get GPU memory information."))
