# Resource Monitor 顯示 CPU 負載 / 記憶體、電池、磁碟使用情形 #

* 作者：Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala 和其他 NVDA 貢獻者
* 下載 [穩定版][1]

這個附加元件提供有關 CPU 負載，記憶體使用情形，及其他資源的使用訊息。

# 快速鍵 #

* NVDA+Shift+E 顯示記憶體使用情形、CPU 使用率，如有連接電池，也讀出電池訊息。
* NVDA+Shift+1 顯示 CPU 平均使用率，及個別核心的使用情形。
* NVDA+Shift+2/5 顯示實體記憶體、虛擬記憶體的使用情形。
* NVDA+Shift+3 顯示本機磁碟及卸除是磁碟的總計空間及已用空間。
* NVDA+Shift+4 顯示電池電量及充電狀態。未充電時顯示剩餘時間。電量低時顯示警告。
* NVDA+Shift+6 顯示作業系統版本
* NVDA+Shift+7 顯示系統執行時間

如果您安裝了 NVDA 2013.3 或更高版本，您能變更這些快速鍵。

## 用戶請注意 ##

這個元件不會取代工作管理員及其她系統程式訊息。還要留意以下幾點：

* CPU 使用率是針對邏輯處理器而非實體核心。對於使用超執行緒的處理器來說，這是顯而易見的，其中 CPU 的數量是 CPU 核心數量的兩倍。
* 如果正在進行繁忙的磁碟活動（例如復制大型檔案），則獲取磁碟使用訊息時可能出現延遲。
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 ended on June
  30, 2018.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Version 18.04

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

## 17.12 版

* 支援 Windows 10 的 64 位元 ARM 處理器。

## 17.09 版

重要提醒：17.09.x 版是支援 Windows XP 的最後一個版本。

* 最後一個能在 Windows XP 執行的版本。
* Windows 10 組建 16278 及其之後的版本，已可被識別為 1709 版。等到組件 1709
  的穩定版釋出後，此元件也將發布一個小幅修正的版本。

## 17.07.1 版

* 重新支援 Windows XP。（早先從 17.02 版就不支援了）

## 17.05 版

* 顯示系統執行時間（最近一次開機後經過的時間，NVDA+Shift+7）

## 17.02 版

* 更新 psutil 到 5.0.1。
* 檢查磁碟使用情形時，在卸除是裝置未被正確識別的某些系統上（例如，當卡未插入讀卡機時）），NVDA 不在出現錯誤對話方塊。

## 16.08 版

從 16.08 版起，新版附加元件將使用年.月為版本號。

* Windows 10 的幾個更新版本，已可正確識別。（例如：1607、14393）
* Windows 10 組建版本（在安裝累積更新後），已可被正確識別，（如14393.51）。
* 如果使用 Windows 10 Insider Preview 組建，已可是別。

## 4.5 版的更新 ##

* 此元件的儲存庫班一道 GitHub，地址為 (https://github.com/josephsl/resourcemonitor)。
* Windows Server 2016 已能正確識別。

## 4.0 版的更新 ##

* 更新 psutil 到 2.2.1。
* 在獲取有關 CPU 負載訊息時，效能大幅改善。
* 新增了對 Windows 10 的識別。
* 在 Windows 10，已可顯示 Windows 的內部版本號。
* 您可在「管理附加元件」中，獲得元件說明。

## 3.1 版的更新 ##

* Resource Monitor 正是支援 Windows 8.1。
* 更新翻譯

## 3.0 版的更新 ##

* 更新 psutil 到 1.2.1。
* 顯示目前 Windows 版本及 Service Pack。(NVDA+Shift+6)
* 可變更元件快速鍵，（需 NVDA 2013.3 或更高版本。）
* 可複製個別資源摘要到剪貼簿，方法是相同的元件指令連按兩次。

## 2.4 版的更新 ##

* 新增語言：中文（簡體）、，烏克蘭文。
* 更新翻譯

## 2.3 版的更新 ##

* 新增保加利亞文翻譯。

## 2.2 版的更新 ##

* 新增以下翻譯：阿拉伯文、阿拉貢文、克羅埃西亞文、荷蘭文、芬蘭文、法文、加里斯亞文、德文、匈牙利文、意大利文、日文、韓文、尼泊爾文、波蘭文、葡萄牙文（巴西）、俄文、斯洛伐克文、斯洛維尼亞文、西班牙文、坦米爾文、土耳其文。

## 2.1 版的更新 ##

* 更新 psutil 到 0.6.1。
* 獲取磁碟訊息時，修復延遲較長時間的問題。
* 程式碼清理

## 2.0 版的更新 ##

* 支援翻譯元件及翻譯註解。

## 1.0 版的更新 ##

* 初始的版本

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
