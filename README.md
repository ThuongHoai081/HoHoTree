# HoHoTree
```bash
The application uses AI to analyze images of tomato plants.  
Detect abnormalities on leaves or fruits.  
Provide a diagnosis of common diseases (such as leaf spot, leaf curl, or blight).  
Users simply take a photo of the affected plant with their phone.  
The system returns a result along with suggested treatments.
hohotree_be/                  # Thư mục gốc của backend
│── src/              # Cấu hình chính Django
│   ├── api/                  # API tổng
│   │   ├── __init__.py
│   │   ├── urls.py           # URL API tổng
│   ├── plant_disease/        # Ứng dụng phát hiện bệnh cây trồng
│   │   ├── migrations/       # Database migrations
│   │   ├── ml/               # Chứa model AI
│   │   │   ├── model.pkl     # File model AI đã train
│   │   │   ├── preprocess.py # Xử lý ảnh trước khi đưa vào AI
│   │   │   ├── predict.py    # Hàm chạy AI để phát hiện bệnh
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── services.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   ├── settings/             # Chứa file settings.py
│   │   ├── __init__.py
│   │   ├── local.py          # Cấu hình môi trường local
│   │   ├── production.py     # Cấu hình môi trường production
│   │   ├── common.py         # Cấu hình chung
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py               # Khai báo API endpoints chính
│── media/                    # Lưu trữ ảnh tải lên từ người dùng
│── requirements.txt          # Danh sách thư viện cần cài đặt
│── manage.py                 # Quản lý Django
│── Dockerfile                # Triển khai bằng Docker
│── docker-compose.yml        # Cấu hình Docker Compose
│── .env                      # Biến môi trường
