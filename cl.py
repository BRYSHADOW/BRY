import os
import shutil
import time
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"

# Link Deep-link (Vào thẳng game)
GAME_URL = "roblox://placeId=2753915549" 

def log(text):
    print(f"\033[92m[AUTO]\033[0m {text}")

def error(text):
    print(f"\033[91m[ERROR]\033[0m {text}")

def check_permission():
    # Kiểm tra quyền truy cập bộ nhớ
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Hãy chạy lệnh: termux-setup-storage")
        sys.exit(1)

def main():
    check_permission()
    
    # --- PHẦN 1: COPY FILE ---
    print("\n" + "="*20)
    log("Đang kiểm tra và copy scripts...")
    
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
            log(f"Đã copy thành công: {count} file.")
        except Exception as e:
            error(f"Lỗi khi copy: {e}")
    else:
        log(f"Không tìm thấy thư mục nguồn: {SOURCE_PATH}")
        log("Bỏ qua bước copy.")

    # --- PHẦN 2: NHẬP SỐ LẦN MUỐN MỞ ---
    print("="*20)
    while True:
        try:
            # Nhập input từ bàn phím
            user_input = input("\033[93m👉 Nhập số lần muốn mở game (Mặc định Enter là 4): \033[0m").strip()
            
            if user_input == "":
                so_lan = 4 # Nếu không nhập gì thì lấy số 4
                break
            
            so_lan = int(user_input)
            if so_lan > 0:
                break
            else:
                print("⚠️ Vui lòng nhập số lớn hơn 0.")
        except ValueError:
            print("⚠️ Lỗi: Chỉ được nhập con số (Ví dụ: 1, 2, 5...)")

    # --- PHẦN 3: THỰC THI MỞ GAME ---
    log(f"Bắt đầu mở game {so_lan} lần...")
    
    for i in range(1, so_lan + 1):
        print(f"\n--- Lần mở thứ {i}/{so_lan} ---")
        try:
            # Lệnh Termux để mở link
            os.system(f'termux-open-url "{GAME_URL}"')
            log(f"Đã gửi lệnh mở Roblox.")
        except Exception as e:
            error(f"Lỗi hệ thống: {e}")
            
        # Nếu chưa phải lần cuối thì đợi 3 giây
        if i < so_lan: 
            log("Đang đợi 3 giây để mở lần tiếp theo...")
            time.sleep(3)
    
    print("\n" + "="*20)
    log("HOÀN TẤT! Chúc bạn chơi vui vẻ.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m[STOP]\033[0m Đã dừng tool thủ công.")
