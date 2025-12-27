import os
import shutil
import time
import subprocess
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
# Danh sách package: zam.delta.vn1 -> zam.delta.vn4
PACKAGES = [f"zam.delta.vn{i}" for i in range(1, 5)] 
GAME_URL = "https://www.roblox.com/vi/games/2753915549/Blox-Fruits"

def log(text):
    print(f"\033[92m[AUTO]\033[0m {text}") # In chữ màu xanh lá

def error(text):
    print(f"\033[91m[ERROR]\033[0m {text}") # In chữ màu đỏ

def check_permission():
    # Kiểm tra quyền truy cập bộ nhớ
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Vui lòng chạy lệnh: termux-setup-storage")
        sys.exit(1)

def copy_scripts():
    log("Đang kiểm tra thư mục Scripts...")
    if not os.path.exists(SOURCE_PATH):
        error(f"Thư mục nguồn không tồn tại: {SOURCE_PATH}")
        return

    if not os.path.exists(DEST_PATH):
        try:
            os.makedirs(DEST_PATH)
            log(f"Đã tạo thư mục: {DEST_PATH}")
        except Exception as e:
            error(f"Không thể tạo thư mục: {e}")
            return

    files = os.listdir(SOURCE_PATH)
    count = 0
    for filename in files:
        src = os.path.join(SOURCE_PATH, filename)
        dst = os.path.join(DEST_PATH, filename)
        if os.path.isfile(src):
            try:
                shutil.copy2(src, dst)
                count += 1
            except Exception as e:
                error(f"Lỗi copy {filename}: {e}")
    log(f"Đã copy thành công {count} file vào Autoexecute.")

def open_apps():
    log("Đang mở các ứng dụng Delta...")
    null_file = open(os.devnull, 'w')
    
    for pkg in PACKAGES:
        log(f"-> Đang mở: {pkg}")
        # Dùng monkey để kích hoạt app
        cmd = f"monkey -p {pkg} -c android.intent.category.LAUNCHER 1"
        subprocess.call(cmd, shell=True, stdout=null_file, stderr=null_file)
        # Nghỉ 3 giây giữa các lần mở để tránh lag máy
        time.sleep(3)
    
    null_file.close()

def join_game():
    log("Đang kích hoạt link tham gia game...")
    try:
        subprocess.call(f'termux-open-url "{GAME_URL}"', shell=True)
        log("Đã gửi yêu cầu mở link thành công.")
    except Exception as e:
        error(f"Không thể mở link: {e}")

def main():
    print("\n" + "="*30)
    print("   DELTA AUTO LAUNCHER   ")
    print("="*30 + "\n")
    
    check_permission()
    copy_scripts()
    open_apps()
    join_game()
    
    print("\n" + "="*30)
    log("HOÀN TẤT QUÁ TRÌNH!")

if __name__ == "__main__":
    main()
