# Bài tập GitNexus

Sáu bài tập đi từ index repo đầu tiên tới review pull request và tích hợp vào workflow. Làm trên một repo mã nguồn mở cỡ vừa (vài trăm file) bằng ngôn ngữ chính đã chọn, hoặc trên project của nhóm kỹ năng 2–3 trong roadmap. Kết quả mỗi bài ghi vào `notes/bai-tap-NN.md` trong thư mục này.

## Bài 1. Index repo đầu tiên

Mục tiêu: G1, G2.

1. Cài GitNexus và chạy `gitnexus setup`.
2. Clone repo thực hành, chạy `gitnexus analyze`.
3. Ghi lại thời gian index và số node, số cạnh từ `gitnexus status`.
4. Trong AI coding assistant, gọi `list_repos` và đọc `gitnexus://repo/{name}/context`.

Đạt khi: `status` cho "Indexed commit" trùng "Current commit"; assistant liệt kê được repo.

## Bài 2. Tìm hiểu một luồng

Mục tiêu: G3.

1. Chọn một tính năng của repo, ví dụ đăng nhập hoặc xử lý request.
2. Dùng `query` tìm các symbol liên quan.
3. Dùng `context` trên 3 symbol chính.
4. Đọc resource `process/{name}` của luồng đó.
5. Vẽ lại luồng bằng Mermaid trong ghi chú.

Đạt khi: sơ đồ có ít nhất 5 bước và khớp với code khi đọc lại.

## Bài 3. Cypher

Mục tiêu: G3.

Viết truy vấn Cypher cho bốn câu hỏi:

1. Có bao nhiêu node mỗi loại?
2. Mười function có nhiều caller nhất là gì?
3. File nào import nhiều module nhất?
4. Có bao nhiêu process và process nào dài nhất?

Đạt khi: mỗi câu có truy vấn chạy được và kết quả.

## Bài 4. Đánh giá tác động trước khi sửa

Mục tiêu: G4.

1. Chọn một function được gọi ở nhiều nơi.
2. Chạy `impact` upstream với `--depth 3 --include-tests`.
3. Lập bảng symbol theo d=1, d=2, d=3 và mức rủi ro.
4. Grep tên function; so sánh số caller theo grep với số caller theo graph, giải thích chênh lệch.
5. Sửa chữ ký function, chạy `detect_changes -s unstaged`, đối chiếu với bảng ở bước 3.

Đạt khi: bảng tác động khớp với danh sách file phải sửa thực tế; chênh lệch với grep được giải thích bằng các trường hợp ở bài 05.

## Bài 5. Review pull request

Mục tiêu: G5.

1. Chọn một PR đã merge của repo thực hành.
2. Tạo worktree tại head của PR, index với `--name <repo>-pr<N>`.
3. Tính merge-base, chạy `detect_changes` với `scope: "compare"`.
4. Chạy `impact` trên từng symbol thay đổi; liệt kê symbol d=1 nằm ngoài diff.
5. Viết nhận xét review: phát hiện kèm mức HIGH, MEDIUM, LOW và kết luận APPROVE, REQUEST CHANGES hoặc NEEDS DISCUSSION.
6. Dọn worktree và index.

Đạt khi: có bản review; `gitnexus list` không còn index của worktree.

## Bài 6. Tích hợp vào workflow

Mục tiêu: G6.

1. Thêm khối quy tắc GitNexus (bài 04, mục 2) vào `CLAUDE.md` hoặc `AGENTS.md` của repo thực hành.
2. Thêm Git pre-commit hook chạy `gitnexus check --cycles`.
3. Làm một thay đổi nhỏ có commit theo đúng vòng ở bài 04, Hình 1; ghi lại từng lời gọi tool.
4. Xác nhận hook PostToolUse báo index stale sau commit.
5. Tùy chọn: dựng workflow GitHub Actions ở bài 04, mục 9 và ghi lại kết quả chạy.

Đạt khi: commit có ghi chép đầy đủ các bước `impact` và `detect_changes`.
