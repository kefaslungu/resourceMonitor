#Resource Monitor for NvDA
#Presents basic info on CPU load, memory and disk usage, as well as battery information.
#Authors: Alex Hall (core mechanics and messages), Joseph Lee (internationalization), Beqa Gozalishvili (updated psutil to 0.6.1, and made needed changes to make code run).

import _winreg
import globalPluginHandler, ui, api, scriptHandler
import sys
import os
impPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(impPath)
import psutil
del sys.path[-1]
import battery
import addonHandler
addonHandler.initTranslation()

# 2013.3 or later: is gesture reassignment possible?
try:
	from baseObject import ScriptableObject # 2013.3 or later.
except: notImplementedError # 2013.2 or earlier.

def toBiggestBytes(n, x=2, useLongNames=False):
	#returns a string where n, rounded to x, is in the largest logical measure possible
	i=0 #counter
	units=[" bytes","kb","mb","gb","tb"]
	longUnits=[" bytes","kilobytes","megabytes","gigabytes","terrabytes"]
	n=float(n)
	while(n>=1024):
		n=n/1024.0
		i=i+1
	res=(str(round(n, x)))
	if useLongNames: return res+" "+longUnits[i]
	else: return res+units[i]

def tryTrunk(n):
	#this method basically removes decimal zeros, so 5/0 will just be 5.
	#If the number ends in anything other than a 0, nothing happens (if the trunkated number is not equal to the decimal).
	if n==int(n): return int(n)
	return n

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: The gestures category for this add-on in input gestures dialog (2013.3 or later).
	scriptCategory = _("Resource Monitor")

	# Translators: Presented when a resource summary is copied to clipboard.
	RMCopyMessage = _("Resource summary copied to clipboard")

	# Two functions will be used for each summary info: the script driver and the message getter as shown below.

	def getBatteryInfo(self):
		info=""
		#returns nothing, but sets vars we can now inspect
		battery.getInfo()
		if battery.noBattery:
			# Translators: Message reported when there is no battery on the system, mostly laptops with battery pack removed and running on AC power.
			info=_("This computer does not have a battery connected.")
		elif not battery.onBattery: 
			# Translators: message presented when AC is connected and battery is charging, also show current battery percentage.
			info=_("{percent}%, battery charging.").format(percent=tryTrunk(battery.percentage))
		elif battery.onBattery: 
			# Translators: message presented when computer is running on battery power, showing percentage remaining and estimated remaining time.
			info=_("{percent}% battery remaining, about {time}.").format(percent=tryTrunk(battery.percentage), time=battery.timeLeft)
			if battery.low:
				# Translators: Message reported when battery level is low.
				info+=_(" Warning: low battery.")
			elif battery.critical:
				# Translators: Message reported when battery level is critical.
				info+=_(" Warning: battery is critically low.")
		return info

	def script_announceBatteryInfo(self, gesture):
		info=self.getBatteryInfo()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			if api.copyToClip(info): ui.message(self.RMCopyMessage)
	# Translators: Input help message about battery info command in Resource Monitor.
	script_announceBatteryInfo.__doc__=_("Presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical.")

	def getDriveInfo(self):
		#goes through all registered drives and gives info on each one
		info=""
		#get all registered drives
		for drive in psutil.disk_partitions():
			try:
				#get info on each one
				driveInfo=psutil.disk_usage(drive[0])
				# Translators: Shows drive letter, type of drive (fixed or removable), used capacity and total capacity of a drive (example: C drive, ntfs; 40 GB of 100 GB used (40%).
				info+=_("{driveName} ({driveType} drive): {usedSpace} of {totalSpace} used {percent}%. ").format(driveName=drive[0], driveType=drive[2], usedSpace=toBiggestBytes(tryTrunk(driveInfo[1])), totalSpace=toBiggestBytes(tryTrunk(driveInfo[0])), percent=tryTrunk(driveInfo[3]))
			except:
				pass
		return info

	def script_announceDriveInfo(self, gesture):
		#goes through all registered drives and gives info on each one
		info= self.getDriveInfo()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			if api.copyToClip(info): ui.message(self.RMCopyMessage)
	# Translators: Input help message about drive info command in Resource Monitor.
	script_announceDriveInfo.__doc__=_("Presents the used and total space of the static and removable drives on this computer.")

	def getProcessorInfo(self):
		cores=psutil.NUM_CPUS #number of cores
		averageLoad=psutil.cpu_percent()
		#lists load for each core
		perCpuLoad=psutil.cpu_percent(percpu=True)
		coreLoad=""
		for i in range(len(perCpuLoad)):
			# Translators: Shows average load of CPU cores (example: core 1, 50%).
			coreLoad+=_("Core {coreNumber}: {corePercent}%. ").format(coreNumber=str(i+1), corePercent=tryTrunk(perCpuLoad[i]))
		# Translators: Shows average load of the processor and the load for each core.
		info=_("Average CPU load {avgLoad}%, {cores}").format(avgLoad=tryTrunk(averageLoad), cores=coreLoad)
		return info

	def script_announceProcessorInfo(self, gesture):
		info= self.getProcessorInfo()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			if api.copyToClip(info): ui.message(self.RMCopyMessage)
	# Translators: Input help mode message about processor info command in Resource Monitor.
	script_announceProcessorInfo.__doc__=_("Presents the average processor load and the load of each core.")

	def getRamInfo(self):
		ram=psutil.phymem_usage()
		# Translators: Shows RAM (physical memory) usage.
		info=_("Physical: {physicalUsed} of {physicalTotal} used ({physicalPercent}%). ").format(physicalUsed=toBiggestBytes(tryTrunk(ram[1])), physicalTotal=toBiggestBytes(tryTrunk(ram[0])), physicalPercent=tryTrunk(ram[3]))
		virtualRam=psutil.virtmem_usage()
		# Translators: Shows virtual memory usage.
		info+=_("Virtual: {virtualUsed} of {virtualTotal} used ({virtualPercent}%).").format(virtualUsed=toBiggestBytes(tryTrunk(virtualRam[1])), virtualTotal=toBiggestBytes(tryTrunk(virtualRam[0])), virtualPercent=tryTrunk(virtualRam[3]))
		return info

	def script_announceRamInfo(self, gesture):
		info=self.getRamInfo()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			if api.copyToClip(info): ui.message(self.RMCopyMessage)
	# Translators: Input help mode message about memory info command in Resource Monitor.
	script_announceRamInfo.__doc__=_("Presents the used and total space for both physical and virtual ram.")

	def getWinVer(self):
		# Obtain winversion. Python's Platform module provides below functionality, but platform module is not available for NVDA.
		# Prepare to receive various components for Windows info output.
		winMajor, winMinor, winverName, sp, server, is64Bit, x64 = sys.getwindowsversion().major, sys.getwindowsversion().minor, "", sys.getwindowsversion().service_pack, sys.getwindowsversion().product_type, os.environ.get("PROCESSOR_ARCHITEW6432") == "AMD64", ""
		# Determine Windows version.
		if winMajor == 5: # XP (5.1) or Server 2003 (5.2).
			if winMinor == 1: winverName = "Windows XP" # Since most XP systems use 32-bit editions.
			elif winMinor == 2: winverName = "Windows Server 2003"
		elif winMajor == 6: # Vista/Server 2008 (6.0), 7/2008 R2 (6.1), 8/2012 (6.2), 8.1/2012 R2 (6.3).
			if winMinor == 0: winverName = "Windows Vista" if server == 1 else "Windows Server 2008" # Vista.
			elif winMinor == 1: winverName = "Windows 7" if server == 1 else "Windows Server 2008 R2" # Windows 7
			elif winMinor == 2: winverName = "Windows 8" if server == 1 else "Windows Server 2012" # Windows 8.
			elif winMinor == 3: winverName = "Windows 8.1" if server == 1 else "Windows Server 2012 R2" # Windows 8.1.
		elif winMajor == 10: # Windows 10/Server 2015 (10.0).
			if winMinor == 0:
				# Remove this once WinTen is officially released unless MS decides to update build numbers during automatic updates.
				winverName = "Windows 10 Technical Preview" if server == 1 else "Windows Server 10 Preview"
				buildNum = sys.getwindowsversion().build
		# Translators: Presented under 64-bit Windows.
		if is64Bit: x64 = _("64-bit")
		# Translators: Presented under 32-bit Windows.
		else: x64 = _("32-bit")
		# Translators: Presents Windows version (example output: "Windows version: Windows XP (32-bit)").
		if not sp: info = _("Windows version: {winVersion} ({cpuBit})").format(winVersion = winverName, cpuBit = x64)
		# Translators: Presents Windows version and service pack level (example output: "Windows version: Windows 7 service pack 1 (64-bit)").
		else: info = _("Windows version: {winVersion} {servicePackLevel} ({cpuBit})").format(winVersion = winverName, servicePackLevel = sp, cpuBit = x64)
		if (winMajor, winMinor) == (10, 0): info = info + " build {build}".format(build = buildNum)
		return info

	def script_announceWinVer(self, gesture):
		info = self.getWinVer()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(info)
		else:
			if api.copyToClip(info): ui.message(self.RMCopyMessage)
	# Translators: Input help mode message about Windows version command in Resource Monitor.
	script_announceWinVer.__doc__=_("Announces the version of Windows you are using.")

	def script_announceResourceSummary(self, gesture):
		cpuLoad=psutil.cpu_percent()
		ram=psutil.phymem_usage()
		freeRam=ram[3]
		# Translators: presents the overall summary of resource usage, such as CPU load and RAM usage.
		info=(_("{ramPercent}% RAM used, CPU at {cpuPercent}%. ").format(ramPercent=tryTrunk(freeRam), cpuPercent=tryTrunk(cpuLoad)))
		battery.getInfo()
		if not battery.noBattery and not battery.batteryStatusUnknown and not battery.onBatteryUnknown:
			if not battery.onBattery: info+=_("{percent}%, battery charging.").format(percent=tryTrunk(battery.percentage))
			elif battery.onBattery:
				#discharging battery, so provide info on it
				info+=_("{percent}% battery remaining, about {time}.").format(percent=tryTrunk(battery.percentage), time=battery.timeLeft)
				if battery.low:
					info+=_(" Warning: low battery.")
				elif battery.critical:
					# Translators: In addition to processor and memory usage, presented when battery is low.
					info+=_(" Warning: critically low battery.")
		ui.message(info)
	# Translators: Input help mode message about overall system resource info command in Resource Monitor
	script_announceResourceSummary.__doc__=_("Presents used ram, average processor load, and battery info if available.")

	__gestures={
		"KB:NVDA+shift+e":"announceResourceSummary",
		"KB:NVDA+shift+1":"announceProcessorInfo",
		"KB:NVDA+shift+2":"announceRamInfo",
		"KB:NVDA+shift+3":"announceDriveInfo",
		"KB:NVDA+shift+4":"announceBatteryInfo",
		"KB:NVDA+shift+5":"announceRamInfo",
		"KB:NVDA+shift+6":"announceWinVer",
	}
