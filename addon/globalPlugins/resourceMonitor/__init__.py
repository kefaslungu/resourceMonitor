# Resource Monitor for NVDA
# Presents basic info on CPU load, memory and disk usage, as well as battery information.
# Copyright 2013-2021 Alex Hall, Joseph Lee, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst,
# released under GPL.
# This add-on uses Psutil, licensed under 3-Clause BSD License which is compatible with GPL.

import winreg
from datetime import datetime
import sys
import os
import functools
import globalPluginHandler
import ui
import api
import scriptHandler
from . import psutil
import addonHandler
addonHandler.initTranslation()

# Styles of size calculation/string composition, do not change!
# Treditional style, Y, K, M, G, B, ...
traditional = [
	(1024.0**8.0, 'Y'),
	(1024.0**7.0, 'Z'),
	(1024.0**6.0, 'E'),
	(1024.0**5.0, 'P'),
	(1024.0**4.0, 'T'),
	(1024.0**3.0, 'G'),
	(1024.0**2.0, 'M'),
	(1024.0**1.0, 'K'),
	(1024.0**0.0, 'B'),
]

# Alternative style (displayed with most PCs): MB, KB, GB, YB, ZB, ...
alternative = [
	(1024.0**8.0, ' YB'),
	(1024.0**7.0, ' ZB'),
	(1024.0**6.0, ' EB'),
	(1024.0**5.0, ' PB'),
	(1024.0**4.0, ' TB'),
	(1024.0**3.0, ' GB'),
	(1024.0**2.0, ' MB'),
	(1024.0**1.0, ' KB'),
	(1024.0**0.0, (' byte', ' bytes')),
]

# Verbose style: Kilobytes, Megabytes, Gigabytes, ...
verbose = [
	(1024.0**8.0, ' yottabytes'),
	(1024.0**7.0, ' zettabytes'),
	(1024.0**6.0, ' exabytes'),
	(1024.0**5.0, (' petabyte', ' petabytes')),
	(1024.0**4.0, (' terabyte', ' terabytes')),
	(1024.0**3.0, (' gigabyte', ' gigabytes')),
	(1024.0**2.0, (' megabyte', ' megabytes')),
	(1024.0**1.0, (' kilobyte', ' kilobytes')),
	(1024.0**0.0, (' byte', ' bytes')),
]

# International Electrotechnical Commission (IEC) style: Ki, Mi, Gi, Ti, ...
iec = [
	(1024.0**8.0, 'Yi'),
	(1024.0**7.0, 'Zi'),
	(1024.0**6.0, 'Ei'),
	(1024.0**5.0, 'Pi'),
	(1024.0**4.0, 'Ti'),
	(1024.0**3.0, 'Gi'),
	(1024.0**2, 'Mi'),
	(1024.0**1.0, 'Ki'),
	(1024.0**0.0, ''),
]

# International System of Units (Si) style: each unit is 1000 of another (i.e. 1000 KB is 1 MB)
si = [
	(1000.0**8.0, 'Y'),
	(1000.0**7.0, 'Z'),
	(1000.0**6.0, 'E'),
	(1000.0**5.0, 'P'),
	(1000.0**4.0, 'T'),
	(1000.0**3.0, 'G'),
	(1000.0**2.0, 'M'),
	(1000.0**1.0, 'K'),
	(1000.0**0.0, 'B'),
]


def size(bytes, system=traditional):
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


def tryTrunk(n):
	# This method basically removes decimal zeros, so 5.0 will just be 5.
	# If the number ends in anything other than a 0,
	# nothing happens (if the trunkated number is not equal to the decimal).
	if n == int(n):
		return int(n)
	return n


# Moved from battery module to the main module in 2019 (code provided by Alex Hall)
def _batteryInfo(verbose=False):
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
			if secsleft == 0xffffffff:
				# Translators: message presented when computer is running on battery power,
				# showing percentage remaining yet battery time is unknown.
				info = _("{percent}% battery remaining, battery time unknown.").format(percent=tryTrunk(percent))
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
						_("1 hour")
						# Translators: battery and system uptime in hours.
						if hours == 1 else _("{0} hours").format(hours)
					)
				# Translators: battery and system uptime in minutes.
				timeLeft.append(
					# Translators: battery and system uptime in minutes.
					_("1 minute")
					# Translators: battery and system uptime in minutes.
					if minutes == 1 else _("{0} minutes").format(minutes)
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


# Record Windows Server 10 builds to release ID's.
# Client versions will be checked via Registry.
server10LTSBuilds = {
	14393: "Windows Server 2016",
	17763: "Windows Server 2019",
}


def _winRID(buildNum, isClient):
	# Special cases: Windows 10 Version 1507, Windows Server long-term servicing channel (LTSC) releases.
	if isClient and buildNum == 10240:
		return "Windows 10 1507"
	elif not isClient and buildNum in server10LTSBuilds:
		return server10LTSBuilds[buildNum]
	# Since late 2019 (and confirmed with Server vNext build 20201),
	# "rs_prerelease" branch designates dev channel build.
	# Note that in some cases Insider Preview builds may come from what may appear to be
	# feature update branch such as mn_release for 20H2 Azure release.
	# If self-host IsRetailOS flag is present (an integer), it is an Insider Preview.
	# Because NVDA is a 32-bit application, 64-bit view of Registry must be attempted for self-host key.
	if os.environ.get("PROCESSOR_ARCHITEW6432") in ("AMD64", "ARM64"):
		selfHostApplicability = winreg.OpenKeyEx(
			winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\WindowsSelfHost\Applicability",
			access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY
		)
	else:
		selfHostApplicability = winreg.OpenKeyEx(
			winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\WindowsSelfHost\Applicability"
		)
	try:
		isRetailOS = winreg.QueryValueEx(selfHostApplicability, "IsRetailOS")[0]
	except OSError:
		isRetailOS = 1
	winreg.CloseKey(selfHostApplicability)
	with winreg.OpenKey(
		winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion"
	) as currentVersion:
		try:
			buildBranch = winreg.QueryValueEx(currentVersion, "BuildBranch")[0]
		except OSError:
			buildBranch = None
		if isRetailOS:
			isRetailOS = buildBranch and not buildBranch.startswith("rs_prerelease")
		# Version 20H2/2009 and later where a separate display version string is used.
		# For backward compatibility, release ID variable will store display version string.
		try:
			releaseID = winreg.QueryValueEx(currentVersion, "DisplayVersion")[0]
		except OSError:
			releaseID = None
		# Version 1511 and later unless display version string is present.
		if not releaseID:
			try:
				releaseID = winreg.QueryValueEx(currentVersion, "ReleaseID")[0]
			except OSError:
				releaseID = "Unknown"
	# Insider Preview builds.
	if not isRetailOS:
		return "Windows Insider" if isClient else "Windows Server Insider"
	if isClient:
		if buildNum < 22000:
			return "Windows 10 {0}".format(releaseID)
		else:
			return "Windows 11 {0}".format(releaseID)
	else:
		return "Windows Server {0}".format(releaseID)


@functools.lru_cache(maxsize=128)
def getWinVer():
	# Obtain winversion.
	# Python's Platform module provides below functionality,
	# but platform module is not available for NVDA.
	# Prepare to receive various components for Windows info output.
	winMajor, winMinor = sys.getwindowsversion().major, sys.getwindowsversion().minor
	buildNum = sys.getwindowsversion().build
	sp, server = sys.getwindowsversion().service_pack, sys.getwindowsversion().product_type
	arch64 = os.environ.get("PROCESSOR_ARCHITEW6432")
	# Determine Windows version.
	if winMajor == 6:  # 7/2008 R2 (6.1), 8/2012 (6.2), 8.1/2012 R2 (6.3).
		if winMinor == 1:  # Windows 7
			winverName = "Windows 7" if server == 1 else "Windows Server 2008 R2"
		elif winMinor == 2:  # Windows 8.
			winverName = "Windows 8" if server == 1 else "Windows Server 2012"
		elif winMinor == 3:  # Windows 8.1.
			winverName = "Windows 8.1" if server == 1 else "Windows Server 2012 R2"
	elif winMajor == 10:  # Windows 10/Server 2016 (10.0) and beyond.
		# Also take care of release ID, introduced in Version 1511
		# as well as Windows 11 (2021).
		winverName = _winRID(buildNum, server == 1)
	if arch64 in ("AMD64", "ARM64"):
		x64 = "x64" if arch64 == "AMD64" else arch64
	else:
		x64 = "32-bit"
	# Announce build.revision on Windows 8.1/Server 2012 R2 and later.
	buildRevision = None
	if (winMajor, winMinor) >= (6, 3):
		# Just like retail OS check for Insider Preview builds, 64-bit systems require a different access token.
		if arch64:
			currentVersion = winreg.OpenKey(
				winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion",
				access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY
			)
		else:
			currentVersion = winreg.OpenKey(
				winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion"
			)
		ubr = winreg.QueryValueEx(currentVersion, "UBR")[0]  # UBR = Update Build Revision
		winreg.CloseKey(currentVersion)
		buildRevision = f"{buildNum}.{ubr}"
	if not sp:
		# Translators: Presents Windows version
		# (example output: "Windows 8.1 (32-bit)").
		info = _("{winVersion} ({cpuBit})").format(
			winVersion=winverName, cpuBit=x64
		)
	else:
		# Translators: Presents Windows version and service pack level
		# (example output: "Windows 7 service pack 1 (64-bit)").
		info = _("{winVersion} {servicePackLevel} ({cpuBit})").format(
			winVersion=winverName, servicePackLevel=sp, cpuBit=x64
		)
	if buildRevision is not None:
		info += " build {build}".format(build=buildRevision)
	return info


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: The gestures category for this add-on in input gestures dialog (2013.3 or later).
	scriptCategory = _("Resource Monitor")

	@scriptHandler.script(
		description=_(
			# Translators: Input help message about battery info command in Resource Monitor.
			"Presents battery percentage, charging status, remaining time (if not charging), "
			"and a warning if the battery is low or critical."
		),
		gesture="KB:NVDA+shift+4"
	)
	def script_announceBatteryInfo(self, gesture):
		info = _batteryInfo(verbose=True)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help message about drive info command in Resource Monitor.
		description=_("Presents the used and total space of the static and removable drives on this computer."),
		gesture="KB:NVDA+shift+3"
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
						percent=tryTrunk(driveInfo[3])
					)
				)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(" ".join(info))
		else:
			api.copyToClip(" ".join(info), notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about processor info command in Resource Monitor.
		description=_("Presents the average processor load and the load of each core."),
		gesture="KB:NVDA+shift+1"
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
		# Translators: Shows average load of the processor and the load for each core.
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
		gestures=["KB:NVDA+shift+2", "KB:NVDA+shift+5"]
	)
	def script_announceRamInfo(self, gesture):
		ram = psutil.virtual_memory()
		# Translators: Shows RAM (physical memory) usage.
		info = _("Physical: {physicalUsed} of {physicalTotal} used ({physicalPercent}%). ").format(
			physicalUsed=size(ram[3], alternative),
			physicalTotal=size(ram[0], alternative),
			physicalPercent=tryTrunk(ram[2])
		)
		virtualRam = psutil.swap_memory()
		# Translators: Shows virtual memory usage.
		info += _("Virtual: {virtualUsed} of {virtualTotal} used ({virtualPercent}%).").format(
			virtualUsed=size(virtualRam[1], alternative),
			virtualTotal=size(virtualRam[0], alternative),
			virtualPercent=tryTrunk(virtualRam[3])
		)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	@scriptHandler.script(
		# Translators: Input help mode message about Windows version command in Resource Monitor.
		description=_("Announces the version of Windows you are using."),
		gesture="KB:NVDA+shift+6"
	)
	def script_announceWinVer(self, gesture):
		# Unlike other resource usage information, current Windows version info is static.
		info = getWinVer()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			api.copyToClip(info, notify=True)

	def getUptime(self):
		bootTimestamp = psutil.boot_time()
		if bootTimestamp == 0.0:
			raise TypeError
		uptime = datetime.now() - datetime.fromtimestamp(bootTimestamp)
		hours, remainingMinutes = divmod(uptime.seconds, 3600)
		minutes, seconds = divmod(remainingMinutes, 60)
		uptimeComponents = []
		uptimeComponents.append(
			# Translators: system uptime in days.
			_("1 day")
			# Translators: system uptime in days.
			if uptime.days == 1 else _("{0} days").format(uptime.days)
		)
		# Translators: system uptime in hours.
		uptimeComponents.append(
			# Translators: system uptime in hours.
			_("1 hour")
			# Translators: system uptime in hours.
			if hours == 1 else _("{0} hours").format(hours)
		)
		uptimeComponents.append(
			# Translators: system uptime in minutes.
			_("1 minute")
			# Translators: system uptime in minutes.
			if minutes == 1 else _("{0} minutes").format(minutes)
		)
		# Translators: system uptime in seconds.
		uptimeComponents.append(
			# Translators: system uptime in seconds.
			_("1 second")
			# Translators: system uptime in seconds.
			if seconds == 1 else _("{0} seconds").format(seconds)
		)
		return ", ".join(uptimeComponents)

	@scriptHandler.script(
		# Translators: Input help mode message about obtaining the system's uptime
		description=_("Announces the system's uptime."),
		gesture="kb:NVDA+shift+7"
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
		# Translators: Input help mode message about overall system resource info command in Resource Monitor
		description=_("Presents used ram, average processor load, and battery info if available."),
		gesture="KB:NVDA+shift+e"
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
