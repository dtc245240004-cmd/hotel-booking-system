# Hotel Booking System

Hệ thống đặt phòng khách sạn được triển khai trên Ubuntu bằng Docker Compose.

## 1. Kiến trúc hệ thống

Các thành phần chính:

- Django: Web application
- PostgreSQL 16: Database
- pgAdmin: Quản trị PostgreSQL
- Nginx: Reverse Proxy và HTTPS
- Prometheus: Thu thập metrics
- Grafana: Dashboard giám sát
- Node Exporter: Giám sát tài nguyên máy chủ
- PostgreSQL Exporter: Giám sát PostgreSQL
- Loki: Lưu trữ tập trung log
- Promtail: Thu thập log Docker và gửi đến Loki

## 2. Các cổng dịch vụ

| Service | Port | Chức năng |
|---|---:|---|
| Nginx HTTP | 80 | HTTP |
| Nginx HTTPS | 443 | HTTPS |
| Django | 8000 | Web application |
| Grafana | 3000 | Monitoring dashboard |
| Prometheus | 9090 | Metrics |
| Loki | 3100 | Centralized logging |
| Node Exporter | 9100 | Server metrics |
| PostgreSQL Exporter | 9187 | PostgreSQL metrics |
| pgAdmin | 5050 | Database management |

## 3. Khởi động hệ thống

```bash
cd ~/hotel-booking-system
docker compose up -d
