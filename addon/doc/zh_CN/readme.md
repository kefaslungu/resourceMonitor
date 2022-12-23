# 资源监控器 #

* 作者:Alex Hall，Joseph Lee，beqa gozalishvili，Tuukka Ojala，Ethin
  Probst和其他NVDA贡献者
* 下载 [稳定版][1]
* NVDA compatibility: 2022.3 and later

该插件可读出 CPU 负载，内存使用情况和其他资源使用信息。

# 快捷键

* NVDA+Shift+E： 读出内存的使用率、CPU 平均负载和电池信息（如果可用）。
* NVDA+Shift+1： 读出每个 CPU 核心的负载和平均负载。
* NVDA+Shift+2/5： 读出物理内存和虚拟内存的容量和使用情况。
* NVDA+Shift+3： 读出此计算机上所有驱动器的文件系统和空间使用情况。
* NVDA+Shift+4： 读出电量、充电状态、剩余时间（如果没有充电）且在电量不足时发出警告。
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7： 读出当前系统的运行时间。

You can change these shortcut keys via input gestures dialog.

## 使用说明

此插件不替换 Windows 的任务管理器和其他系统信息程序。另请注意以下事项：

* 如果在安全屏幕中使用该插件，则无法将资源信息复制到剪贴板。
* 为逻辑处理器而不是物理内核提供CPU使用率。对于使用超线程技术的处理器来说，这是显而易见的，其中CPU的数量是CPU核心数量的两倍。
* 如果存在大量磁盘活动（例如复制大文件），则在获取磁盘使用信息时可能会出现延迟。
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

关于许可证的说明：此附加组件使用Psutil，根据与GNU通用公共许可证兼容的3条款BSD许可证进行许可。

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.
* NVDA will announce actual processor architecture (x86/AMD64/ARM64) as part
  of Windows version information.
* On single-core systems, NVDA will no longer announce CPU core load as
  average CPU load is the same as core load.

## 版本 22.03

22.03 版是支持 Windows 7 Service Pack 1、8 和 8.1 的最后一个稳定版。

* 需要 NVDA 2021.3 或更高版本。
* 试图在 Windows 7、8 和 8.1 上安装插件时将显示一条警告消息。
* 将 psutil 更新到 5.9.0。

## 版本 22.01

* 需要 NVDA 2021.2 或更高版本。

## 版本 21.10

* 由于对 NVDA 的更改会影响此插件，因此需要 NVDA 2021.1 或更高版本。

## 版本21.08

* 最低 Windows 版本要求现在与 NVDA 版本相关联。
* Windows 构建 20348 和 22000 分别被确认为 Windows Server 2022 和 Windows 11。
* 在 Insider Preview 版本中，不会使用诸如“Windows 10”之类的 Windows 版本。相反，NvDA 将宣布“Windows
  Insider”。
* 在 64 位系统上，处理器架构（x64 或 ARM64）将作为 Windows 版本信息的一部分公布。

## 版本21.04

* 需要 NVDA 2020.4 或更高版本。
* 将 psutil 更新为5.8.0。
* 当连按两次快捷键将资源信息复制到剪贴板时，NVDA 将读出已复制的资源摘要。

## 版本21.01

* 将 psutil 更新为5.7.3。
* 缩短了 Windows 版本消息。
* 在 Windows 8.1 上，build.revision 将作为 Windows 版本消息的一部分读出，类似于 Windows 10。

## 版本20.09

* 系统正常运行时间现在以天、小时、分钟、秒来呈现。
* Windows Server Insider Preview build 20201或更高版本现在被正确识别为Server Insider
  build。

## 版本20.07

* 在获取Windows版本信息时，正确识别Windows 10版本20H2（NVDA+Shift+6）。
* 简化Windows 10版本信息，即当按NVDA+Shift+6时，Windows 10 YYMM代替Windows 10verYYMM。

## 版本20.06

* 使用 Flake8 解决了许多编码样式问题和潜在错误。

## 版本20.04

* 将psutil更新为5.7.0。

## 版本20.01

* 由于广泛使用Python 3，因此需要NVDA 2019.3或更高版本。

## 版本19.11

* 改进了对Windows Insider Preview版本的检测，尤其是对于20H1及更高版本。

## 版本19.07

* 将 psutil 更新为5.6.3。
* 电池状态通知命令的内部更改。

## 版本18.12

* 支持未来 NVDA 版本的内部更改。

## 版本18.10

* 代码已经与Python 3更兼容。
* 将 psutil 更新为5.4.7。
* 现在，获取磁盘容量和内存使用量时，如果使用计算机或RAM超过1兆字节或磁盘大小的服务，NVDA将不再出错。
* 内存和磁盘使用的值最多显示两位小数（例如4.00 GB而不是4.0 GB）。
* 改进了对Windows Insider Preview构建的检测。

## 版本18.04

版本18.04.x是支持早于7 SP1的Windows版本的最后一个版本。

* 上一版本支持Windows Server 2003，Vista和Server 2008。
* 更好地检测Windows 10版本并区分公共和内部预览版本。

## 版本17.12

* 在Windows 10上添加了对64位ARM处理器的支持。

## 版本17.09

现在：版本17.09.x是支持Windows XP的最后一个版本。

* 上一个版本在Windows XP上运行。
* Windows 10内部版本16278及更高版本被识别为版本1709.一旦发布版本1709稳定版本，将发布此附加组件的次要修订版本。

## 版本17.07.1

* 重新引入对Windows XP的支持（从17.02版开始分解）。

## 版本17.05

* 现在可以报告系统正常运行时间(自上次启动以来的时间; NVDA + Shift + 7）。

## 版本17.02

* 将 psutil 更新为5.0.1。
* 在检查磁盘使用情况时，NVDA将不再在可移动介质未被正确识别的某些系统上出现错误对话框（例如，当卡未插入读卡器时）。）

## 版本16.08

从版本16.08开始，插件版本将显示为year.month.revision。

* 现在可以正确识别Windows 10的各种修订版（例如构建14393的1607）。
* Windows 10构建版本（安装累积更新后）已正确识别（例如14393.51）。
* 如果使用Insider Preview构建，则会认识到这一事实。

## 版本4.5

* 附加存储库已移至GitHub（可在https://github.com/josephsl/resourcemonitor找到）。
* Windows Server 2016已被正确识别。

## 版本4.0

* 将 psutil 更新为2.2.1。
* 在获取有关CPU负载的信息时，性能得到极大改善。
* 添加了对Windows 10识别的支持。
* 在Windows 10中，Windows的内部版本号也将被公布。
* 现在您可以使用插件管理器来访问插件帮助。

## 版本3.1

* 资源监视器正式支持Windows 8.1。
* 更新翻译。

## 版本3.0

* 将 psutil 更新为1.2.1。
* 报告当前Windows版本，CPU架构和服务包（如果有）（NVDA + Shift + 6）。
* 可以更改附加快捷键（NVDA 2013.3或更高版本）。
* 通过按资源快捷键两次，可以将单个资源信息复制到剪贴板。

## 版本2.4

* 新的语言：中文（简体），乌克兰语。
* 更新翻译。

## 版本2.3

* 增加保加利亚语翻译。

## 版本2.2

* 增加了以下翻译：阿拉伯语，阿拉贡语，克罗地亚语，荷兰语，芬兰语，法语，加利西亚语，德语，匈牙利语，意大利语，日语，韩语，尼泊尔语，波兰语，葡萄牙语（巴西），俄语，斯洛伐克语，斯洛文尼亚语，西班牙语，泰米尔语和土耳其语。

## 版本2.1

* 将 psutil 更新为0.6.1。
* 获取驱动器信息时修复很长时间的延迟。
* 代码清理。

## 版本2.0

* 增加了翻译支持和翻译评论。

## 版本1.0

* 发布初始版本

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
