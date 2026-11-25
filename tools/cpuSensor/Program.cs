// Resource Monitor CPU sensor bridge. GPL-2.0-or-later.
// Sensor access is provided by the unmodified LibreHardwareMonitor library (MPL-2.0).
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.IO.Pipes;
using System.Runtime.InteropServices;
using System.Security.AccessControl;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;
using System.Web.Script.Serialization;
using Microsoft.Win32.SafeHandles;
using LibreHardwareMonitor.Hardware;

internal static class Program
{
    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern SafeFileHandle CreateFile(string name, uint access, uint share,
        IntPtr security, uint creation, uint flags, IntPtr template);

    private static int Main(string[] args)
    {
        Console.OutputEncoding = new UTF8Encoding(false);
        try
        {
            if (args.Length == 2 && (args[0] == "--read" || args[0] == "--stop"))
                return Request(args[1], args[0] == "--stop" ? "stop" : "read");
            int parentId;
            if (args.Length == 3 && args[0] == "--serve" && int.TryParse(args[1], out parentId))
                return Serve(parentId, args[2]);
            Write(new { version = 1, status = "invalidArguments", sensors = new object[0] });
            return 1;
        }
        catch (Exception error)
        {
            Console.Error.WriteLine(error.ToString());
            Write(new { version = 1, status = "unavailable", sensors = new object[0] });
            return 1;
        }
    }

    private static bool IsAdministrator()
    {
        return new WindowsPrincipal(WindowsIdentity.GetCurrent())
            .IsInRole(WindowsBuiltInRole.Administrator);
    }

    private static int Request(string pipeName, string command)
    {
        using (var pipe = new NamedPipeClientStream(".", pipeName, PipeDirection.InOut))
        {
            pipe.Connect(command == "stop" ? 500 : 10000);
            using (var writer = new StreamWriter(pipe, new UTF8Encoding(false), 1024, true))
            using (var reader = new StreamReader(pipe, Encoding.UTF8, false, 1024, true))
            {
                writer.AutoFlush = true;
                writer.WriteLine(command);
                string response = reader.ReadLine();
                if (response == null || response.Length > 65536)
                    return 1;
                Console.WriteLine(response);
            }
        }
        return 0;
    }

    private static int Serve(int parentId, string pipeName)
    {
        if (!IsAdministrator())
            throw new UnauthorizedAccessException("The sensor host requires administrator access.");
        if (!pipeName.StartsWith("ResourceMonitor.CpuSensor.", StringComparison.Ordinal)
            || pipeName.Length > 100 || pipeName.IndexOf('\\') >= 0 || pipeName.IndexOf('/') >= 0)
            throw new ArgumentException("Invalid pipe name.");
        using (Process parent = Process.GetProcessById(parentId))
        {
            if (parent.SessionId != Process.GetCurrentProcess().SessionId)
                throw new ArgumentException("Parent must be in the same session.");
            var security = new PipeSecurity();
            security.SetAccessRuleProtection(true, false);
            security.AddAccessRule(new PipeAccessRule(WindowsIdentity.GetCurrent().User,
                PipeAccessRights.FullControl, AccessControlType.Allow));
            while (!parent.HasExited)
            {
                using (var pipe = new NamedPipeServerStream(pipeName, PipeDirection.InOut, 1,
                    PipeTransmissionMode.Byte, PipeOptions.Asynchronous, 4096, 4096, security))
                {
                    Task connection = pipe.WaitForConnectionAsync();
                    while (!connection.Wait(500))
                    {
                        if (parent.HasExited)
                            return 0;
                    }
                    using (var reader = new StreamReader(pipe, Encoding.UTF8, false, 1024, true))
                    using (var writer = new StreamWriter(pipe, new UTF8Encoding(false), 1024, true))
                    {
                        Task<string> request = reader.ReadLineAsync();
                        if (!request.Wait(3000))
                            continue;
                        bool stop = request.Result == "stop";
                        string result = stop ? "{\"version\":1,\"status\":\"stopped\"}"
                            : request.Result == "read" ? Collect()
                            : "{\"version\":1,\"status\":\"invalidCommand\"}";
                        try { writer.WriteLine(result); writer.Flush(); }
                        catch (IOException) { /* The requesting NVDA instance may have closed. */ }
                        if (stop)
                            return 0;
                    }
                }
            }
        }
        return 0;
    }

    private static string Collect()
    {
        // A stale uninstall entry does not prove that the kernel driver is available.
        using (SafeFileHandle device = CreateFile(@"\\?\GLOBALROOT\Device\PawnIO",
            0xC0000000, 3, IntPtr.Zero, 3, 0, IntPtr.Zero))
        {
            if (device.IsInvalid)
            {
                int error = Marshal.GetLastWin32Error();
                return Serialize(new { version = 1,
                    status = error == 5 ? "accessDenied" : "driverUnavailable", sensors = new object[0] });
            }
        }
        var computer = new Computer { IsCpuEnabled = true };
        try
        {
            computer.Open();
            var readings = new List<object>();
            foreach (IHardware hardware in computer.Hardware)
            {
                if (hardware.HardwareType == HardwareType.Cpu)
                    ReadTemperatures(hardware, hardware.Name, readings);
            }
            return Serialize(new
            {
                version = 1,
                status = readings.Count > 0 ? "ok" : "noSensors",
                sensors = readings
            });
        }
        catch (UnauthorizedAccessException)
        {
            return Serialize(new { version = 1, status = "accessDenied", sensors = new object[0] });
        }
        catch (Exception error)
        {
            Console.Error.WriteLine(error.ToString());
            return Serialize(new { version = 1, status = "error", sensors = new object[0] });
        }
        finally
        {
            computer.Close();
        }
    }

    private static void ReadTemperatures(IHardware hardware, string cpu, List<object> readings)
    {
        hardware.Update();
        foreach (ISensor sensor in hardware.Sensors)
        {
            if (sensor.SensorType != SensorType.Temperature || !sensor.Value.HasValue)
                continue;
            float value = sensor.Value.Value;
            if (float.IsNaN(value) || float.IsInfinity(value) || value <= 0 || value > 150)
                continue;
            readings.Add(new { cpu = cpu, name = sensor.Name, celsius = value });
        }
        foreach (IHardware child in hardware.SubHardware)
            ReadTemperatures(child, cpu, readings);
    }

    private static void Write(object result)
    {
        Console.WriteLine(Serialize(result));
    }

    private static string Serialize(object result)
    {
        return new JavaScriptSerializer().Serialize(result);
    }
}
