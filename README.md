# Learning Software Engineer 2027

Repo này tổng hợp các nhóm kỹ năng mà một kỹ sư phần mềm cần nắm vững cho năm 2027, trình bày dưới dạng roadmap tự học. Nền tảng khoa học máy tính và backend vẫn là phần cốt lõi. Bên cạnh đó, roadmap đưa vào các kỹ năng được kỳ vọng ngày càng nhiều: vận hành trên cloud, bảo mật ứng dụng, xây ứng dụng có dùng LLM và làm việc cùng AI coding assistant. Mỗi nhóm có kiến thức tiên quyết, danh sách nội dung để đánh dấu tiến độ và một project. Các project nối tiếp nhau trên cùng một sản phẩm, nên khi đi hết lộ trình, repo có một hệ thống chạy được kèm ghi chép, đủ dùng làm portfolio khi phỏng vấn.

## 1. Sơ đồ roadmap

Học từ trên xuống theo đường nối trong Hình 1. Sau nhóm 3, ba nhóm 4, 5 và 6 có thể học song song; khối "Xuyên suốt" được áp dụng ở mọi nhóm.

<p align="center">
  <img src="assets/roadmap.svg" alt="Roadmap bảy nhóm kỹ năng kỹ sư phần mềm 2027" width="100%">
</p>

Hình 1. Roadmap bảy nhóm kỹ năng. Màu xanh dương là nền tảng, xanh lá là lõi backend, tím là các nhóm học song song, cam là AI engineering.

Sơ đồ được sinh bằng script [scripts/gen_roadmap.py](scripts/gen_roadmap.py), chỉ dùng thư viện chuẩn của Python 3. Để thêm hoặc đổi chủ đề, sửa danh sách trong script rồi chạy lại:

```bash
python3 scripts/gen_roadmap.py
```

## 2. Mục tiêu

Mỗi mục tiêu gắn với một nhóm kỹ năng và có ngưỡng đạt để tự kiểm khi hoàn thành nhóm đó.

| Mã | Nhóm | Mục tiêu | Ngưỡng đạt |
| --- | --- | --- | --- |
| G1 | 1 | Nắm vững cấu trúc dữ liệu và giải thuật | 150 bài tập có lời giải và phân tích độ phức tạp trong `01-cs-foundations/exercises/` |
| G2 | 2, 3 | Xây được một backend service hoàn chỉnh | Có API, database, test tự động, CI chạy xanh, test coverage từ 70% |
| G3 | 4 | Phân tích được thiết kế hệ thống | 5 bản thiết kế, mỗi bản có sơ đồ và bảng đánh đổi giữa các phương án |
| G4 | 5 | Deploy và vận hành service trên cloud | Service chạy trên cloud, có dashboard monitoring và ít nhất 1 runbook xử lý sự cố |
| G5 | 6 | Bảo vệ được service đã xây | Không còn lỗ hổng mức HIGH hoặc CRITICAL khi quét bằng Trivy; đã rà theo OWASP Top 10 |
| G6 | 7 | Xây tính năng có dùng LLM | Tính năng RAG hoặc agent chạy trong service, kèm bộ eval tự động từ 50 case |
| G7 | Xuyên suốt | Duy trì thói quen học đều | Ít nhất 1 commit ghi chép hoặc code mỗi tuần trong suốt lộ trình |

## 3. Nhóm kỹ năng

Mỗi nhóm gồm kiến thức tiên quyết, roadmap tham khảo trên [roadmap.sh](https://roadmap.sh), nội dung cần học và project. Roadmap trên roadmap.sh chi tiết hơn nội dung ở đây; dùng chúng để tra cứu khi cần học sâu một chủ đề. Các link được kiểm tra ngày 26/11/2026. Đánh dấu ô chọn khi đã học xong và có ghi chép trong repo.

### 3.1 Nền tảng khoa học máy tính

Tiên quyết: không có.

Roadmap tham khảo: [Computer Science](https://roadmap.sh/computer-science), [Data Structures & Algorithms](https://roadmap.sh/datastructures-and-algorithms), [Linux](https://roadmap.sh/linux).

- [ ] Cấu trúc dữ liệu: mảng, danh sách liên kết, stack, queue, hash table, cây, heap, đồ thị
- [ ] Giải thuật: sắp xếp, tìm kiếm, đệ quy, quy hoạch động, duyệt đồ thị
- [ ] Phân tích độ phức tạp thời gian và bộ nhớ
- [ ] Hệ điều hành: tiến trình, luồng, bộ nhớ ảo, hệ thống file, đồng bộ hóa
- [ ] Mạng máy tính: mô hình TCP/IP, HTTP/HTTPS, DNS, TLS

Project: một công cụ dòng lệnh (CLI) phân tích log, có test. Project này là điểm khởi đầu của sản phẩm xuyên suốt.

### 3.2 Ngôn ngữ và kỹ thuật lập trình

Tiên quyết: nhóm 1.

Roadmap tham khảo: [Go](https://roadmap.sh/golang), [Java](https://roadmap.sh/java), [Python](https://roadmap.sh/python) hoặc [TypeScript](https://roadmap.sh/typescript) tùy ngôn ngữ chính; [Software Design & Architecture](https://roadmap.sh/software-design-architecture), [Code Review](https://roadmap.sh/code-review), [QA](https://roadmap.sh/qa).

- [ ] Ngôn ngữ chính: cú pháp, hệ thống kiểu, xử lý lỗi, concurrency, quản lý package (xem mục 8)
- [ ] Clean code và refactoring
- [ ] Design pattern thường gặp
- [ ] Kiểm thử: unit test, integration test, test pyramid, mock

Project: viết lại CLI ở nhóm 1 bằng ngôn ngữ chính theo cấu trúc module rõ ràng, test coverage từ 70%.

### 3.3 Backend và dữ liệu

Tiên quyết: nhóm 2.

Roadmap tham khảo: [Backend](https://roadmap.sh/backend), [API Design](https://roadmap.sh/api-design), [SQL](https://roadmap.sh/sql), [PostgreSQL](https://roadmap.sh/postgresql-dba), [Redis](https://roadmap.sh/redis), [MongoDB](https://roadmap.sh/mongodb).

- [ ] Thiết kế API: REST, GraphQL, phân trang, versioning, xử lý lỗi
- [ ] SQL: mô hình dữ liệu, chỉ mục, transaction, mức cô lập
- [ ] Một hệ NoSQL để so sánh với SQL
- [ ] Cache và message queue
- [ ] Xác thực người dùng ở mức cơ bản

Project: chuyển CLI thành backend service có API, database và CI.

### 3.4 System design

Tiên quyết: nhóm 3.

Roadmap tham khảo: [System Design](https://roadmap.sh/system-design), [Software Architect](https://roadmap.sh/software-architect).

- [ ] Khả năng mở rộng: scale dọc, scale ngang, cân bằng tải
- [ ] Dữ liệu phân tán: replication, partitioning, định lý CAP
- [ ] Tính nhất quán và xử lý lỗi: idempotency, retry, circuit breaker
- [ ] Ghi lại quyết định kiến trúc theo dạng Architecture Decision Record (ADR)

Project: 5 bản thiết kế cho các bài toán quen thuộc (rút gọn URL, chat, news feed, rate limiter, hệ thống thông báo), trong đó có một bản cho chính service ở nhóm 3.

### 3.5 Cloud và DevOps

Tiên quyết: nhóm 3.

Roadmap tham khảo: [DevOps](https://roadmap.sh/devops), [Docker](https://roadmap.sh/docker), [Kubernetes](https://roadmap.sh/kubernetes), [Terraform](https://roadmap.sh/terraform), [AWS](https://roadmap.sh/aws).

- [ ] Container: Docker, Docker Compose
- [ ] Kubernetes ở mức deploy, scale và cấu hình
- [ ] Infrastructure as Code (IaC) với Terraform
- [ ] CI/CD: build, test, deploy, rollback
- [ ] Observability: metrics, log, tracing, cảnh báo

Project: deploy service lên cloud, kèm dashboard monitoring và runbook.

### 3.6 Bảo mật ứng dụng

Tiên quyết: nhóm 3.

Roadmap tham khảo: [Cyber Security](https://roadmap.sh/cyber-security), [API Security Best Practices](https://roadmap.sh/api-security-best-practices).

- [ ] OWASP Top 10
- [ ] Xác thực và phân quyền: OAuth 2.0, OpenID Connect, JWT
- [ ] Quản lý secret và cấu hình
- [ ] Quét lỗ hổng dependency và container image

Project: rà soát bảo mật service, sửa lỗ hổng tìm được và ghi lại kết quả.

### 3.7 AI engineering

Tiên quyết: nhóm 3; nên xong nhóm 5 để deploy được.

Roadmap tham khảo: [AI Engineer](https://roadmap.sh/ai-engineer), [AI Agents](https://roadmap.sh/ai-agents), [Prompt Engineering](https://roadmap.sh/prompt-engineering), [MLOps](https://roadmap.sh/mlops).

- [ ] Nền tảng LLM: token, context window, prompt, structured output, tool use
- [ ] Retrieval-Augmented Generation (RAG): embedding, vector database, chunking, reranking
- [ ] Agent: vòng lặp tool use, Model Context Protocol (MCP), giới hạn chi phí và xử lý lỗi
- [ ] Eval: xây bộ eval, so sánh phiên bản prompt và model

Project: thêm tính năng hỏi đáp trên log bằng RAG hoặc agent vào service, kèm bộ eval.

### 3.8 Kỹ năng xuyên suốt

Các kỹ năng này không có thời điểm học riêng mà được dùng trong mọi nhóm.

Roadmap tham khảo: [Git and GitHub](https://roadmap.sh/git-github), [Linux](https://roadmap.sh/linux).

- [ ] Git: branch, rebase, giải quyết xung đột, pull request
- [ ] Linux shell và viết script tự động hóa
- [ ] Làm việc với AI coding assistant: viết đặc tả rõ, review code do AI sinh, giữ chất lượng test
- [ ] Ghi chép sau mỗi chủ đề và tự đánh giá sau mỗi nhóm

Capstone ở cuối lộ trình: tổng hợp sản phẩm qua bảy nhóm thành một bản demo, kèm bài viết mô tả kiến trúc và các bài học rút ra.

## 4. Toolkit

Danh sách công cụ đầy đủ nằm trong thư mục [toolkit/](toolkit/), chia theo đúng bảy nhóm kỹ năng ở mục 3. Mỗi công cụ kèm mục đích và link tài liệu chính thức. Thư mục này cũng chứa checklist cài đặt môi trường, ghi chú cách dùng từng công cụ (`toolkit/notes/`) và file cấu hình dùng lại được (`toolkit/configs/`).

Công cụ chính theo nhóm: VS Code, Git, Claude Code và GitNexus dùng xuyên suốt; PostgreSQL và Redis cho backend; Docker, kind, Terraform và GitHub Actions cho cloud và DevOps; Trivy cho bảo mật; Claude API, pgvector và MCP SDK cho AI engineering.

Công cụ cần học sâu có khóa training riêng trong thư mục [training/](training/). Khóa đầu tiên là [GitNexus](training/gitnexus/): index codebase thành knowledge graph, đánh giá tác động trước khi sửa code, review pull request và tích hợp vào workflow cùng AI coding assistant.

## 5. Cấu trúc repo

Mỗi nhóm kỹ năng một thư mục, đánh số theo sơ đồ ở mục 1. Thư mục được tạo khi bắt đầu nhóm tương ứng.

```text
.
├── README.md
├── assets/           # Ảnh dùng trong README (roadmap.svg)
├── scripts/          # Script sinh sơ đồ roadmap
├── toolkit/          # Danh sách công cụ, checklist cài đặt, ghi chú
├── training/         # Khóa học chuyên sâu cho từng công cụ (GitNexus, ...)
├── 01-cs-foundations/
│   ├── notes/        # Ghi chép theo chủ đề
│   ├── exercises/    # Bài tập
│   └── project/      # Project của nhóm
├── 02-programming/
├── 03-backend-data/
├── 04-system-design/
├── 05-cloud-devops/
├── 06-security/
├── 07-ai-engineering/
├── capstone/
└── resources.md      # Tài liệu đã đọc, kèm ngày đọc
```

## 6. Quy ước làm việc

- Ghi chép viết bằng tiếng Việt; code, tên file và tên nhánh viết bằng tiếng Anh.
- Commit message theo Conventional Commits, scope là tên thư mục nhóm, ví dụ `feat(03-backend-data): add user login API`.
- Mỗi project có README riêng gồm: mục đích, cách chạy, cách test, các quyết định thiết kế chính.
- Xong mỗi nhóm, đánh dấu ô chọn ở mục 3 và viết một bản tự đánh giá ngắn so với mục tiêu ở mục 2.

## 7. Tài liệu tham khảo

| Nhóm | Tài liệu |
| --- | --- |
| Tổng quan | [roadmap.sh](https://roadmap.sh), [Full Stack](https://roadmap.sh/full-stack); roadmap theo từng nhóm được gắn ở mục 3 |
| 1. Nền tảng | [CS50 (Harvard)](https://cs50.harvard.edu/x/), [NeetCode](https://neetcode.io), [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| Xuyên suốt | [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/) |
| 3, 4. Backend và system design | Sách *Designing Data-Intensive Applications*, Martin Kleppmann; [System Design Primer](https://github.com/donnemartin/system-design-primer) |
| 6. Bảo mật | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| 7. AI engineering | Sách *AI Engineering*, Chip Huyen |

## 8. Vấn đề mở

- [ ] Chọn ngôn ngữ lập trình chính cho toàn bộ lộ trình (ví dụ Go, Java, Python hay TypeScript). Người quyết định: chủ repo.
- [ ] Xác định số giờ học mỗi tuần để kiểm tra các ngưỡng ở mục 2 có khả thi không. Người quyết định: chủ repo.
- [ ] Chọn nhà cung cấp cloud cho nhóm 5 (AWS, GCP hay Azure), tính cả chi phí free tier. Người quyết định: chủ repo.
