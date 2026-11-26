# 05. Lỗi thường gặp

Phần lớn kết quả sai khi dùng GitNexus thuộc một trong hai loại: index không khớp code đang xem, hoặc graph không nối được một kiểu lời gọi. Trước khi tin một kết quả "không có caller" hay "không tìm thấy", hãy loại trừ hai nguyên nhân này. Bảng dưới gom các tình huống đã gặp khi dùng thực tế và cách xử lý.

## 1. Index không khớp code

| Triệu chứng | Nguyên nhân | Cách xử lý |
| --- | --- | --- |
| `status` báo stale dù đúng commit | Working tree có thay đổi chưa commit, kể cả file cấu hình chưa track | Tin cặp "Indexed commit"/"Current commit"; thêm file chưa track vào `.git/info/exclude` |
| Truy vấn không thấy code vừa pull | Chưa `git fetch` và pull trước khi index; `status` chỉ so với HEAD cục bộ | `git pull --ff-only` rồi `analyze` |
| "Not found" cho một symbol | Symbol đã bị xóa ở commit sau, hoặc index cũ hơn PR đang xem | `git log --diff-filter=D -- <file>`; index worktree của PR |
| Banner MCP "N commits behind" vẫn còn sau khi index lại | MCP server giữ trạng thái cũ | Dữ liệu trả về đã mới; kết nối lại MCP nếu cần |
| MCP `query` trả `processes: []` nhưng CLI thấy đủ | MCP server cache process cũ | Kiểm bằng CLI trước; đúng thì khởi động lại MCP, không cần index lại |
| Truy vấn nhầm dữ liệu của repo khác | Nhiều repo trong registry, không truyền `repo` | Luôn truyền `repo`; dọn index cũ bằng `gitnexus remove` |

## 2. Graph không nối được lời gọi

`impact` upstream chỉ đi theo cạnh gọi hàm và method; cạnh ở mức file không được tính. `upstream=0` không có nghĩa là an toàn. Các trường hợp graph thường trả UNKNOWN hoặc 0:

- Lời gọi qua `asyncio.to_thread(fn, ...)`, thread pool hoặc lambda.
- Class và method static trong C#.
- Lời gọi C++ qua receiver hoặc hàm inline trong header; tên trùng giữa `.h` và `.cpp` (gọi `impact` bằng `uid`).
- Truy cập dữ liệu và thuộc tính: bảng hằng, field của object.
- Caller ở ngôn ngữ khác gọi qua HTTP; field dùng chung giữa các ngôn ngữ.
- Gọi qua namespace object: `import * as x; x.a.b()`.

Cách xử lý chung: đối chiếu với `context` (caller đi vào) và grep tên symbol. Với file bị xóa, grep cả tên file lẫn tên symbol.

Một số giới hạn khác:

- Danh sách process bị cắt theo độ sâu và độ rẽ nhánh; thiếu một luồng không chứng minh luồng đó không tồn tại.
- Process của thư viện có thể đẩy process của code mình ra khỏi top kết quả; dùng nhãn của một luồng đã biết để kiểm tra.
- `explain` và lớp PDG không mô hình closure, callback, field và luồng ngầm; thay đổi ranh giới phân quyền giữa các service thường cho 0 phát hiện. Không có phát hiện không phải là bằng chứng an toàn.
- `rename` không dùng compiler: kiểm tra kỹ bản xem trước.
- `status` báo `scope-extraction-failed` hoặc `scope-extraction-unverified`: kết quả `impact` và `context` chỉ là cận dưới.

## 3. Lỗi khi index

| Triệu chứng | Nguyên nhân | Cách xử lý |
| --- | --- | --- |
| `query` chỉ trả biến, hằng, 0 process | Chỉ mục full-text hỏng, ví dụ trên ổ FUSE/NTFS không đổi tên file WAL được | `grep -i fts <log>` sau mỗi lần index; chạy `analyze --force` (`--repair-fts` không phải lúc nào cũng sửa được) |
| Database phình to, dựng chỉ mục lỗi | Chạy index tăng dần nhiều lần | `gitnexus clean -f` rồi `analyze --force` |
| `analyze` thứ hai chờ rồi bỏ cuộc | Tiến trình worker của lần trước vẫn giữ khóa | Tìm và dừng đúng pid của worker; chỉ chạy một `analyze` tại một thời điểm |
| "Only one write transaction at a time" | Hai tiến trình cùng mở `.gitnexus/lbug` | Dừng MCP server hoặc `analyze` còn lại; không xóa file khóa khi còn tiến trình ghi |
| `analyze` báo INCOMPLETE, mã thoát khác 0 | Ghi graph bị gián đoạn | Kiểm tra dung lượng ổ đĩa, không có `analyze` khác đang chạy, rồi `analyze --force` |
| `--name` trùng làm `analyze` lỗi sau vài phút | Tên đã có trong registry từ phiên cũ | Thêm hậu tố, ví dụ `-r2`; hoặc xóa tên cũ bằng `gitnexus remove` |
| MCP báo "DB not found at <đường dẫn cũ>" | Dùng lại tên cho worktree ở đường dẫn mới | Truyền `repo` là đường dẫn worktree thay vì tên |

## 4. Lỗi cài đặt

| Triệu chứng | Cách xử lý |
| --- | --- |
| npm 11: `Cannot destructure property 'package' of 'node.target'` khi chạy `npx` | `npm i -g gitnexus`, hoặc `bunx gitnexus@latest analyze` |
| MCP không khởi động kịp trong Claude Code | `npx` tải gói lần đầu vượt thời gian chờ khoảng 30 giây; cài toàn cục trước khi `setup` |
| `pnpm dlx` lỗi `ERR_DLOPEN_FAILED` | Thiếu file native `lbugjs.node`; dùng cài toàn cục bằng npm |

## 5. Lỗi khi chạy trong script và agent

- `pgrep -f 'gitnexus analyze'` khớp luôn dòng lệnh của chính vòng chờ, nên vòng chờ không bao giờ thoát. Dùng `pgrep -f '[g]itnexus analyze'`.
- Trong `cd x && VAR=... && nohup ... &`, dấu `&` cuối đưa cả chuỗi vào nền, nên `VAR` không có trong shell ngoài. Gán biến ở lệnh riêng.
- Dừng `analyze` giữa chừng không làm hỏng index cũ: `status` vẫn trỏ về commit trước.

## Tự kiểm tra

- [ ] Liệt kê được ít nhất bốn trường hợp `impact` trả UNKNOWN dù có caller.
- [ ] Biết cách phân biệt lỗi do MCP cache với lỗi do index cũ.
- [ ] Biết cách xử lý khi `query` không trả process nào.
