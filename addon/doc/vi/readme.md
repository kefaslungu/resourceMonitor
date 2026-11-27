# Theo dõi tài nguyên

* Tác giả: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome và những người đóng góp NVDA khác

Add-on này cung cấp các thông tin về tải CPU, sử dụng bộ nhớ và các nguồn tài nguyên khác.

## Các phím tắt

Tất cả các lệnh đã hỗ trợ chế độ đọc theo yêu cầu.

* NVDA+Shift+E: enters the Resource Monitor command layer. There are two modes:
	* Lock: pressing the layer entry command once will keep the layer mode active until the Escape key or a key not defined in the layer mode (see below) is pressed. Keys not defined in the layer mode will be passed to the application.
	* Report: performing a resource usage info command will announce the information and exit the layer mode. Press the layer entry command repeatedly to lock the layer mode.

Các lớp lệnh sau đây có sẵn để lấy thông tin về mức sử dụng tài nguyên riêng lẻ:

* Space: thông tin tổng quan về mức sử dụng tài nguyên, bao gồm RAM (bộ nhớ vật lý) đã sử dụng và tải trung bình của bộ xử lý.
* C: CPU (tải trung bình của bộ xử lý và nếu là CPU đa lõi thì tính tải của từng lõi)
* D: ổ đĩa (dung lượng đã sử dụng và tổng dung lượng của các ổ đĩa cố định (gắn liền), ổ đĩa di động và ổ đĩa mạng)
* G (không khả dụng ở chế độ bảo mật): thông tin bộ xử lý đồ họa (GPU)
* Shift+G (không khả dụng ở chế độ bảo mật): Sử dụng bộ nhớ GPU
* M: bộ nhớ (dung lượng đã sử dụng và tổng dung lượng cho cả RAM vật lý và ảo)
* O: Hệ điều hành (phiên bản Windows, kiến ​​trúc CPU và số bản dựng chính xác (build.revision))
* U: thời gian hoạt động của hệ thống
* W: Wi-Fi (tên mạng (SSID), cường độ tín hiệu, chế độ bảo mật, hoặc không có SSID nếu không có mạng nào)

You can also assign shortcuts to announce individual resource information without entering the layer first (go to NvDA menu/Preferences/Input gestures to assign custom commands).

## Các lưu ý sử dụng

Add-on này không thay thế cho task manager và các trình kiểm tra thông tin hệ thống khác của Windows. Cũng lưu ý những điểm sau:

* Pressing resource commands twice or Control+NVDA+X will copy resource usage information to the clipboard (pressing Control+NVDA+X copies the last spoken resource information).
* Không thể sao chép thông tin tài nguyên vào bộ nhớ tạm nếu chạy tiện ích bổ sung trong màn hình bảo vệ.
* Mức sử dụng CPU được hiển thị cho các bộ xử lý logic, chứ không phải lõi vật lý. Điều này dễ nhận thấy ở các bộ xử lý có công nghệ Hyper-Threading, trong đó số lượng CPU gấp đôi số lượng lõi CPU. Trên một số máy tính đời mới hơn, không phải tất cả các lõi CPU đều được bật công nghệ Hyper-Threading.
* Nếu có nhiều hoạt động trên ổ đĩa, chẳng hạn như sao chép các tập tin lớn hoặc khi tìm kiếm các ổ đĩa mạng, có thể sẽ xảy ra độ trễ khi thu thập thông tin về mức sử dụng ổ đĩa.
* NVDA sẽ phát ra âm thanh và thông báo mỗi khi kết nối hoặc ngắt kết nối với mạng không dây. Xem phần tiếp theo để biết cách thay đổi hành vi này.
* Thông tin về GPU được cung cấp cho các GPU của Nvidia.
* Khi công bố thông tin kiến ​​trúc bộ xử lý như một phần của báo cáo phiên bản Windows, "AMD64" đề cập đến các bộ xử lý Intel và AMD 64-bit (x64). Thông tin này không đề cập đến tên của bộ xử lý thực tế đang được sử dụng.
* Cài đặt tiện ích bổ sung trên Windows 10/11 LTSC không được hỗ trợ.

## Cài đặt

You can configure the following settings from NVDA settings screen under Resource Monitor category:

* Enter resource monitor layer when layer command is performed: select between once (default, lock the layer mode) or repeatedly (pressing once will anounce resource info once, press repeatedly to lock the layer mode).
* Đơn vị đo nhiệt độ GPU: Chọn đơn vị đo nhiệt độ được hiển thị trong thông tin GPU (độ C hoặc độ F).
* Thông báo kết nối/ngắt kết nối Wi-Fi: Chọn cách NVDA sẽ thông báo các thông báo kết nối/ngắt kết nối Wi-Fi (tắt, tin nhắn, âm thanh, cả tin nhắn và âm thanh).
* Ký hiệu dung lượng bộ nhớ và ổ đĩa: chọn cách hiển thị dung lượng bộ nhớ RAM và dung lượng ổ đĩa theo đơn vị như gigabyte và terabyte (mặc định là phương pháp thay thế (KB/MB/...)).

Để biết danh sách các thay đổi được thực hiện giữa mỗi bản phát hành tiện ích bổ sung, hãy tham khảo tài liệu [thay đổi cho bản phát hành của tiện ích bổ sung][1].

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
