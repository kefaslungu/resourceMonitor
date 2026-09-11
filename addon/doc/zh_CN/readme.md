# 资源监控器

* 作者: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst 和其他NVDA贡献者

该插件可读出 CPU 负载，内存使用情况和其他资源使用信息。

## 快捷键

所有命令都支持手动朗读模式。

* NVDA+Shift+E：进入资源监控器命令层。

以下层命令可用于获取各个资源的单独使用情况信息：

* 空格：整体资源使用情况信息，包括物理内存的使用率和CPU 平均负载。
* C：CPU（平均处理器负载，如果是多核 CPU，还包括每个核心的负载）
* D：磁盘（固定（内置）、可移动和网络驱动器的已用空间及总空间）
* G（在安全模式下不可用）：图形处理器（GPU）信息
* Shift+G（在安全模式下不可用）：GPU 内存使用情况
* M：内存（物理内存和虚拟内存的已用空间及总空间）
* O：操作系统（Windows 版本、CPU 体系结构以及精确的内部版本号（build.revision））
* U：系统运行时间
* W：Wi-Fi（网络名称（SSID）、信号强度、安全类型，如果没有可用网络则提示无 SSID）

资源命令层会保持激活状态，以便重复执行。按 Esc 键退出命令层；未映射的按键将退出命令层并传递给当前活动的应用程序。

为提供有限的向后兼容性，此前的 NVDA+Shift+1 至 NVDA+Shift+7 资源快捷键仍然可用：

* NVDA+Shift+1：CPU
* NVDA+Shift+2/5：内存（当 NVDA+Shift+2 这一组合键无法执行时，可使用 NVDA+Shift+5 作为替代）
* NVDA+Shift+3：磁盘
* NVDA+Shift+4：Wi-Fi
* NVDA+Shift+6：操作系统
* NVDA+Shift+7：系统运行时间

您可通过按键与手势对话框更改这些快捷键。

## 使用说明

此插件不替换 Windows 的任务管理器和其他系统信息程序。另请注意以下事项：

* Pressing resource commands twice will copy resource usage information to the clipboard.
* 在安全界面运行插件时，无法将资源信息复制到剪贴板。
* 给出的 CPU 使用情况是针对逻辑处理器而非物理核心。这对于使用超线程的处理器来说是显而易见的，其中 CPU 数量通常是 CPU 核心数量的两倍。在一些较新的计算机上，并非所有 CPU 核心都启用了超线程。
* 如果存在大量磁盘活动，例如复制大文件或查找网络驱动器，则在获取磁盘使用情况信息时可能会出现延迟。
* GPU 信息仅适用于英伟达 GPU。
* 读出 Windows 版本时给出的处理器架构信息中的“AMD64”是指 64 位（x64）的 Intel 和 AMD 处理器。此信息并非指当前使用的实际处理器名称。
* 不支持在 Windows 10/11 LTSC 上安装本插件。

有关每个插件版本之间的所做更改，请参阅[插件更新日志（英语）][1]文档。

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
