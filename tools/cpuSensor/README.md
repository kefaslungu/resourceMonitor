# CPU temperature component

Build with `powershell -File tools/cpuSensor/Build-Sensor.ps1` on Windows x64.
The script downloads and verifies LibreHardwareMonitor 0.9.6, copies its libraries
and notices, and compiles our bridge with Windows' .NET Framework C# compiler.
The generated `sensors/` directory is included in the NVDA add-on archive.
No separate LibreHardwareMonitor application or .NET SDK is required at runtime.

The bundled component currently supports Windows x64; ARM64 is not implemented.
PawnIO's signed driver must already be installed and working. A registry uninstall
entry alone is insufficient. The bridge does not install drivers or change device
permissions. Never enable the unrestricted/unsigned driver edition for this feature.

The first optional CPU temperature report requests Windows UAC approval for the bundled host only.
The host accepts `read` and `stop` commands over a random, user-restricted named
pipe. It does not accept executable paths, arbitrary hardware commands, or output
file paths. NVDA stays unelevated. The host stops on add-on reload or NVDA exit.
Only the CPU sensor group is opened. A failed/zero reading is not a temperature.

Test the generated component with:

```powershell
./tools/cpuSensor/Test-Sensor.ps1 -HelperPath ./addon/globalPlugins/resourceMonitor/sensors/ResourceMonitor.CpuSensor.exe
```

The test requests elevation and prints the hardware result as JSON. An `ok`
response must still be compared against the same sensor in an independent monitor
before declaring hardware validation complete. `driverUnavailable` means the
kernel device could not be opened, even if installation metadata exists.

Third-party source: https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/tree/v0.9.6
The unmodified sensor library uses MPL-2.0. Its license and third-party notices
are distributed alongside the generated helper. Our bridge source is GPL-2.0-or-later.
