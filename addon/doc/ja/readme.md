# Resource Monitor #

* 作者: Alex Hall, Joseph Lee, beqa gozalishvili and other NVDA contributors
* Download [stable version][1]
* Download [development version][2]

このアドオンはCPU負荷、メモリ使用量などリソースの使用状態を通知します。

Important: Resource Monitor 3.1 is not compatible with NvDA 2013.3 or
earlier. If you use 2013.3 or earlier, please use Resource Monitor 3.0.

# キー操作 #

* NVDA+Shift+E メモリ使用量、平均プロセッサー負荷、バッテリーがある場合はその情報も通知します。
* NVDA+Shift+1 平均CPU負荷、マルチコアの場合は各コアの負荷を通知します。
* NVDA+Shift+2/5 物理メモリと仮想メモリの使用量と合計量を通知します。
* NVDA+Shift+3 コンピューターの内蔵および外付けディスクの使用量と合計量を通知します。
* NVDA+Shift+4 バッテリー残量のパーセント値、充電状態、残り時間(放電中のとき)、バッテリーの低下やバッテリー切れの警告を通知します。
* NVDA+Shift+6 CPUアーキテクチャーの32/64ビット、Windowsのバージョンやサービスパックの情報を通知します。

NVDA 2013.3 以降の場合はこれらのショートカットキーは変更できます。

## 使用方法 ##

このアドオンはタスクマネージャーやWindowsのシステム情報プログラムの代替ではありません。以下をお読みください：

* CPU負荷は物理コアではなく論理プロセッサーについて示します。ハイパースレッディング対応のCPUでは論理プロセッサー数は物理コアの数の2倍になります。
* CPU負荷情報の取得には時間がかかる場合があります。

## Changes for 3.1 ##

* Resource Monitor officially supports Windows 8.1.
* Updated translations.

## Changes for 3.0 ##

* psutil を 1.2.1 に更新。
* 現在のWindowsのバージョンやCPUアーキテクチャー、サービスパックの通知（NVDA+Shift+6）
* ショートカットキーの入力ジェスチャー変更に対応(NVDA 2013.3以降).
* コマンドを2回続けて押すとそれぞれのリソース情報をコピーする機能を追加。

## Changes for 2.4 ##

* New languages: Chinese (simplified), Ukrainian.
* Updated translations.

## Changes for 2.3 ##

* Added Bulgarian translation.

## Changes for 2.2 ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## Changes for 2.1 ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Code cleanup.

## Changes for 2.0 ##

* added translation support and translation comments.

## Changes for 1.0 ##

* Initial Release

[[!tag stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
