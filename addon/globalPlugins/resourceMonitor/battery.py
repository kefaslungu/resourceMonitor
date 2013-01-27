#This is not my work. I found it at this link:
#http://www.python-forum.org/pythonforum/viewtopic.php?f=1&t=8425
#The person who wrote it is a genius, so thanks go to them for making this available.
import ctypes
import ctypes.wintypes

high=low=critical=charging=onBattery=onBatteryUnknown=noBattery=batteryStatusUnknown=False
timeLeft=percentage=BatteryFlag=ACLineStatus=0

class SYSTEM_POWER_STATUS(ctypes.Structure):
 _fields_=[
  ("ACLineStatus", ctypes.c_byte),
  ("BatteryFlag", ctypes.c_byte),
  ("BatteryLifePercent", ctypes.c_byte),
  ("Reserved1", ctypes.c_byte),
  ("BatteryLifeTime", ctypes.wintypes.DWORD),
  ("BatteryFullLiveTime", ctypes.wintypes.DWORD)
 ]

sps=SYSTEM_POWER_STATUS()
ac_constants={
 0:"battery",
 1:"AC",
 255:"unknown"
}
status_constants = {
 1:"high",
 2:"low",
 4:"critical",
 8:"charging",
 128:"no system battery",
 255:"unknown"
}

def getInfo():
 #returns a tuple of (percentage, expected life, charge status, power source, status flag, source flag)
 global high, low, critical, charging, onBattery, onBatteryUnknown, noBattery, batteryStatusUnknown
 global timeLeft, percentage, BatteryFlag, ACLineStatus
 ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(sps))
 hours, rest = divmod(sps.BatteryLifeTime,3600)
 minutes, seconds = divmod(rest, 60)
 timeLeft=""
 if hours>1000000: timeleft="unknown"
 else:
  if hours>0:
   timeLeft+=str(hours)
   if hours==1: timeLeft+=" hour, "
   else: timeLeft+=" hours, "
  timeLeft+=str(minutes)
  if minutes==1: timeLeft+=" minute"
  else: timeLeft+=" minutes"
 percentage=sps.BatteryLifePercent
 ACLineStatus=sps.ACLineStatus%256
 BatteryFlag=sps.BatteryFlag%256
 if ACLineStatus==0: onBattery=True
 elif ACLineStatus==1: onBattery=False
 elif ACLineStatus==255: onBatteryUnknown=True
 if BatteryFlag&1: high=True
 if BatteryFlag&2: low=True
 if BatteryFlag&4: critical=True
 if BatteryFlag&8: charging=True
 if BatteryFlag&128:  noBattery=True
 if BatteryFlag&255: batteryStatusUnknown=True
