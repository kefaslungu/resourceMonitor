#Resource Monitor for NvDA
#Presents basic info on CPU load, memory and disk usage, as well as battery information.
#Authors: Alex Hall (core mechanics and messages), Joseph Lee (internationalization).

import globalPluginHandler, ui
import psutil, battery
import addonHandler
addonHandler.initTranslation()


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

 def script_announceBatteryInfo(self, gesture):
  info=""
  battery.getInfo() #returns nothing, but sets vars we can now inspect
  if battery.noBattery: info=_("This computer does not have a battery connected.")
  elif not battery.onBattery: info=_("%s%%, battery is charging.") %(tryTrunk(battery.percentage))
  elif battery.onBattery: #discharging battery, so provide info on it
   info=_("%s%% (about %s) battery remaining. ") %(tryTrunk(battery.percentage), battery.timeLeft)
   if battery.low:
    info+=_(" Battery is low")
   elif battery.critical:
    info+=_(" Battery is critical")
  ui.message(info)
 script_announceBatteryInfo.__doc__=_("Speaks battery percentage, charging status, time left (if not charging), and a warning if the battery is low or critical.")

 def script_announceDriveInfo(self, gesture):
  #goes through all registered drives and gives info on each one
  info=""
  for drive in psutil.disk_partitions(): #get all registered drives
   driveInfo=psutil.disk_usage(drive[0]) #get info on each one
   #Translators: Shows drive letter, type of drive (fixed or removable), used capacity and total capacity of a drive (example: C, fixed drive; 40 GB of 100 GB used (40%). Note that %s cannot be changed.
   info+=_("%s (%s drive): %s of %s used (%s%%). ") %(drive[0], drive[2], toBiggestBytes(tryTrunk(driveInfo[1])), toBiggestBytes(tryTrunk(driveInfo[0])), tryTrunk(driveInfo[3]))
  ui.message(info)
 script_announceDriveInfo.__doc__=_("Speaks the used and total space of every drive registered on this computer, along with each drive's type (fixed, removeable, or CDROM).")

 def script_announceProcessorInfo(self, gesture):
  cores=psutil.NUM_CPUS #number of cores
  averageLoad=psutil.cpu_percent()
  perCpuLoad=psutil.cpu_percent(percpu=True) #lists load for each core
  coreLoad=""
  # Translators: Shows average load of CPU cores (example: core 1, 50%).
  for i in range(len(perCpuLoad)): coreLoad+="Core %s: %s%%. " %(str(i+1), tryTrunk(perCpuLoad[i]))
  #Translators: Shows average load of the processor (example: 15% average load). The second %s denotes core number.
  info=_("%s%% average CPU load. %s") %(tryTrunk(averageLoad), coreLoad)
  ui.message(info)
 script_announceProcessorInfo.__doc__=_("Speaks the average processor load, then the load of each core.")

 def script_announceRamInfo(self, gesture):
  ram=psutil.phymem_usage()
  # Translators: Shows RAM (physical memory) usage.
  info=_("Physical: %s of %s used (%s%%). ") %(toBiggestBytes(tryTrunk(ram[1])), toBiggestBytes(tryTrunk(ram[0])), tryTrunk(ram[3]))
  virtualRam=psutil.virtmem_usage()
  # Translators: Shows virtual memory usage (first %s is used space, second %s is total capacity, third %s is usage in percentage).
  info+=_("Virtual: %s of %s used (%s%%).") %(toBiggestBytes(tryTrunk(virtualRam[1])), toBiggestBytes(tryTrunk(virtualRam[0])), tryTrunk(virtualRam[3]))
  ui.message(info)
 script_announceRamInfo.__doc__=_("Speaks the used and total space for both physical and virtual ram.")

 def script_announceResourceSummary(self, gesture):
  cpuLoad=psutil.cpu_percent()
  ram=psutil.phymem_usage()
  freeRam=ram[3]
  # Translators: shows the overal summary of resource usage, such as CPU load and RAM usage.
  info=(_("%s%% ram used, CPU at %s%%.") %(tryTrunk(freeRam), tryTrunk(cpuLoad)))
  battery.getInfo()
  if not battery.noBattery and not battery.batteryStatusUnknown and not battery.onBatteryUnknown:
   if not battery.onBattery: info+=_(" Battery is charging, at %s%%.") %(tryTrunk(battery.percentage))
   elif battery.onBattery: #discharging battery, so provide info on it
    info+=_(" %s%% (about %s) battery remaining. ") %(tryTrunk(battery.percentage), battery.timeLeft)
    if battery.low: info+=_(" Battery is low")
    elif battery.critical: info+=_(" Battery is critical")
  ui.message(info)
 script_announceResourceSummary.__doc__=_("Speaks used ram, average processor load, and battery info (if this computer has a battery).")

 __gestures={
  "KB:NVDA+shift+e":"announceResourceSummary",
  "KB:NVDA+shift+1":"announceProcessorInfo",
  "KB:NVDA+shift+2":"announceRamInfo",
  "KB:NVDA+shift+3":"announceDriveInfo",
  "KB:NVDA+shift+4":"announceBatteryInfo",
  "KB:NVDA+shift+5":"announceRamInfo",
 }