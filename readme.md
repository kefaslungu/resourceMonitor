# Resource Monitor

## CPU temperature

Two separate processor commands are available in NVDA's Input Gestures dialog:
processor information reports average load and logical processor loads; processor
load and temperature reports average load and CPU package temperature. Assign a
shortcut to either or both according to your preference. Both are unassigned by default.
The first request asks for Windows administrator approval for the bundled sensor
host. NVDA itself stays unelevated. The signed PawnIO driver must be available;
its official installer is included under `globalPlugins/resourceMonitor/sensors/`.
Driver installation is an explicit setup step, never performed silently on NVDA startup.
The CPU/GPU temperature unit setting applies to both sensors. Invalid or missing
readings are announced as unavailable. Secure screens do not start the sensor host.

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Commands and Input Gestures

All commands support speech on demand mode.

Commands have no default shortcuts or fixed command layer. Open NVDA menu >
Preferences > Input Gestures > Resource Monitor, select a command, and add the
gesture you want. Existing user-defined bindings for resource commands are kept.

Available commands:

* Overall resource usage: used RAM and average CPU load.
* Processor information: average CPU load and logical processor loads.
* Processor load and temperature: average CPU load and CPU package temperature (unavailable in secure mode).
* Memory: used and total physical and virtual RAM.
* Disks: used and total space of fixed, removable and network drives.
* GPU information: GPU load and temperature (unavailable in secure mode).
* GPU memory: used and total GPU memory (unavailable in secure mode).
* Wi-fi: network name, signal strength and security type.
* Operating system: Windows version, architecture and build number.
* System uptime.

## Usage notes

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* Pressing resource commands twice will copy resource usage information to the clipboard.
* Resource information cannot be copied to the clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors with Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* If there is heavy disk activity such as copying large files or while locating network drives, there might be delays when obtaining disk usage information.
* NVDA will play a sound and report a message whenever connecting to or disconnecting from wireless networks. See the next section on how to change this behavior.
* GPU information is given for Nvidia GPU's.
* When announcing processor architecture information as part of Windows version reporting, "AMD64" refer to 64-bit (x64) Intel and AMD processors. This information does not refer to the name of the actual processor in use.
* Installing the add-on on Windows 10/11 LTSC is not supported.

## Settings

You can configure the following resource usage reporting options from NVDA settings screen under Resource Monitor category:

* CPU/GPU temperature unit: Select Celsius or Fahrenheit for CPU and GPU temperatures.
* Wi-fi connect/disconnect notification: Select how NVDA should report wi-fi connect/disconnect notifications (off, message, sound, both message and sound).
* Memory and disk size notation: select how memory sizes for RAM and disk usage units such as gigabytes and terabytes are reported (default is the alternative method (KB/MB/...).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md

## Building and testing

On Windows x64, run `uv sync --only-group build --python 3.13`, followed by
`powershell -File tools/Build-Addon.ps1`. The package is written to `dist/`.
Then run `.venv/Scripts/python.exe -m unittest discover -s tests -v`.
The reporting tests use the compiled Turkish catalog produced by the build.
See `tools/cpuSensor/README.md` for component dependencies and hardware validation.
