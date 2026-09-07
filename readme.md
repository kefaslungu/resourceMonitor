# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Shortcuts

All commands support speech on demand mode.

* NVDA+Shift+E: enters the Resource Monitor command layer.

The following layer commands are available to obtain individual resource usage information:

* Space: overall resource usage information including used RAM (physical memory) and average processor load.
* C: CPU (average processor load and if multicore CPU's are present the load of each core)
* D: disks (used and total space of the fixed (built-in), removable, and network drives)
* G (unavailable in secure mode): graphics processing unit (GPU) information
* Shift+G(unavailable in secure mode): GPU memory usage
* M: memory (used and total space for both physical and virtual RAM (NVDA+Shift+5 is an alternative to NVDA+Shift+2 when the latter keyboard combination cannot be performed))
* O: operating system (Windows version, CPU architecture, and exact build number (build.revision))
* U: system uptime
* W: wi-fi (network name (SSID), signal strength, security mode, or no SSID if there is none available)

Resource commands keep the layer active so they can be repeated. Press Escape to exit the layer; an unmapped key exits and is passed through the active application.

For limited backward compatibility, the previous NVDA+Shift+1 through NVDA+Shift+7 resource shortcuts remain available:

* NVDA+Shift+1: CPU
* NVDA+Shift+2/5: memory
* NVDA+Shift+3: disks
* NVDA+Shift+4: wi-fi
* NVDA+Shift+6: operating system
* NVDA+Shift+7: system uptime

You can change these gestures via the input gestures dialog.

## Usage notes

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* Pressing resource commands twice will copy resource usage information to the clipboard.
* Resource information cannot be copied to the clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors with Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* If there is heavy disk activity such as copying large files or while locating network drives, there might be delays when obtaining disk usage information.
* GPU information is given for Nvidia GPU's.
* When announcing processor architecture information as part of Windows version reporting, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively. This information does not refer to the name of the actual processor in use.
* Installing the add-on on Windows 10/11 LTSC is not supported.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
