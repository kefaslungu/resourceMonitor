# 资源监控器

* 作者: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst 和其他NVDA贡献者

该插件可读出 CPU 负载，内存使用情况和其他资源使用信息。

## 快捷键

所有命令都支持手动朗读模式。

* NVDA+Shift+E：读出物理内存使用率和 CPU 平均负载。
* NVDA+Shift+1： 读出每个 CPU 核心的负载和平均负载。
* NVDA+Shift+2/5： 读出物理内存和虚拟内存的容量和使用情况（当 NVDA+Shift+2 无法执行时，可使用 NVDA+Shift+5 代替）。
* NVDA+Shift+3: presents the used and total space of the fixed (built-in), removable, and network drives.
* NVDA+Shift+4：读出有关无线连接、SSID 名称和强度的信息，如果没有可用的 SSID，则给出提示。
* NVDA+Shift+6：读出 Windows 版本、CPU 架构以及精确的内部版本号（build.revision）。
* NVDA+Shift+7： 读出当前系统的运行时间。
* 未分配：读出有关图形处理单元（GPU）的信息；该功能在安全模式下不可用。
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

您可以通过按键与手势对话框更改这些快捷键。

## 使用说明

此插件不替换 Windows 的任务管理器和其他系统信息程序。另请注意以下事项：

* 除总体资源使用情况命令（NVDA+Shift+E）外，连按其他命令两次可将资源使用信息复制到剪贴板。
* 在安全界面运行插件时，无法将资源信息复制到剪贴板。
* 给出的 CPU 使用情况是针对逻辑处理器而非物理核心。这对于使用超线程的处理器来说是显而易见的，其中 CPU 数量是 CPU 核心数量的两倍。在一些较新的计算机上，并非所有 CPU 核心都启用了超线程。
* If there is heavy disk activity such as copying large files or while locating network drives, there might be delays when obtaining disk usage information.
* GPU information is given for Nvidia GPU's.
* 所读出的处理器架构信息“x86”和“AMD64”分别指代的是 32 位和 64 位 (x64) Intel 和 AMD 处理器。
* 不支持在 Windows 10/11 LTSC 上安装本插件。

有关每个插件版本之间的所做更改，请参阅[插件更新日志（英语）][1]文档。

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
