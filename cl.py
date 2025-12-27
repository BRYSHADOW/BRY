import os
import shutil
import time
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"

# Link Deep-link (Giúp vào thẳng game, hạn chế vào Web/CH Play)
GAME_URL = "roblox://placeId=2753915549" 

def log(text):
    print(f"\033[92m[AUTO]\033[0m {text}")

def error(text):
    print(f"\033[91m[ERROR]\033[0m {text}")

def check_permission():
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Chạy: termux-setup-storage")
        sys.exit(1)

def main():
    check_permission()
    
    # 1. COPY FILE (Giữ nguyên phần đã chạy ổn)
    log("Bắt đầu copy scripts...")
    if os.path.exists(SOURCE_PATH):
        if not os.path.exists(DEST_PATH):
            try:
                os.makedirs(DEST_PATH)
            except: pass
        
        count = 0
        try:
            files = os.listdir(SOURCE_PATH)
            for f in files:
                src = os.path.join(SOURCE_PATH, f)
                dst = os.path.join(DEST_PATH, f)
                if os.path.isfile(src):
                    # Dùng copyfile để tránh lỗi Permission
                    shutil.copyfile(src, dst)
                    count += 1
            log(f"Đã copy xong {count} file.")
        except Exception as e:
            error(f"Lỗi khi copy: {e}")
    else:
        log("Không tìm thấy thư mục Scripts (Bỏ qua copy).")

    # 2. MỞ LINK 4 LẦN (Mỗi lần cách nhau 3 giây)
    log("Bắt đầu mở game 4 lần...")
    
    for i in range(1, 5):
        print(f"\n--- Lần mở thứ {i} ---")
        try:
            # Lệnh mở URL của Termux
            os.system(f'termux-open-url "{GAME_URL}"')
            log(f"Đã gửi lệnh mở game.")
        except Exception as e:
            error(f"Lỗi: {e}")
            
        if i < 4: # Chỉ delay nếu chưa phải lần cuối
            log("Đang đợi 3 giây...")
            time.sleep(10)
    
    print("\n" + "="*20)
    log("HOÀN TẤT QUÁ TRÌNH.")

if __name__ == "__main__":
    main()
