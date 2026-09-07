# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Shortcuts

All commands support speech on demand mode.

* NVDA+Shift+E: enters the Resource Monitor command layer.
* In the command layer, press Space for overall resource usage, C for CPU load, M for memory usage, D for disk usage, W for wireless status, O for Windows version, U for uptime, G for GPU usage, or Shift+G for GPU memory usage.
* Resource commands keep the layer active so they can be repeated. Press Escape to exit the layer; an unmapped key exits and is passed through.
* For limited backward compatibility, the previous NVDA+Shift+1 through NVDA+Shift+7 resource shortcuts remain available.

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
