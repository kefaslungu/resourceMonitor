# 資源監視器

* 作者：Alex Hall、Joseph Lee、Kefas Lungu、Beqa Gozalishvili、Tuukka Ojala、Ethin Probst、Kevin Derome 及其他 NVDA 貢獻者

此附加元件可提供 CPU 負載、記憶體使用量及其他系統資源的使用資訊。

## 快速鍵

所有指令皆支援隨選朗讀模式。

* NVDA+Shift+E：讀出 RAM（實體記憶體）使用量及處理器平均負載。
* NVDA+Shift+1：讀出處理器平均負載；若使用多核心 CPU，則一併讀出各核心的負載。
* NVDA+Shift+2/5：讀出實體記憶體與虛擬記憶體的已使用空間及總空間（若無法按下 NVDA+Shift+2 組合鍵，可改用 NVDA+Shift+5）。
* NVDA+Shift+3：讀出固定式（內建）、卸除式及網路磁碟機的已使用空間與總空間。
* NVDA+Shift+4：讀出無線網路連線資訊，包括網路名稱（SSID）及訊號強度；若沒有可用的 SSID，則會讀出沒有 SSID。
* NVDA+Shift+6: presents  Windows version, CPU architecture (AMD64 (x64), ARM64), and exact build number (build.revision).
* NVDA+Shift+7：讀出系統的運作時間。
* 未指派：讀出圖形處理器（GPU）資訊（在安全模式下無法使用）。
* 未指派：讀出圖形處理器（GPU）記憶體使用量資訊（在安全模式下無法使用）。

您可以透過「輸入手勢」對話框變更這些快速鍵。

## 使用說明

此附加元件無法取代 Windows 的工作管理員及其他系統資訊程式。另請注意以下事項：

* 除了整體資源使用狀況指令（NVDA+Shift+E）之外，其他指令按兩次會將資源使用資訊複製到剪貼簿。
* 在安全畫面中執行此附加元件時，無法將資源資訊複製到剪貼簿。
* CPU 使用率是以邏輯處理器為單位，而非實體核心。對於支援超執行緒（Hyper-Threading）的處理器，這一點尤其明顯，因為邏輯處理器的數量是 CPU 實體核心數量的兩倍。在某些較新的電腦上，並非所有 CPU 核心都會啟用超執行緒。
* 若磁碟活動頻繁，例如正在複製大型檔案或搜尋網路磁碟機時，取得磁碟使用量資訊可能會有所延遲。
* GPU 資訊僅適用於 NVIDIA GPU。
* When announcing processor architecture information as part of Windows version reporting, "AMD64" refer to 64-bit (x64) Intel and AMD processors. This information does not refer to the name of the actual processor in use.
* 不支援在 Windows 10/11 LTSC 上安裝此附加元件。

如需查看各版本附加元件之間的變更內容，請參閱[附加元件版本變更紀錄][1]文件。

如需查看各版本附加元件之間的變更內容，請參閱[附加元件版本變更紀錄][1]文件
