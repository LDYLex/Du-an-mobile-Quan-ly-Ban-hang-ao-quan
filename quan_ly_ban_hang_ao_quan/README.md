# quan_ly_ban_hang_ao_quan

Ứng dụng di động quản lý bán hàng quần áo được xây dựng bằng Flutter theo mô hình **MVVM (Model - View - ViewModel)**.

## 📁 Tổ chức cấu trúc thư mục (Layer-First)

Dự án được phân chia theo các tầng kỹ thuật chính bên trong thư mục `lib/`:

```text
lib/
├── models/           # Chứa các data class (định nghĩa cấu trúc dữ liệu và hàm fromJson/toJson)
│   ├── product_model.dart
│   ├── order_model.dart
│   └── user_model.dart
│
├── viewmodels/       # Chứa logic xử lý nghiệp vụ và quản lý trạng thái giao diện (State Management)
│   ├── product_viewmodel.dart
│   └── order_viewmodel.dart
│
├── views/            # Chứa giao diện người dùng (UI)
│   ├── screens/      # Các màn hình chính của ứng dụng
│   │   ├── login_screen.dart
│   │   ├── product_list_screen.dart
│   │   └── order_screen.dart
│   └── widgets/      # Các thành phần giao diện nhỏ tái sử dụng chung
│       └── custom_button.dart
│
├── services/         # Xử lý các tác vụ nền tảng (Gọi API, kết nối cơ sở dữ liệu local)
│   └── api_service.dart
│
└── utils/            # Các tiện ích chung (Hằng số màu sắc, định dạng tiền tệ, xử lý lỗi)
    └── app_colors.dart