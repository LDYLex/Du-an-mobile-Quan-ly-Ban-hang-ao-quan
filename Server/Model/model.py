import enum
from datetime import date, datetime
from typing import Optional, List
from decimal import Decimal
from sqlalchemy import (
    String, Text, Integer, SmallInteger, Boolean, Date, DateTime, 
    Numeric, ForeignKey, Enum as SQLEnum, func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Connection.connection import Base  # Import Base class đã tạo ở bước trước


# ==========================================
# 1. Các Enum cho Đơn hàng
# ==========================================
class TrangThaiDonHang(str, enum.Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPING = "SHIPPING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class TrangThaiThanhToan(str, enum.Enum):
    UNPAID = "UNPAID"
    PAID = "PAID"
    REFUNDED = "REFUNDED"
class VaiTro(str, enum.Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"
    CUSTOMER = "CUSTOMER"

# ==========================================
# 2. Bảng NguoiDung
# ==========================================
class NguoiDung(Base):
    __tablename__ = "nguoi_dung"

    ma_nguoi_dung: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    so_dien_thoai: Mapped[Optional[str]] = mapped_column(String(20), unique=True, nullable=True)
    mat_khau_ma_hoa: Mapped[str] = mapped_column(String(255), nullable=False)
    ho_va_ten: Mapped[str] = mapped_column(String(100), nullable=False)
    gioi_tinh: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)  # 0: Nữ, 1: Nam, 2: Khác
    ngay_sinh: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    vai_tro: Mapped[VaiTro] = mapped_column(SQLEnum(VaiTro), default=VaiTro.CUSTOMER, nullable=False)
    # Relationships
    gio_hang: Mapped[Optional["GioHang"]] = relationship("GioHang", back_populates="nguoi_dung", uselist=False)
    don_hangs: Mapped[List["DonHang"]] = relationship("DonHang", back_populates="nguoi_dung")


# ==========================================
# 3. Bảng DanhMuc
# ==========================================
class DanhMuc(Base):
    __tablename__ = "danh_muc"

    ma_danh_muc: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_danh_muc_cha: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("danh_muc.ma_danh_muc", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    ten_danh_muc: Mapped[str] = mapped_column(String(100), nullable=False)
    anh_dai_dien: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Relationships
    danh_muc_cha: Mapped[Optional["DanhMuc"]] = relationship("DanhMuc", remote_side=[ma_danh_muc], backref="danh_muc_con")
    san_phams: Mapped[List["SanPham"]] = relationship("SanPham", back_populates="danh_muc")


# ==========================================
# 4. Bảng SanPham
# ==========================================
class SanPham(Base):
    __tablename__ = "san_pham"

    ma_san_pham: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_danh_muc: Mapped[int] = mapped_column(Integer, ForeignKey("danh_muc.ma_danh_muc", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    ten_san_pham: Mapped[str] = mapped_column(String(255), nullable=False)
    gia_ban_niem_yet: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    mo_ta_chi_tiet: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    anh_bang_quy_doi_size: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    ngay_tao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Relationships
    danh_muc: Mapped["DanhMuc"] = relationship("DanhMuc", back_populates="san_phams")
    anh_san_phams: Mapped[List["AnhSanPham"]] = relationship("AnhSanPham", back_populates="san_pham", cascade="all, delete-orphan")
    bien_thes: Mapped[List["BienTheSanPham"]] = relationship("BienTheSanPham", back_populates="san_pham", cascade="all, delete-orphan")


# ==========================================
# 5. Bảng AnhSanPham
# ==========================================
class AnhSanPham(Base):
    __tablename__ = "anh_san_pham"

    ma_anh: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_san_pham: Mapped[int] = mapped_column(Integer, ForeignKey("san_pham.ma_san_pham", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    duong_dan_anh: Mapped[str] = mapped_column(String(500), nullable=False)

    # Relationships
    san_pham: Mapped["SanPham"] = relationship("SanPham", back_populates="anh_san_phams")


# ==========================================
# 6. Bảng BienTheSanPham
# ==========================================
class BienTheSanPham(Base):
    __tablename__ = "bien_the_san_pham"

    ma_bien_the: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_san_pham: Mapped[int] = mapped_column(Integer, ForeignKey("san_pham.ma_san_pham", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    ten_mau_sac: Mapped[str] = mapped_column(String(50), nullable=False)
    kich_co: Mapped[str] = mapped_column(String(20), nullable=False)
    so_luong_ton_kho: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    san_pham: Mapped["SanPham"] = relationship("SanPham", back_populates="bien_thes")
    chi_tiet_gio_hangs: Mapped[List["ChiTietGioHang"]] = relationship("ChiTietGioHang", back_populates="bien_the")
    chi_tiet_don_hangs: Mapped[List["ChiTietDonHang"]] = relationship("ChiTietDonHang", back_populates="bien_the")


# ==========================================
# 7. Bảng GioHang
# ==========================================
class GioHang(Base):
    __tablename__ = "gio_hang"

    ma_gio_hang: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_nguoi_dung: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("nguoi_dung.ma_nguoi_dung", ondelete="CASCADE", onupdate="CASCADE"), unique=True, nullable=True)
    ngay_tao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Relationships
    nguoi_dung: Mapped[Optional["NguoiDung"]] = relationship("NguoiDung", back_populates="gio_hang")
    chi_tiet_gio_hangs: Mapped[List["ChiTietGioHang"]] = relationship("ChiTietGioHang", back_populates="gio_hang", cascade="all, delete-orphan")


# ==========================================
# 8. Bảng ChiTietGioHang
# ==========================================
class ChiTietGioHang(Base):
    __tablename__ = "chi_tiet_gio_hang"

    ma_chi_tiet_gio_hang: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_gio_hang: Mapped[int] = mapped_column(Integer, ForeignKey("gio_hang.ma_gio_hang", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    ma_bien_the: Mapped[int] = mapped_column(Integer, ForeignKey("bien_the_san_pham.ma_bien_the", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    so_luong: Mapped[int] = mapped_column(Integer, nullable=False)

    # Relationships
    gio_hang: Mapped["GioHang"] = relationship("GioHang", back_populates="chi_tiet_gio_hangs")
    bien_the: Mapped["BienTheSanPham"] = relationship("BienTheSanPham", back_populates="chi_tiet_gio_hangs")


# ==========================================
# 9. Bảng DonHang
# ==========================================
class DonHang(Base):
    __tablename__ = "don_hang"

    ma_don_hang: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_dinh_danh_don: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    ma_nguoi_dat: Mapped[int] = mapped_column(Integer, ForeignKey("nguoi_dung.ma_nguoi_dung", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    tong_tien_thanh_toan: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    trang_thai_don_hang: Mapped[TrangThaiDonHang] = mapped_column(SQLEnum(TrangThaiDonHang), default=TrangThaiDonHang.PENDING, nullable=False)
    phuong_thuc_thanh_toan: Mapped[str] = mapped_column(String(20), nullable=False)
    trang_thai_thanh_toan: Mapped[TrangThaiThanhToan] = mapped_column(SQLEnum(TrangThaiThanhToan), default=TrangThaiThanhToan.UNPAID, nullable=False)
    ngay_tao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Relationships
    nguoi_dung: Mapped["NguoiDung"] = relationship("NguoiDung", back_populates="don_hangs")
    chi_tiet_don_hangs: Mapped[List["ChiTietDonHang"]] = relationship("ChiTietDonHang", back_populates="don_hang", cascade="all, delete-orphan")
    van_chuyen: Mapped[Optional["VanChuyen"]] = relationship("VanChuyen", back_populates="don_hang", uselist=False, cascade="all, delete-orphan")


# ==========================================
# 10. Bảng ChiTietDonHang
# ==========================================
class ChiTietDonHang(Base):
    __tablename__ = "chi_tiet_don_hang"

    ma_chi_tiet_don_hang: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_don_hang: Mapped[int] = mapped_column(Integer, ForeignKey("don_hang.ma_don_hang", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    ma_bien_the: Mapped[int] = mapped_column(Integer, ForeignKey("bien_the_san_pham.ma_bien_the", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    ten_san_pham_luu_vet: Mapped[str] = mapped_column(String(255), nullable=False)
    thuoc_tinh_luu_vet: Mapped[str] = mapped_column(String(100), nullable=False)
    don_gia_luu_vet: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    so_luong_mua: Mapped[int] = mapped_column(Integer, nullable=False)

    # Relationships
    don_hang: Mapped["DonHang"] = relationship("DonHang", back_populates="chi_tiet_don_hangs")
    bien_the: Mapped["BienTheSanPham"] = relationship("BienTheSanPham", back_populates="chi_tiet_don_hangs")


# ==========================================
# 11. Bảng VanChuyen
# ==========================================
class VanChuyen(Base):
    __tablename__ = "van_chuyen"

    ma_van_chuyen: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ma_don_hang: Mapped[int] = mapped_column(Integer, ForeignKey("don_hang.ma_don_hang", ondelete="CASCADE", onupdate="CASCADE"), unique=True, nullable=False)
    ten_nguoi_nhan: Mapped[str] = mapped_column(String(100), nullable=False)
    sdt_nguoi_nhan: Mapped[str] = mapped_column(String(20), nullable=False)
    dia_chi_giao_hang: Mapped[str] = mapped_column(String(255), nullable=False)
    ten_ben_van_chuyen: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    ma_van_don: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    thoi_gian_xuat_kho: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    thoi_gian_giao_thanh_cong: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    # Relationships
    don_hang: Mapped["DonHang"] = relationship("DonHang", back_populates="van_chuyen")