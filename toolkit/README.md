# Toolkit

Thư mục này gom các công cụ dùng trong roadmap, chia theo đúng bảy nhóm kỹ năng ở [README chính](../README.md#3-nhóm-kỹ-năng). Mỗi nhóm giữ 1–2 công cụ chính để tránh dàn trải. Công cụ phụ thuộc ngôn ngữ chính được chốt sau khi giải quyết mục "Vấn đề mở" của README chính. Các link trang chính thức được kiểm tra ngày 26/11/2026.

## 1. Cách dùng thư mục

Ghi chú về từng công cụ được viết dần trong quá trình học, không viết trước.

- Bảng ở mục 2 là danh sách công cụ của roadmap. Thêm, bớt hoặc thay công cụ thì sửa bảng này trước.
- Ghi chú cách dùng một công cụ đặt trong `notes/<tool>.md`, ví dụ `notes/docker.md`. File được tạo khi bắt đầu dùng công cụ đó.
- File cấu hình dùng lại được (dotfiles, cấu hình editor, Docker Compose mẫu) đặt trong `configs/`.
- Danh sách ở mục 3 dùng để đánh dấu môi trường đã cài xong.

```text
toolkit/
├── README.md     # Danh sách công cụ và checklist cài đặt
├── notes/        # Ghi chú cách dùng từng công cụ
└── configs/      # File cấu hình dùng lại được
```

## 2. Danh sách công cụ

Mỗi bảng ứng với một nhóm kỹ năng; cột cuối trỏ tới trang tài liệu chính thức để cài đặt và tra cứu.

### 2.1 Xuyên suốt

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| VS Code | Editor chính | [code.visualstudio.com](https://code.visualstudio.com) |
| Git | Quản lý phiên bản | [git-scm.com](https://git-scm.com) |
| GitHub | Lưu repo, pull request, review | [docs.github.com](https://docs.github.com) |
| Claude Code | AI coding assistant | [Claude Code docs](https://docs.claude.com/en/docs/claude-code/overview) |

### 2.2 Nền tảng khoa học máy tính

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| `strace` | Theo dõi system call của tiến trình | [strace.io](https://strace.io) |
| `htop` | Quan sát CPU, bộ nhớ và tiến trình | [htop.dev](https://htop.dev) |
| `tcpdump` | Bắt và đọc gói tin mạng | [tcpdump.org](https://www.tcpdump.org) |

### 2.3 Ngôn ngữ và kỹ thuật lập trình

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| Ngôn ngữ chính và runtime | Viết code cho mọi project | Chốt sau khi chọn ngôn ngữ |
| Debugger | Theo dõi từng bước thực thi, tìm lỗi | Chốt sau khi chọn ngôn ngữ |
| Test framework | Unit test, integration test | Chốt sau khi chọn ngôn ngữ |

### 2.4 Backend và dữ liệu

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| PostgreSQL | Database quan hệ chính | [postgresql.org](https://www.postgresql.org) |
| Redis | Cache và message queue đơn giản | [redis.io](https://redis.io) |
| OpenAPI | Đặc tả API | [openapis.org](https://www.openapis.org) |
| Bruno | Gọi thử API, lưu bộ request trong repo | [usebruno.com](https://www.usebruno.com) |

### 2.5 System design

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| Excalidraw | Vẽ sơ đồ kiến trúc nhanh | [excalidraw.com](https://excalidraw.com) |
| Mermaid | Vẽ sơ đồ bằng text, đặt ngay trong Markdown | [mermaid.js.org](https://mermaid.js.org) |

### 2.6 Cloud và DevOps

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| Docker, Docker Compose | Đóng gói và chạy service cục bộ | [docs.docker.com](https://docs.docker.com) |
| kind | Chạy cluster Kubernetes cục bộ | [kind.sigs.k8s.io](https://kind.sigs.k8s.io) |
| Terraform | Khai báo hạ tầng cloud bằng code | [developer.hashicorp.com/terraform](https://developer.hashicorp.com/terraform) |
| GitHub Actions | Pipeline CI/CD | [GitHub Actions docs](https://docs.github.com/en/actions) |
| Prometheus | Thu thập metrics và cảnh báo | [prometheus.io](https://prometheus.io) |
| Grafana | Dựng dashboard | [grafana.com](https://grafana.com) |

### 2.7 Bảo mật ứng dụng

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| Trivy | Quét lỗ hổng container image và dependency | [trivy.dev](https://trivy.dev) |
| OWASP ZAP | Quét lỗ hổng ứng dụng web đang chạy | [zaproxy.org](https://www.zaproxy.org) |

### 2.8 AI engineering

| Công cụ | Mục đích | Trang chính thức |
| --- | --- | --- |
| Claude API | Gọi LLM, thử tool use và structured output | [Claude API docs](https://docs.claude.com/en/api/overview) |
| pgvector | Lưu và tìm embedding trên PostgreSQL cho RAG | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| MCP SDK | Viết MCP server cho agent | [modelcontextprotocol.io](https://modelcontextprotocol.io) |

## 3. Checklist cài đặt

Đánh dấu khi công cụ đã cài và chạy được lệnh kiểm tra phiên bản. Cài theo nhóm đang học, không cần cài hết từ đầu.

- [ ] Xuyên suốt: VS Code, Git, tài khoản GitHub, Claude Code
- [ ] Nền tảng: `strace`, `htop`, `tcpdump`
- [ ] Lập trình: ngôn ngữ chính, debugger, test framework
- [ ] Backend: PostgreSQL, Redis, Bruno
- [ ] System design: tài khoản hoặc bản cài Excalidraw
- [ ] Cloud và DevOps: Docker, kind, Terraform, `kubectl`
- [ ] Bảo mật: Trivy, OWASP ZAP
- [ ] AI engineering: API key Claude, extension pgvector, MCP SDK
