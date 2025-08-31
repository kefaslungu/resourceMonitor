# Resource Monitor for NVDA
# Presents basic info on CPU load, memory and disk usage, as well as battery information.
# Copyright 2013-2025 Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst,
# released under GPL.
# This add-on uses Psutil, licensed under 3-Clause BSD License which is compatible with GPL.
# psutil is included in NVDA 2024.2 and later.

import functools
import os.path
import queueHandler
import winreg
import winsound
from ctypes import addressof, byref, POINTER, wintypes
from datetime import datetime
from typing import Any
import api
import globalPluginHandler
import scriptHandler
import ui
import winVersion
import psutil

# Windows Server systems prior to Server 2025 do not include wlanapi.dll.
try:
	from . import wlanapi

	wlanapiAvailable = True
except OSError:
	wlanapiAvailable = False

from .networkSpeed import NetworkSpeed

import addonHandler

addonHandler.initTranslation()


MODULE_DIR = os.path.dirname(__file__)


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
	def notifyHandler(pData, pCtx):
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


def customResize(array, newSize):
	return (array._type_ * newSize).from_address(addressof(array))


# Styles of size calculation/string composition, do not change!
# Traditional style, Y, K, M, G, B, ...
traditional = [
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


# Moved from battery module to the main module in 2019 (code provided by Alex Hall)
def _batteryInfo(verbose: bool = False) -> str | None:
	# Returns current battery status provided that the computer has a detectable battery.
	# The verbose argument will force this function to return something if there is no battery.
	info = None
	# Uses psutil.sensors_battery function except it also checks battery low/critical flags.
	battery = psutil.sensors_battery()
	if battery is None:
		# Translators: Message reported when there is no battery on the system,
		# mostly laptops with battery pack removed and running on AC power.
		info = _("This computer does not have a battery connected.") if verbose else None
	else:
		percent, secsleft, power_plugged = battery
		if power_plugged:
			# Translators: message presented when AC is connected and battery is charging,
			# also show current battery percentage.
			info = _("{percent}%, battery charging.").format(percent=tryTrunk(percent))
		else:
			# Announce time unknown status.
			if secsleft == 0xFFFFFFFF:
				# Translators: message presented when computer is running on battery power,
				# showing percentage remaining yet battery time is unknown.
				info = _("{percent}% battery remaining, battery time unknown.").format(
					percent=tryTrunk(percent)
				)
			else:
				# Prepare hours:minutes.
				# Optimization: build components list and take away seconds
				# as it is not required (floor division with 60).
				timeLeft = []
				secsleft = secsleft // 60
				hours, minutes = divmod(secsleft, 60)
				# For hours and minutes, formatted string literals will be appended.
				if hours > 0:
					timeLeft.append(
						# Translators: battery and system uptime in hours.
						ngettext("{hours:d} hour", "{hours:d} hours", hours).format(hours=hours)
					)
				# Translators: battery and system uptime in minutes.
				timeLeft.append(
					# Translators: battery and system uptime in minutes.
					ngettext("{minutes:d} minute", "{minutes:d} minutes", minutes).format(minutes=minutes)
				)
				# Because psutil.sensors_battery function does not present battery flags by default,
				# manually read this info at the cost of calling the C extension twice.
				batteryFlags = psutil._psutil_windows.sensors_battery()[1]
				info = _(
					# Translators: message presented when computer is running on battery power,
					# showing percentage remaining and estimated remaining time.
					"{percent}% battery remaining, about {time}."
				).format(percent=tryTrunk(percent), time=", ".join(timeLeft))
				if batteryFlags & 2:
					# Translators: Message reported when battery level is low.
					info += _(" Warning: low battery.")
				elif batteryFlags & 4:
					# Translators: Message reported when battery level is critical.
					info += _(" Warning: critically low battery.")
	return info


# Record Windows Server builds to release names.
# Client versions will be checked via Registry.
serverReleaseNames = {
	14393: "Windows Server 2016",
	17763: "Windows Server 2019",
	20348: "Windows Server 2022",
	26100: "Windows Server 2025",
}


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
		winverName = serverReleaseNames.get(
			# All publicly available server release names are housed inside a dedicated map.
			currentWinVer.build,
			# On Windows 10 and later, NVDA uses a three-part string (Windows name releaseId).
			# Use reverse partition (str.rpartition) to obtain just the release Id (last part).
			f"Windows Server {winverName.rpartition(' ')[-1]}",
		)
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
		# Create and start the thread that monitors the network connection to calculate the transmission speed
		self.internetSpeedMonitor =  NetworkSpeed()
		self.internetSpeedMonitor.start()

	@scriptHandler.script(
		description=_(
			# Translators: Input help message about battery info command in Resource Monitor.
			"Presents battery percentage, charging status, remaining time (if not charging), "
			"and a warning if the battery is low or critical."
		),
		gesture="KB:NVDA+shift+4",
		speakOnDemand=True,
	)
	def script_announceBatteryInfo(self, gesture):
		info = _batteryInfo(verbose=True)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help message about drive info command in Resource Monitor.
		description=_(
			"Presents the used and total space of the static and removable drives on this computer."
		),
		gesture="KB:NVDA+shift+3",
		speakOnDemand=True,
	)
	def script_announceDriveInfo(self, gesture):
		# Goes through all registered drives and gives info on each one
		info = []
		for drive in psutil.disk_partitions():
			# Get info on each one
			# If and only if the Windows says disk is ready in order to avoid
			# a core stack freeze when no disk is inserted into a slot.
			# This can be checked by looking for a file system.
			if drive.fstype:
				driveInfo = psutil.disk_usage(drive[0])
				info.append(
					# Translators: Shows drive letter, type of drive (fixed or removable),
					# used capacity and total capacity of a drive
					# (example: C drive, ntfs; 40 GB of 100 GB used (40%).
					_("{driveName} ({driveType} drive): {usedSpace} of {totalSpace} used {percent}%.").format(
						driveName=drive[0],
						driveType=drive[2],
						usedSpace=size(driveInfo[1], alternative),
						totalSpace=size(driveInfo[0], alternative),
						percent=tryTrunk(driveInfo[3]),
					)
				)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(" ".join(info))
		else:
			api.copyToClip(" ".join(info), notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about processor info command in Resource Monitor.
		description=_("Presents the average processor load and the load of each core."),
		gesture="KB:NVDA+shift+1",
		speakOnDemand=True,
	)
	def script_announceProcessorInfo(self, gesture):
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
			info = _("Average CPU load {avgLoad}%.").format(avgLoad=tryTrunk(averageLoad))
		else:
			# Translators: Shows average load of the processor and the load for each core on multi-core systems.
			info = _("Average CPU load {avgLoad}%, {cores}.").format(
				avgLoad=tryTrunk(averageLoad), cores=", ".join(coreLoad)
			)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about memory info command in Resource Monitor.
		description=_("Presents the used and total space for both physical and virtual ram."),
		gestures=["KB:NVDA+shift+2", "KB:NVDA+shift+5"],
		speakOnDemand=True,
	)
	def script_announceRamInfo(self, gesture):
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
		# Translators: Input help mode message about Windows version command in Resource Monitor.
		description=_("Announces the version of Windows you are using."),
		gesture="KB:NVDA+shift+6",
		speakOnDemand=True,
	)
	def script_announceWinVer(self, gesture):
		# Unlike other resource usage information, current Windows version info is static.
		info = getWinVer()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about obtaining the ssid of the wireless network,
		# and the strength of the network.
		description=_("Announces the system's wireless network ssid name, and its strength."),
		gesture="kb:NVDA+shift+8",
		speakOnDemand=True,
	)
	def script_wlanStatusReport(self, gesture):
		info = self._getWlanInfo()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

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
						"Connected wireless network: {}. Signal strength: {}%. Security type: {}"
					).format(
						n.dot11Ssid.SSID.decode(),
						n.wlanSignalQuality,
						SECURITY_TYPE.get(n.dot11DefaultAuthAlgorithm),
					)
					break
			wlanapi.WlanFreeMemory(wlan_available_network_list)
		wlanapi.WlanFreeMemory(wlan_ifaces)
		return info

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
		description=_("Announces the system's uptime."),
		gesture="kb:NVDA+shift+7",
		speakOnDemand=True,
	)
	def script_announceUptime(self, gesture):
		try:
			uptime = self.getUptime()
			if scriptHandler.getLastScriptRepeatCount() == 0:
				ui.message(uptime)
			else:
				api.copyToClip(uptime, notify=True)
		except TypeError:
			# Translators: Obtaining uptime failed
			ui.message(_("Failed to get the system's uptime."))

	@scriptHandler.script(
		# Translators: Input help mode message about Internet speed in Resource Monitor
		description=_("Presents the speed of Internet."),
		gesture="KB:NVDA+shift+9",
		speakOnDemand=True,
	)
	def script_announceIngternetSpeed(self, gesture):
		def shorten(bps):
			if bps < 1000:
				return "{} bps".format(bps)
			elif 1000 <= bps < 1000000:
				return "{} Kbps".format(round(bps/1000,2))
			elif bps >= 1000000:
				return "{} Mbps".format(round(bps/1000000,2))
		info = _(
"""Download: {download},
upload: {upload},
Maximum download: {maxdownload},
maximum upload: {maxupload},
average download: {avdownload},
average upload: {avupload}."""
		).format(
			download = shorten(self.internetSpeedMonitor.download),
			upload = shorten(self.internetSpeedMonitor.upload),
			maxdownload = shorten(self.internetSpeedMonitor.maxDownload),
			maxupload = shorten(self.internetSpeedMonitor.maxUpload),
			avdownload = shorten(self.internetSpeedMonitor.averageDownload),
			avupload = shorten(self.internetSpeedMonitor.averageUpload)
		)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about overall system resource info command in Resource Monitor
		description=_("Presents used ram, average processor load, and battery info if available."),
		gesture="KB:NVDA+shift+e",
		speakOnDemand=True,
	)
	def script_announceResourceSummary(self, gesture):
		# Faster to build info on the fly rather than keep appending to a string.
		# Translators: presents the overall summary of resource usage, such as CPU load and RAM usage.
		info = [
			_("{ramPercent}% RAM used, CPU at {cpuPercent}%.").format(
				ramPercent=tryTrunk(psutil.virtual_memory()[2]), cpuPercent=tryTrunk(psutil.cpu_percent())
			)
		]
		batteryInfo = _batteryInfo()
		if batteryInfo is not None:
			info.append(batteryInfo)
		ui.message(" ".join(info))
