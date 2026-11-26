# Training GitNexus

Khóa này hướng dẫn dùng [GitNexus](https://github.com/abhigyanpatwari/GitNexus) để hiểu codebase, đánh giá tác động trước khi sửa code và review pull request, rồi đưa các bước đó vào workflow hằng ngày cùng AI coding assistant. Nội dung tổng hợp từ tài liệu chính thức, phần `--help` của CLI và kinh nghiệm dùng GitNexus trên một monorepo nhiều ngôn ngữ (TypeScript, C#, Python, C++) cỡ 400–530 nghìn node. Sau khóa học, người học tự index được một repo, truy vấn được graph và áp dụng quy trình "impact trước khi sửa, detect_changes trước khi commit".

| Thông tin | Giá trị |
| --- | --- |
| Phiên bản dùng trong bài | GitNexus CLI 1.6.10 (MCP server 17 tool) |
| Ngày kiểm tra tài liệu | 26/11/2026 |
| Giấy phép GitNexus | PolyForm Noncommercial 1.0.0; dùng cho mục đích thương mại cần license riêng |
| Yêu cầu | Node.js 22.18+ (nhánh 22.x) hoặc 24.11+, Git, một AI coding assistant có MCP (ví dụ Claude Code) |

> Tài liệu trên nhánh `main` của GitNexus mới hơn bản 1.6.10, có thêm `analyze --watch`, lệnh `auto-sync` và các MCP tool `read_file`, `grep`. Khóa này dạy theo 1.6.10; tính năng chỉ có ở bản mới được ghi chú "bản mới hơn".

## 1. Mục tiêu

| Mã | Sau khóa học, người học làm được | Cách kiểm |
| --- | --- | --- |
| G1 | Cài GitNexus, kết nối MCP với AI coding assistant | `gitnexus list` hiện repo; assistant gọi được `list_repos` |
| G2 | Index một repo và kiểm tra index còn mới | `gitnexus status` cho "Indexed commit" trùng "Current commit" |
| G3 | Truy vấn graph bằng `query`, `context`, `impact`, `cypher` | Hoàn thành bài tập 2 và 3 |
| G4 | Đánh giá tác động trước khi sửa một symbol | Hoàn thành bài tập 4, có bảng d=1/d=2/d=3 |
| G5 | Review một pull request bằng worktree và index riêng | Hoàn thành bài tập 5 |
| G6 | Đưa GitNexus vào workflow: quy tắc agent, hook, pre-commit | Repo thực hành có khối quy tắc trong `CLAUDE.md` hoặc `AGENTS.md` |

## 2. Bài học

Đọc theo thứ tự. Mỗi bài kết thúc bằng phần "Tự kiểm tra".

| Bài | Nội dung | Thời lượng gợi ý |
| --- | --- | --- |
| [01. Tổng quan](01-tong-quan.md) | GitNexus là gì, cách xây graph, schema node và cạnh | 30 phút |
| [02. Cài đặt và index](02-cai-dat-va-index.md) | Cài CLI, kết nối MCP, `analyze`, `status`, `.gitnexusignore` | 1 giờ |
| [03. Truy vấn graph](03-truy-van-graph.md) | 17 MCP tool, lệnh CLI tương ứng, Cypher | 2 giờ |
| [04. Tích hợp vào workflow](04-tich-hop-workflow.md) | Vòng làm việc hằng ngày, review PR, debug, refactor, hook, CI | 2 giờ |
| [05. Lỗi thường gặp](05-loi-thuong-gap.md) | Index cũ, kết quả thiếu, khóa database, cách xử lý | 45 phút |
| [Cheatsheet](cheatsheet.md) | Lệnh và tool dùng nhiều nhất trên một trang | Tra cứu |
| [Bài tập](bai-tap.md) | 6 bài thực hành từ index tới review PR | 4–6 giờ |

## 3. Nguồn

- Repo GitNexus: `README.md`, `docs/cli-reference.md`, `docs/mcp-reference.md`, `docs/editor-setup.md`, `RUNBOOK.md` trên nhánh `main`, đọc ngày 26/11/2026.
- Kết quả `gitnexus --help` và `gitnexus <lệnh> --help` của bản 1.6.10.
- Bộ skill GitNexus cho Claude Code: `gitnexus-guide`, `gitnexus-cli`, `gitnexus-exploring`, `gitnexus-debugging`, `gitnexus-impact-analysis`, `gitnexus-refactoring`, `gitnexus-review`, `gitnexus-plan`, `gitnexus-work`, `gitnexus-lfg`, `gitnexus-pdg-query`, `gitnexus-taint-analysis`.
- Ghi chép kinh nghiệm cá nhân khi dùng GitNexus cho review PR và phân tích tác động; chi tiết của dự án gốc đã được lược bỏ.
