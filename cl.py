import os
import shutil
import time
import subprocess
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "https://www.roblox.com/vi/games/2753915549/Blox-Fruits"

# Từ khóa để tìm package (Ví dụ máy bạn tên là com.roblox.client thì sửa thành 'roblox')
KEYWORD_SEARCH = "delta" 

def log(text):
    print(f"\033[92m[AUTO]\033[0m {text}")

def error(text):
    print(f"\033[91m[ERROR]\033[0m {text}")

def check_permission():
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Chạy: termux-setup-storage")
        sys.exit(1)

def find_packages():
    log(f"Đang quét các ứng dụng có tên chứa chữ '{KEYWORD_SEARCH}'...")
    try:
        # Lấy danh sách tất cả ứng dụng trong máy
        cmd = "pm list packages"
        output = subprocess.getoutput(cmd)
        
        # Lọc ra các package có chứa từ khóa (ví dụ: delta)
        found_packages = []
        for line in output.splitlines():
            if KEYWORD_SEARCH in line:
                # Dòng kết quả thường là 'package:zam.delta.vn1', cần cắt bỏ chữ 'package:'
                pkg_name = line.replace("package:", "").strip()
                found_packages.append(pkg_name)
        
        if not found_packages:
            error(f"Không tìm thấy ứng dụng nào có tên chứa '{KEYWORD_SEARCH}' trong máy!")
            error("Gợi ý: Hãy kiểm tra lại xem app tên là gì (ví dụ: 'roblox' hay 'delta').")
            return []
            
        log(f"Đã tìm thấy {len(found_packages)} ứng dụng: {found_packages}")
        return found_packages
    except Exception as e:
        error(f"Lỗi khi quét ứng dụng: {e}")
        return []

def open_apps_verbose(packages):
    log("Đang thử mở các ứng dụng...")
    
    for pkg in packages:
        print(f"\n--- Đang mở: {pkg} ---")
        # Lệnh monkey đơn giản nhất, hiển thị kết quả ra màn hình
        cmd = f"monkey -p {pkg} 1"
        
        # Chạy và lấy kết quả trả về
        result = subprocess.getoutput(cmd)
        
        if "No activities found" in result:
            error(f"Lỗi: Không tìm thấy app {pkg} (Sai tên package?)")
        elif "monkey aborted" in result:
            error(f"Lỗi: Hệ thống chặn mở app {pkg}.")
        elif "Events injected: 1" in result:
            log(f"-> Thành công: Đã gửi lệnh mở {pkg}")
        else:
            # In toàn bộ lỗi lạ để bạn đọc
            print(result) 
            
        time.sleep(2)

def main():
    check_permission()
    
    # Bước 1: Copy file (Giữ nguyên như cũ)
    # (Tôi rút gọn đoạn này để tập trung vào lỗi mở app)
    # ...
    
    # Bước 2: Tự động tìm đúng tên Package
    real_packages = find_packages()
    
    if real_packages:
        # Bước 3: Thử mở và hiện lỗi
        open_apps_verbose(real_packages)
    else:
        log("Bỏ qua bước mở App vì không tìm thấy Package.")

    # Bước 4: Mở link (Cái này bạn bảo đã chạy tốt)
    log("Đang mở link game...")
    os.system(f'termux-open-url "{GAME_URL}"')

if __name__ == "__main__":
    main()
