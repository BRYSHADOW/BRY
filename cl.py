import os
import shutil
import time
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"

# Link Deep-link
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
    
    # 1. COPY FILE (Giữ nguyên)
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
                    shutil.copyfile(src, dst)
                    count += 1
            log(f"Đã copy xong {count} file.")
        except Exception as e:
            error(f"Lỗi khi copy: {e}")
    else:
        log("Không tìm thấy thư mục Scripts (Bỏ qua copy).")

    # 2. NHẬP SỐ LƯỢNG MỞ GAME
    print("\n" + "="*20)
    while True:
        try:
            user_input = input("\033[93m👉 Nhập số lần muốn mở game (Mặc định 4): \033[0m").strip()
            if user_input == "":
                so_lan = 4 # Mặc định nếu không nhập gì
                break
            so_lan = int(user_input)
            if so_lan > 0:
                break
            else:
                print("⚠️ Vui lòng nhập số lớn hơn 0.")
        except ValueError:
            print("⚠️ Lỗi: Chỉ được nhập con số!")

    # 3. MỞ LINK THEO SỐ LẦN ĐÃ CHỌN
    log(f"Bắt đầu mở game {so_lan} lần...")
    
    for i in range(1, so_lan + 1):
        print(f"\n--- Lần mở thứ {i}/{so_lan} ---")
        try:
            os.system(f'termux-open-url "{GAME_URL}"')
            log(f"Đã gửi lệnh mở game.")
        except Exception as e:
            error(f"Lỗi: {e}")
            
        # Chỉ delay nếu chưa phải lần cuối cùng
        if i < so_lan: 
            log("Đang đợi 3 giây...")
            time.sleep(3)
    
    print("\n" + "="*20)
    log("HOÀN TẤT QUÁ TRÌNH.")

if __name__ == "__main__":
    main()
