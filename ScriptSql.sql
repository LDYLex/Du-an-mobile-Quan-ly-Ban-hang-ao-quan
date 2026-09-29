-- 1. Tạo Database và chọn sử dụng
CREATE DATABASE IF NOT EXISTS `quan_ly_ban_hang` 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE `quan_ly_ban_hang`;

-- 2. Bảng nguoi_dung (Tài khoản người dùng)
CREATE TABLE `nguoi_dung` (
  `ma_nguoi_dung` INT AUTO_INCREMENT PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `so_dien_thoai` VARCHAR(20) UNIQUE NULL,
  `mat_khau_ma_hoa` VARCHAR(255) NOT NULL,
  `ho_va_ten` VARCHAR(100) NOT NULL,
  `vai_tro` ENUM('ADMIN', 'STAFF', 'CUSTOMER') NOT NULL DEFAULT 'CUSTOMER', -- Thêm cột này
  `gioi_tinh` TINYINT NULL COMMENT '0: Nữ, 1: Nam, 2: Khác',
  `ngay_sinh` DATE NULL
) ENGINE=InnoDB;

-- 3. Bảng danh_muc (Danh mục sản phẩm)
CREATE TABLE `danh_muc` (
  `ma_danh_muc` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_danh_muc_cha` INT NULL,
  `ten_danh_muc` VARCHAR(100) NOT NULL,
  `anh_dai_dien` VARCHAR(500) NULL,
  CONSTRAINT `fk_danh_muc_cha` 
    FOREIGN KEY (`ma_danh_muc_cha`) REFERENCES `danh_muc` (`ma_danh_muc`) 
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 4. Bảng san_pham (Sản phẩm gốc)
CREATE TABLE `san_pham` (
  `ma_san_pham` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_danh_muc` INT NOT NULL,
  `ten_san_pham` VARCHAR(255) NOT NULL,
  `gia_ban_niem_yet` DECIMAL(12,2) NOT NULL,
  `mo_ta_chi_tiet` TEXT NULL,
  `anh_bang_quy_doi_size` VARCHAR(500) NULL,
  `ngay_tao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT `fk_san_pham_danh_muc` 
    FOREIGN KEY (`ma_danh_muc`) REFERENCES `danh_muc` (`ma_danh_muc`) 
    ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 5. Bảng anh_san_pham (Bộ ảnh sản phẩm)
CREATE TABLE `anh_san_pham` (
  `ma_anh` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_san_pham` INT NOT NULL,
  `duong_dan_anh` VARCHAR(500) NOT NULL,
  CONSTRAINT `fk_anh_san_pham` 
    FOREIGN KEY (`ma_san_pham`) REFERENCES `san_pham` (`ma_san_pham`) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 6. Bảng bien_the_san_pham (Biến thể sản phẩm - Màu & Size)
CREATE TABLE `bien_the_san_pham` (
  `ma_bien_the` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_san_pham` INT NOT NULL,
  `ten_mau_sac` VARCHAR(50) NOT NULL,
  `kich_co` VARCHAR(20) NOT NULL,
  `so_luong_ton_kho` INT NOT NULL DEFAULT 0,
  CONSTRAINT `fk_bien_the_san_pham` 
    FOREIGN KEY (`ma_san_pham`) REFERENCES `san_pham` (`ma_san_pham`) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 7. Bảng gio_hang (Giỏ hàng)
CREATE TABLE `gio_hang` (
  `ma_gio_hang` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_nguoi_dung` INT UNIQUE NULL,
  `ngay_tao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT `fk_gio_hang_nguoi_dung` 
    FOREIGN KEY (`ma_nguoi_dung`) REFERENCES `nguoi_dung` (`ma_nguoi_dung`) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 8. Bảng chi_tiet_gio_hang (Chi tiết giỏ hàng)
CREATE TABLE `chi_tiet_gio_hang` (
  `ma_chi_tiet_gio_hang` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_gio_hang` INT NOT NULL,
  `ma_bien_the` INT NOT NULL,
  `so_luong` INT NOT NULL CHECK (`so_luong` > 0),
  CONSTRAINT `fk_chi_tiet_gio_hang` 
    FOREIGN KEY (`ma_gio_hang`) REFERENCES `gio_hang` (`ma_gio_hang`) 
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_chi_tiet_gio_hang_bien_the` 
    FOREIGN KEY (`ma_bien_the`) REFERENCES `bien_the_san_pham` (`ma_bien_the`) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 9. Bảng don_hang (Đơn đặt hàng)
CREATE TABLE `don_hang` (
  `ma_don_hang` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_dinh_danh_don` VARCHAR(50) NOT NULL UNIQUE,
  `ma_nguoi_dat` INT NOT NULL,
  `tong_tien_thanh_toan` DECIMAL(12,2) NOT NULL,
  `trang_thai_don_hang` ENUM('PENDING', 'PROCESSING', 'SHIPPING', 'COMPLETED', 'CANCELLED') NOT NULL DEFAULT 'PENDING',
  `phuong_thuc_thanh_toan` VARCHAR(20) NOT NULL,
  `trang_thai_thanh_toan` ENUM('UNPAID', 'PAID', 'REFUNDED') NOT NULL DEFAULT 'UNPAID',
  `ngay_tao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT `fk_don_hang_nguoi_dung` 
    FOREIGN KEY (`ma_nguoi_dat`) REFERENCES `nguoi_dung` (`ma_nguoi_dung`) 
    ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 10. Bảng chi_tiet_don_hang (Chi tiết món trong đơn hàng)
CREATE TABLE `chi_tiet_don_hang` (
  `ma_chi_tiet_don_hang` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_don_hang` INT NOT NULL,
  `ma_bien_the` INT NOT NULL,
  `ten_san_pham_luu_vet` VARCHAR(255) NOT NULL,
  `thuoc_tinh_luu_vet` VARCHAR(100) NOT NULL,
  `don_gia_luu_vet` DECIMAL(12,2) NOT NULL,
  `so_luong_mua` INT NOT NULL CHECK (`so_luong_mua` > 0),
  CONSTRAINT `fk_chi_tiet_don_hang_don_hang` 
    FOREIGN KEY (`ma_don_hang`) REFERENCES `don_hang` (`ma_don_hang`) 
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_chi_tiet_don_hang_bien_the` 
    FOREIGN KEY (`ma_bien_the`) REFERENCES `bien_the_san_pham` (`ma_bien_the`) 
    ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 11. Bảng van_chuyen (Thông tin Vận chuyển & Giao hàng)
CREATE TABLE `van_chuyen` (
  `ma_van_chuyen` INT AUTO_INCREMENT PRIMARY KEY,
  `ma_don_hang` INT NOT NULL UNIQUE,
  `ten_nguoi_nhan` VARCHAR(100) NOT NULL,
  `sdt_nguoi_nhan` VARCHAR(20) NOT NULL,
  `dia_chi_giao_hang` VARCHAR(255) NOT NULL,
  `ten_ben_van_chuyen` VARCHAR(50) NULL,
  `ma_van_don` VARCHAR(100) NULL,
  `thoi_gian_xuat_kho` DATETIME NULL,
  `thoi_gian_giao_thanh_cong` DATETIME NULL,
  CONSTRAINT `fk_van_chuyen_don_hang` 
    FOREIGN KEY (`ma_don_hang`) REFERENCES `don_hang` (`ma_don_hang`) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;