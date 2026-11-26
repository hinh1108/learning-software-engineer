# 03. Truy vấn graph

Bài này giới thiệu 17 MCP tool của GitNexus 1.6.10 và lệnh CLI tương ứng. Bốn tool dùng nhiều nhất là `query`, `context`, `impact` và `detect_changes`; các tool còn lại dùng cho tình huống chuyên biệt. Graph chỉ là bản đồ chỉ chỗ cần xem: kết luận cuối cùng phải dựa trên đọc code, grep và chạy test.

## 1. Quy tắc chung

- Gọi `list_repos` trước để biết tên repo. Khi có từ hai repo trở lên trong registry, mọi lời gọi phải truyền `repo`, nếu không tool báo lỗi "Multiple repositories indexed" hoặc truy vấn nhầm index cũ của repo khác.
- Đọc resource `gitnexus://repo/{name}/context` để xem số liệu, độ mới của index và danh sách tool.
- Báo kèm tên repo và độ mới của index khi trả lời dựa trên graph.

## 2. Bốn tool chính

### 2.1 `query`: tìm theo khái niệm

Tìm kiếm lai (BM25, semantic) và gom kết quả theo process.

```text
query({ search_query: "user login", task_context: "debug login timeout", repo: "<repo>" })
```

```bash
gitnexus query "user login" -r <repo> -l 5
```

Kết quả phụ thuộc chỉ mục full-text. Nếu `query` chỉ trả về biến, hằng và không có process nào, chỉ mục full-text có thể đã hỏng (xem bài 05).

### 2.2 `context`: nhìn toàn cảnh một symbol

Trả về caller, callee, process chứa symbol, route liên quan và cờ `is_entry_point`.

```text
context({ name: "validateUser", repo: "<repo>" })
context({ uid: "<uid>", repo: "<repo>" })          # khi trùng tên
```

```bash
gitnexus context validateUser -r <repo>
gitnexus context validateUser -r <repo> -f src/auth/validate.ts
```

`context` là cách tin cậy nhất để kiểm tra index đã có code mới hay chưa.

### 2.3 `impact`: phạm vi ảnh hưởng

Liệt kê symbol phụ thuộc, nhóm theo độ sâu, kèm độ tin cậy.

```text
impact({ target: "validateUser", direction: "upstream", maxDepth: 3, includeTests: true, repo: "<repo>" })
```

```bash
gitnexus impact validateUser -r <repo> -d upstream --depth 3 --include-tests
gitnexus impact validateUser -r <repo> --mode pdg      # dùng lớp PDG
```

Cách đọc kết quả:

| Độ sâu | Ý nghĩa | Việc cần làm |
| --- | --- | --- |
| d=1 | Sẽ hỏng: caller và importer trực tiếp | Phải sửa theo hoặc kiểm tra |
| d=2 | Nhiều khả năng bị ảnh hưởng | Nên kiểm tra |
| d=3 | Có thể cần test lại | Chạy test liên quan |

| Mức rủi ro | Dấu hiệu |
| --- | --- |
| LOW | Dưới 5 symbol, ít process |
| MEDIUM | 5–15 symbol, 2–5 process |
| HIGH | Trên 15 symbol hoặc nhiều process |
| CRITICAL | Chạm luồng xác thực, thanh toán hoặc tương đương |

`UNKNOWN` nghĩa là không tìm thấy caller nào, không phải rủi ro thấp: caller có thể nằm ở chỗ graph không nối được. Luôn grep lại. Kết quả có `partial: true` hoặc `truncated: true` là chưa đầy đủ.

### 2.4 `detect_changes`: ánh xạ diff sang symbol

```text
detect_changes({ scope: "staged", repo: "<repo>" })
detect_changes({ scope: "compare", base_ref: "<merge-base-sha>", repo: "<repo>" })
```

```bash
gitnexus detect-changes -s staged
gitnexus detect-changes -s compare -b origin/main
```

`scope` nhận `unstaged`, `staged`, `all` hoặc `compare`. Kết quả gồm symbol thay đổi, process bị ảnh hưởng và `risk_level`. Lệnh CLI in dạng text, không phải JSON.

## 3. Tool chuyên biệt

| Tool | Dùng khi | Ghi chú |
| --- | --- | --- |
| `list_repos` | Xem repo đã index | Phân trang bằng `limit`, `offset` |
| `trace` | Tìm đường đi ngắn nhất từ A tới B | Không có đường thì node xa nhất cho biết chuỗi đứt ở đâu |
| `rename` | Đổi tên symbol trên nhiều file | Mặc định chỉ xem trước; xem mục 4 |
| `cypher` | Truy vấn tùy ý | Đọc resource `schema` trước |
| `check` | Kiểm tra cấu trúc, ví dụ import vòng | CLI: `gitnexus check --cycles` |
| `route_map` | Xem API route, nơi gọi và handler | |
| `api_impact` | Đánh giá trước khi sửa một route handler | Gồm consumer, middleware, độ lệch cấu trúc response |
| `shape_check` | So khóa trong response với thuộc tính consumer đọc | Báo MISMATCH |
| `tool_map` | Xem định nghĩa MCP/RPC tool và nơi xử lý | |
| `pdg_query` | Phụ thuộc ở mức câu lệnh trong một hàm | Cần `--pdg`; `mode: "controls"` hoặc `"flows"` |
| `explain` | Xem luồng taint từ source tới sink | Cần `--pdg`; chỉ có qua MCP |
| `group_list`, `group_sync` | Làm việc với nhóm nhiều repo | Contract Registry giữa các repo |

## 4. Đổi tên an toàn với `rename`

1. Gọi `rename` không kèm `dry_run` hoặc với `dry_run: true` để xem trước.
2. Kiểm tra danh sách `file_path`, đối chiếu phần sửa theo graph với phần sửa theo tìm chuỗi.
3. Gọi lại với cùng tham số, `dry_run: false` và `plan_token` từ bản xem trước. Token dùng một lần, hết hạn sau 15 phút.
4. Chạy `detect_changes` rồi chạy test.

`rename` không dùng compiler, từ chối tham chiếu mơ hồ hoặc động, không di chuyển file, và bước áp dụng không có giao dịch hoàn tác.

## 5. Cypher

Mọi cạnh nằm trong một bảng `CodeRelation`; lọc theo `type`. Viết `[r:CDG]` sẽ lỗi.

```cypher
// Liệt kê bảng node
CALL show_tables() RETURN *

// Ai gọi validateUser
MATCH (a)-[r:CodeRelation]->(b:Function {name: 'validateUser'})
WHERE r.type = 'CALLS'
RETURN a.name, a.filePath

// Cạnh PDG
MATCH ()-[r:CodeRelation]->() WHERE r.type IN ['CDG', 'REACHING_DEF', 'CFG'] RETURN count(r)

// Kiểm tra đủ chỉ mục full-text
CALL SHOW_INDEXES() RETURN *
```

Node `Process` có `heuristicLabel`, `label`, `entryPointId`, `terminalId`, không có `name`.

## 6. Resource và prompt MCP

| Resource | Nội dung |
| --- | --- |
| `gitnexus://repos` | Danh sách repo |
| `gitnexus://repo/{name}/context` | Số liệu, độ mới, tool khả dụng; đọc đầu tiên |
| `gitnexus://repo/{name}/clusters`, `.../cluster/{name}` | Các community |
| `gitnexus://repo/{name}/processes`, `.../process/{name}` | Các luồng thực thi |
| `gitnexus://repo/{name}/schema` | Schema graph cho Cypher |

Hai prompt có sẵn: `detect_impact` (phân tích trước khi commit) và `generate_map` (sinh tài liệu kiến trúc kèm sơ đồ Mermaid).

## Tự kiểm tra

- [ ] Biết khi nào phải truyền `repo`.
- [ ] Đọc được bảng d=1/d=2/d=3 và giải thích vì sao UNKNOWN không có nghĩa là an toàn.
- [ ] Viết được truy vấn Cypher tìm caller của một hàm.
- [ ] Làm được quy trình `rename` hai bước.
