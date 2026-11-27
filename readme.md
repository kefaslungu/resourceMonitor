# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Shortcuts

All commands support speech on demand mode.

* NVDA+Shift+E: enters the Resource Monitor command layer. There are two modes:
	* Lock: pressing the layer entry command once will keep the layer mode active until the Escape key or a key not defined in the layer mode (see below) is pressed. Keys not defined in the layer mode will be passed to the application.
	* Report: performing a resource usage info command will announce the information and exit the layer mode. Press the layer entry command repeatedly to lock the layer mode.

The following layer commands are available to obtain individual resource usage information:

* Space: overall resource usage information including used RAM (physical memory) and average processor load.
* C: CPU (average processor load and if multicore CPU's are present the load of each core)
* D: disks (used and total space of the fixed (built-in), removable, and network drives)
* G (unavailable in secure mode): graphics processing unit (GPU) information
* Shift+G(unavailable in secure mode): GPU memory usage
* M: memory (used and total space for both physical and virtual RAM)
* O: operating system (Windows version, CPU architecture, and exact build number (build.revision))
* U: system uptime
* W: wi-fi (network name (SSID), signal strength, security mode, or no SSID if there is none available)

You can also assign shortcuts to announce individual resource information without entering the layer first (go to NvDA menu/Preferences/Input gestures to assign custom commands).

## Usage notes

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* Pressing resource commands twice or Control+NVDA+X will copy resource usage information to the clipboard (pressing Control+NVDA+X copies the last spoken resource information).
* Resource information cannot be copied to the clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors with Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* If there is heavy disk activity such as copying large files or while locating network drives, there might be delays when obtaining disk usage information.
* NVDA will play a sound and report a message whenever connecting to or disconnecting from wireless networks. See the next section on how to change this behavior.
* GPU information is given for Nvidia GPU's.
* When announcing processor architecture information as part of Windows version reporting, "AMD64" refer to 64-bit (x64) Intel and AMD processors. This information does not refer to the name of the actual processor in use.
* Installing the add-on on Windows 10/11 LTSC is not supported.

## Settings

You can configure the following settings from NVDA settings screen under Resource Monitor category:

* Enter resource monitor layer when layer command is performed: select between once (default, lock the layer mode) or repeatedly (pressing once will anounce resource info once, press repeatedly to lock the layer mode).
* GPU temperature unit: Select the temperature unit reported as part of the GPU information (Celcius or Fahrenheit).
* Wi-fi connect/disconnect notification: Select how NVDA should report wi-fi connect/disconnect notifications (off, message, sound, both message and sound).
* Memory and disk size notation: select how memory sizes for RAM and disk usage units such as gigabytes and terabytes are reported (default is the alternative method (KB/MB/...).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
