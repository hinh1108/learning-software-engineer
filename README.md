# Learning Software Engineer 2027

Repo này ghi lại lộ trình tự học kỹ sư phần mềm trong năm 2027, từ 01/01/2027 đến 31/12/2027. Lộ trình chia thành bốn giai đoạn theo quý: nền tảng khoa học máy tính, backend và system design, cloud và vận hành, rồi AI engineering. Mỗi giai đoạn kết thúc bằng một project có code, test và tài liệu đặt trong repo này. Kết quả cuối năm là một bộ project và ghi chép đủ để chứng minh năng lực khi phỏng vấn hoặc nhận việc thực tế.

## 1. Mục tiêu

Mỗi mục tiêu có chỉ số và hạn để cuối mỗi quý tự đánh giá được là đạt hay chưa.

| Mã | Mục tiêu | Chỉ số | Ngưỡng đạt | Hạn |
| --- | --- | --- | --- | --- |
| G1 | Nắm vững cấu trúc dữ liệu và giải thuật | Số bài tập đã giải, có lời giải và phân tích độ phức tạp trong `exercises/` | 150 bài | 31/03/2027 |
| G2 | Xây được một backend service hoàn chỉnh | Project Q2 có API, database, test tự động và CI chạy xanh | Test coverage từ 70% | 30/06/2027 |
| G3 | Deploy và vận hành service trên cloud | Project Q3 chạy trên cloud, có monitoring, log và tài liệu rollback | Có ít nhất 1 runbook xử lý sự cố | 30/09/2027 |
| G4 | Xây ứng dụng có dùng LLM | Project Q4 có RAG hoặc agent, kèm bộ eval tự động | Bộ eval từ 50 case | 31/12/2027 |
| G5 | Duy trì thói quen học đều | Số tuần có ít nhất 1 commit ghi chép hoặc code | 48/52 tuần | 31/12/2027 |

## 2. Lộ trình

Lộ trình đi từ nền tảng lên ứng dụng; giai đoạn sau dùng lại kiến thức và project của giai đoạn trước. Việc dùng AI coding assistant được áp dụng xuyên suốt cả năm, không tách thành một giai đoạn riêng.

### 2.1 Quý 1: Nền tảng khoa học máy tính

- Cấu trúc dữ liệu và giải thuật: mảng, danh sách liên kết, cây, đồ thị, hash table, sắp xếp, tìm kiếm, quy hoạch động.
- Hệ điều hành: tiến trình, luồng, bộ nhớ, hệ thống file, đồng bộ hóa.
- Mạng máy tính: TCP/IP, HTTP/HTTPS, DNS, TLS.
- Công cụ: Git, Linux shell, editor, debugger.
- Một ngôn ngữ chính, dùng cho cả năm (xem mục 8).

Project Q1: một công cụ dòng lệnh (CLI) có test, ví dụ trình quản lý ghi chú hoặc trình phân tích log.

### 2.2 Quý 2: Backend và system design

- Thiết kế API: REST, GraphQL, phân trang, versioning, xử lý lỗi.
- Database: SQL, chỉ mục, transaction, mô hình dữ liệu; một hệ NoSQL để so sánh.
- Kiểm thử: unit test, integration test, test pyramid.
- System design: cache, message queue, cân bằng tải, khả năng mở rộng, tính nhất quán dữ liệu.
- Clean code, design pattern, refactoring.

Project Q2: một backend service có xác thực người dùng, database, test tự động và CI.

### 2.3 Quý 3: Cloud, DevOps và bảo mật

- Container: Docker, Docker Compose.
- Điều phối: Kubernetes ở mức deploy, scale và cấu hình.
- Infrastructure as Code: Terraform.
- CI/CD: pipeline build, test, deploy, rollback.
- Observability: metrics, log, tracing, cảnh báo.
- Bảo mật ứng dụng: OWASP Top 10, quản lý secret, phân quyền.

Project Q3: deploy project Q2 lên cloud, kèm dashboard monitoring và runbook.

### 2.4 Quý 4: AI engineering

- Nền tảng LLM: token, context window, prompt, structured output, tool use.
- Retrieval-Augmented Generation (RAG): embedding, vector database, chunking, reranking.
- Agent: vòng lặp tool use, Model Context Protocol (MCP), xử lý lỗi và giới hạn chi phí.
- Đánh giá: xây bộ eval, so sánh phiên bản prompt và model.
- Làm việc với AI coding assistant: viết đặc tả rõ, review code do AI sinh, giữ chất lượng test.

Project Q4: một ứng dụng hỏi đáp trên tài liệu riêng hoặc một agent tự động hóa công việc, kèm bộ eval.

## 3. Cấu trúc repo

Mỗi quý một thư mục; trong đó tách ghi chép, bài tập và project.

```text
.
├── README.md
├── q1-foundations/
│   ├── notes/        # Ghi chép theo chủ đề
│   ├── exercises/    # Bài tập giải thuật
│   └── project/      # Project cuối quý
├── q2-backend/
├── q3-cloud-devops/
├── q4-ai-engineering/
└── resources.md      # Danh sách tài liệu đã đọc, kèm ngày đọc
```

Các thư mục được tạo khi bắt đầu giai đoạn tương ứng.

## 4. Quy ước làm việc

- Ghi chép viết bằng tiếng Việt; code, tên file và tên nhánh viết bằng tiếng Anh.
- Commit message theo Conventional Commits, ví dụ `feat(q2): add user login API` hoặc `docs(q1): add notes on TCP handshake`.
- Mỗi project có README riêng gồm: mục đích, cách chạy, cách test, các quyết định thiết kế chính.
- Cuối mỗi quý, cập nhật bảng tiến độ ở mục 7 và viết một bản tự đánh giá ngắn so với mục tiêu ở mục 1.

## 5. Toolkit

Toolkit gom các công cụ dùng trong năm theo nhóm kỹ năng, mỗi nhóm giữ 1–2 công cụ chính. Công cụ phụ thuộc ngôn ngữ chính được chốt sau khi giải quyết mục 8.

### 5.1 Công cụ chung

| Công cụ | Mục đích |
| --- | --- |
| VS Code | Editor chính |
| Linux shell (bash hoặc zsh) | Làm việc với dòng lệnh, viết script tự động hóa |
| Git, GitHub | Quản lý phiên bản, lưu repo học tập |
| Markdown | Viết ghi chép trong `notes/` |

### 5.2 Nền tảng khoa học máy tính

| Công cụ | Mục đích |
| --- | --- |
| Ngôn ngữ chính và runtime | Giải bài tập, viết project; theo lựa chọn ở mục 8 |
| Debugger của ngôn ngữ chính | Theo dõi từng bước thực thi, tìm lỗi |
| `strace`, `htop`, `tcpdump` | Quan sát tiến trình, bộ nhớ và gói tin khi học hệ điều hành và mạng |

### 5.3 Backend và dữ liệu

| Công cụ | Mục đích |
| --- | --- |
| PostgreSQL | Database quan hệ chính |
| Redis | Cache và message queue đơn giản |
| OpenAPI, Bruno | Đặc tả và gọi thử API |
| Test framework của ngôn ngữ chính | Unit test, integration test; theo lựa chọn ở mục 8 |

### 5.4 Cloud, DevOps và bảo mật

| Công cụ | Mục đích |
| --- | --- |
| Docker, Docker Compose | Đóng gói và chạy service cục bộ |
| Kubernetes (kind) | Chạy cluster cục bộ để học deploy và scale |
| Terraform | Khai báo hạ tầng cloud bằng code |
| GitHub Actions | Pipeline CI/CD |
| Prometheus, Grafana | Thu thập metrics, dựng dashboard và cảnh báo |
| Trivy | Quét lỗ hổng trong image và dependency |

### 5.5 AI engineering

| Công cụ | Mục đích |
| --- | --- |
| Claude Code | AI coding assistant dùng xuyên suốt năm |
| Claude API | Gọi LLM trong project, thử tool use và structured output |
| pgvector | Lưu embedding trên PostgreSQL cho RAG |
| MCP SDK | Viết MCP server cho agent |

## 6. Tài liệu tham khảo

| Chủ đề | Tài liệu |
| --- | --- |
| Lộ trình tổng quan | [roadmap.sh](https://roadmap.sh) |
| Nhập môn khoa học máy tính | [CS50 (Harvard)](https://cs50.harvard.edu/x/) |
| Công cụ dòng lệnh, Git | [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/) |
| Giải thuật | [NeetCode](https://neetcode.io), sách *Introduction to Algorithms* (CLRS) |
| Hệ điều hành | [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| Hệ thống dữ liệu | Sách *Designing Data-Intensive Applications*, Martin Kleppmann |
| System design | [System Design Primer](https://github.com/donnemartin/system-design-primer) |
| Bảo mật ứng dụng | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| AI engineering | Sách *AI Engineering*, Chip Huyen |

## 7. Tiến độ

- [ ] Q1: Nền tảng khoa học máy tính
- [ ] Q2: Backend và system design
- [ ] Q3: Cloud, DevOps và bảo mật
- [ ] Q4: AI engineering

## 8. Vấn đề mở

- [ ] Chọn ngôn ngữ lập trình chính cho cả năm (ví dụ Go, Java, Python hay TypeScript). Người quyết định: chủ repo.
- [ ] Xác định số giờ học mỗi tuần để kiểm tra các ngưỡng ở mục 1 có khả thi không. Người quyết định: chủ repo.
- [ ] Chọn nhà cung cấp cloud cho quý 3 (AWS, GCP hay Azure), tính cả chi phí free tier. Người quyết định: chủ repo.
