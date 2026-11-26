# 02. Cài đặt và index

Bài này đi từ cài CLI, kết nối MCP tới index repo đầu tiên và kiểm tra index còn mới. Điểm cần nhớ nhất: luôn kiểm tra cặp "Indexed commit" và "Current commit" trong `gitnexus status` trước khi tin kết quả truy vấn.

## 1. Cài đặt

Cài toàn cục để tránh lỗi khi `npx` tải gói lần đầu (xem bài 05, mục npm 11):

```bash
npm install -g gitnexus
gitnexus --version
```

Lần đầu trong một repo có thể chạy thẳng bằng `npx`:

```bash
npx gitnexus analyze
```

## 2. Kết nối MCP với AI coding assistant

Lệnh `setup` tự phát hiện editor và cấu hình MCP, skill và hook; chỉ cần chạy một lần trên máy.

```bash
gitnexus setup                 # tự phát hiện
gitnexus setup -c cursor,codex # chỉ cấu hình các agent được liệt kê
gitnexus uninstall             # xem trước việc gỡ; thêm -f để gỡ thật
```

Mức hỗ trợ theo editor:

| Editor | Mức hỗ trợ |
| --- | --- |
| Claude Code, Codex | Đầy đủ: MCP, skill, hook PreToolUse và PostToolUse |
| Cursor, Antigravity, Factory, OpenCode | Đầy đủ qua hook sau mỗi tool |
| CodeBuddy, Qoder | MCP và skill |
| Windsurf | Chỉ MCP, cấu hình tay |

Cấu hình tay khi không dùng `setup`:

```bash
# Claude Code
claude mcp add gitnexus -- npx -y gitnexus@latest mcp
```

```json
// Cursor: ~/.cursor/mcp.json
{ "mcpServers": { "gitnexus": { "command": "npx", "args": ["-y", "gitnexus@latest", "mcp"] } } }
```

Khi nhiều agent chạy cùng lúc, nên dùng một MCP server HTTP chung thay vì mỗi agent một tiến trình:

```bash
gitnexus mcp --http --port 3111
# client kết nối tới http://127.0.0.1:3111/mcp
```

## 3. Index repo

Chạy từ thư mục gốc của repo:

```bash
gitnexus analyze                          # lần đầu
gitnexus analyze --force --index-only     # dựng lại toàn bộ, không sửa AGENTS.md/CLAUDE.md
gitnexus analyze --force --index-only --pdg   # thêm lớp PDG cho pdg_query, explain
```

Các cờ hay dùng:

| Cờ | Tác dụng |
| --- | --- |
| `-f`, `--force` | Dựng lại toàn bộ index |
| `--index-only` | Chỉ index, không ghi khối GitNexus vào `AGENTS.md`/`CLAUDE.md` và không cài skill |
| `--skip-agents-md` | Giữ nguyên phần đã sửa tay trong `AGENTS.md`/`CLAUDE.md` |
| `--no-stats` | Bỏ số liệu hay thay đổi khỏi `AGENTS.md`/`CLAUDE.md`, tránh diff mỗi lần index |
| `--pdg` | Thêm lớp PDG |
| `--embeddings [limit]` | Bật embedding cho tìm kiếm ngữ nghĩa (mặc định tắt) |
| `--name <alias>` | Đặt tên riêng cho index, dùng khi index worktree |
| `--skills` | Sinh skill theo từng community vào `.claude/skills/gitnexus-area-<name>/` |
| `--max-file-size <kb>` | Bỏ qua file lớn hơn ngưỡng, mặc định 512 KB |

Kinh nghiệm thực tế trên một monorepo lớn:

- `--force` dựng lại toàn bộ thường nhanh hơn index tăng dần. Index tăng dần chạy nhiều lần còn làm database phình to tới mức hỏng chỉ mục full-text.
- Index toàn bộ mất khoảng 10–17 phút; bật `--pdg` chậm hơn 2–3 lần. Repo nhỏ chỉ mất vài giây tới vài phút.
- Nên dùng `--index-only` khi `AGENTS.md`/`CLAUDE.md` có phần sửa tay, tránh bị ghi đè hoặc xung đột khi `git pull`.

Có thể đặt sẵn tùy chọn trong file `.gitnexusrc` (JSON) ở gốc repo; cờ trên dòng lệnh luôn ghi đè file này.

## 4. Kiểm tra index còn mới

```bash
git fetch && git pull --ff-only   # status chỉ so với HEAD cục bộ
gitnexus status
gitnexus list                     # các repo đã index
```

Đọc kết quả `status`:

- So sánh "Indexed commit" với "Current commit". Trùng nhau là index mới.
- `status` báo stale khi working tree có thay đổi chưa commit, kể cả khi hai commit trùng nhau. Tin cặp commit, không tin chữ "stale".
- Không tin dòng tiêu đề "indexed by GitNexus (N symbols...)" trong `AGENTS.md`/`CLAUDE.md`: dòng này không được cập nhật khi dùng `--index-only`.
- Cách kiểm chắc nhất: gọi `gitnexus context <symbol-mới-thêm>` với một symbol chỉ có ở commit mới.

## 5. Chọn file cần index

GitNexus đọc `.gitignore` và `.gitnexusignore` ở gốc repo, cùng global excludes và `.git/info/exclude`. File `.gitignore` ở thư mục con không được đọc. `node_modules`, `dist`, `vendor`, `venv`, `site-packages` nằm trong danh sách bỏ qua mặc định.

Quy tắc phủ định `!` trong `.gitnexusignore` ghi đè cả danh sách mặc định lẫn `.gitignore`. Muốn index một thư viện trong `node_modules`, phải mở từng tầng, vì gitignore không cho mở lại thư mục con khi thư mục cha đang bị loại:

```gitignore
!<pkg>/node_modules/
<pkg>/node_modules/*
!<pkg>/node_modules/@scope/
<pkg>/node_modules/@scope/*
!<pkg>/node_modules/@scope/lib/
# Quy tắc dist/ ở gốc thắng âm thầm (quy tắc cuối cùng khớp sẽ thắng), nên phải mở dist tường minh
!<pkg>/node_modules/@scope/*/dist/
!<pkg>/node_modules/@scope/*/dist/**
# Chặn phụ thuộc bắc cầu
<pkg>/node_modules/@scope/*/node_modules/
```

Dấu hiệu dính bẫy `dist`: thư viện trong graph chỉ có `package.json`, `README` và `src`. Kiểm tra số file đã index so với trên đĩa bằng Cypher:

```cypher
MATCH (f:File) WHERE f.filePath STARTS WITH '<path>' RETURN count(f)
```

Với cây mã nguồn C++ của bên thứ ba, nên loại các thư mục ThirdParty, Testing, Examples, Docs.

## 6. Dọn index

```bash
gitnexus clean -f            # xóa index của repo hiện tại
gitnexus remove <alias> -f   # xóa index theo tên, chạy được từ bất kỳ đâu
```

## Tự kiểm tra

- [ ] `gitnexus list` hiện repo vừa index.
- [ ] Assistant gọi được MCP tool `list_repos`.
- [ ] Giải thích được vì sao `status` có thể báo stale dù index đúng commit.
- [ ] Viết được `.gitnexusignore` để index một thư viện trong `node_modules`.
