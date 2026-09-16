"# Du-an-mobile-Quan-ly-Ban-hang-ao-quan" 
## BE (Làm các api của phần mềm)
-- Database: Mysql 
-- Framwork: fastApi
-- Thuvien: SqlAlchemy,

 Tính năng: 
 
Nhóm Tính năng Dành cho Khách hàng (Customer Features)
Phần này mô tả các chức năng cốt lõi phục vụ trải nghiệm mua sắm của khách hàng tích hợp với hệ thống API Backend:

1. Xác thực người dùng (Authentication)
Đăng ký tài khoản (Sign Up): Cho phép khách hàng mới tạo tài khoản bằng cách cung cấp thông tin cá nhân. Backend FastAPI tiếp nhận, mã hóa mật khẩu bảo mật và lưu vào MySQL.

Đăng nhập hệ thống (Sign In): Khách hàng đăng nhập để truy cập các tính năng mua sắm và quản lý đơn hàng cá nhân thông qua cơ chế xác thực Token.

2. Quản lý Sản phẩm & Giỏ hàng (Product Management)
Xem danh sách áo quần: Hiển thị danh sách sản phẩm áo, quần với hình ảnh, giá cả lên giao diện trang chủ. Khách hàng có thể nhấn vào để xem chi tiết.

Thêm áo quần vào giỏ hàng: Chọn số lượng, size và thêm sản phẩm vào danh sách mua sắm tạm thời.

Sửa số lượng / Cập nhật: Thay đổi số lượng hoặc size của áo, quần đã chọn trước khi thanh toán.

Xóa áo quần: Xóa bớt các món đồ không muốn mua ra khỏi giỏ hàng.

3. Quản lý Hóa đơn & Đơn hàng (Order Management)
Tạo hóa đơn / Đặt hàng: Khách hàng xác nhận thanh toán giỏ hàng, hệ thống tạo hóa đơn mới lưu trạng thái chờ xử lý trên cơ sở dữ liệu.

Hủy hóa đơn / Đơn hàng: Cho phép khách hàng chủ động hủy đơn hàng trong trường hợp cửa hàng chưa xử lý/giao vận. Hệ thống tự động hoàn lại số lượng tồn kho tương ứng.