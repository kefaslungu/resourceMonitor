# Resource Monitor

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## キー操作

* NVDA+Shift+E メモリ使用量、平均プロセッサー負荷、バッテリーがある場合はその情報も通知します。
* NVDA+Shift+1 平均CPU負荷、マルチコアの場合は各コアの負荷を通知します。
* NVDA+Shift+2/5 物理メモリと仮想メモリの使用量と合計量を通知します。
* NVDA+Shift+3 コンピューターの内蔵および外付けディスクの使用量と合計量を通知します。
* NVDA+Shift+4 バッテリー残量のパーセント値、充電状態、残り時間(放電中のとき)、バッテリーの低下やバッテリー切れの警告を通知します。
* NVDA+Shift+6 CPUアーキテクチャーの32/64ビット、Windowsのバージョンやサービスパックの情報を通知します。
* NVDA+Shift+7 presents the system's uptime.

If you have NVDA 2013.3 or later installed, you can change these shortcut keys via input gestures dialog.

## 使用方法

このアドオンはタスクマネージャーやWindowsのシステム情報プログラムの代替ではありません。以下をお読みください：

* CPU負荷は物理コアではなく論理プロセッサーについて示します。これは、CPUの数がCPUコアの数の2倍になるハイパースレッディング対応のCPUで顕著に表れます。
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* This add-on requires Windows 7 Service Pack 1 or later.
