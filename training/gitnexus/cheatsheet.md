# Cheatsheet GitNexus

Lệnh và tool dùng nhiều nhất của GitNexus 1.6.10.

## Cài đặt và index

| Việc | Lệnh |
| --- | --- |
| Cài toàn cục | `npm install -g gitnexus` |
| Cấu hình MCP cho editor | `gitnexus setup` |
| Index lần đầu | `gitnexus analyze` |
| Index lại toàn bộ, không sửa `AGENTS.md`/`CLAUDE.md` | `gitnexus analyze --force --index-only` |
| Thêm lớp PDG | `gitnexus analyze --force --index-only --pdg` |
| Index worktree với tên riêng | `gitnexus analyze --index-only --force --name <repo>-pr<N>` |
| Xem độ mới của index | `gitnexus status` |
| Liệt kê repo đã index | `gitnexus list` |
| Xóa index repo hiện tại | `gitnexus clean -f` |
| Xóa index theo tên | `gitnexus remove <alias> -f` |
| Mở web UI | `gitnexus serve` (cổng 4747) |

## Truy vấn bằng CLI

| Việc | Lệnh |
| --- | --- |
| Tìm theo khái niệm | `gitnexus query "<khái niệm>" -r <repo>` |
| Toàn cảnh một symbol | `gitnexus context <symbol> -r <repo>` |
| Phạm vi ảnh hưởng | `gitnexus impact <symbol> -r <repo> -d upstream --depth 3` |
| Đường đi từ A tới B | `gitnexus trace <A> <B> -r <repo>` |
| Thay đổi đã stage | `gitnexus detect-changes -s staged` |
| So với nhánh chính | `gitnexus detect-changes -s compare -b origin/main` |
| Import vòng | `gitnexus check --cycles` |
| Cypher | `gitnexus cypher "<query>" -r <repo>` |

## MCP tool

| Tool | Câu hỏi trả lời |
| --- | --- |
| `list_repos` | Có những repo nào đã index? |
| `query` | Code nào liên quan tới khái niệm X? |
| `context` | Ai gọi symbol này, nó gọi ai, thuộc luồng nào? |
| `impact` | Sửa symbol này ảnh hưởng tới đâu? |
| `detect_changes` | Diff này chạm tới symbol và luồng nào, rủi ro mức nào? |
| `trace` | A tới được B bằng đường nào? |
| `rename` | Đổi tên an toàn trên nhiều file thế nào? |
| `cypher` | Truy vấn tùy ý trên graph |
| `route_map`, `api_impact`, `shape_check` | API route nào, ai gọi, sửa handler ảnh hưởng gì? |
| `pdg_query`, `explain` | Điều kiện nào bảo vệ câu lệnh này, dữ liệu bẩn đi tới đâu? (cần `--pdg`) |

## Hai quy tắc

1. Trước khi sửa symbol: `impact` upstream.
2. Trước khi commit: `detect_changes` với `scope: "staged"`.

## Đọc kết quả `impact`

| Độ sâu | Ý nghĩa |
| --- | --- |
| d=1 | Sẽ hỏng |
| d=2 | Nhiều khả năng bị ảnh hưởng |
| d=3 | Có thể cần test lại |

UNKNOWN hoặc 0 caller: grep lại trước khi kết luận.
