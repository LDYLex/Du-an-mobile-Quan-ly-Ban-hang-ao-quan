from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import date
class NguoiDungCreate(BaseModel):
    email: EmailStr
    mat_khau: str
    ho_va_ten: str
    so_dien_thoai: Optional[str] = None

# Schema trả về cho Client (Ẩn mật khẩu)
class NguoiDungResponse(BaseModel):
    ma_nguoi_dung: int
    email: EmailStr
    ho_va_ten: str
    so_dien_thoai: Optional[str] = None
    gioi_tinh: Optional[int] = None
    ngay_sinh: Optional[date] = None
# Schema cho dữ liệu Đăng nhập gửi lên
class LoginRequest(BaseModel):
    email: EmailStr
    mat_khau: str

# Schema trả về cho Client khi đăng nhập thành công
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    vai_tro: str  # Ví dụ: "CUSTOMER", "STAFF", "ADMIN"
    ho_va_ten: Optional[str] = None