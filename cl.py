import os
import shutil
import time
import sys

# --- CẤU HÌNH (Sửa thông số tại đây) ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "roblox://placeId=2753915549" 
DELAY_SECONDS = 15  # Thời gian nghỉ giữa các lần mở (giây)

# --- MÀU SẮC TERMINAL (Cho đẹp) ---
R = "\033[91m" # Đỏ
G = "\033[92m" # Xanh lá
Y = "\033[93m" # Vàng
C = "\033[96m" # Xanh dương
B = "\033[1m"  # In đậm
RESET = "\033[0m"

def clear_screen():
    os.system('clear')

def banner():
    clear_screen()
    print(f"{C}{B}╔══════════════════════════════════════════╗")
    print(f"║        AUTO DELTA EXECUTOR TOOL          ║")
    print(f"║     {R}♦{C} Copy Scripts & Auto Open {R}♦{C}        ║")
    print(f"╚══════════════════════════════════════════╝{RESET}")
    print(f"{Y}➤ Delta Path: {SOURCE_PATH}{RESET}")
    print(f"{Y}➤ Game ID:    {GAME_URL.split('=')[-1]}{RESET}")
    print("-" * 44)

def log(text):
    print(f"{G}[SUCCESS]{RESET} {text}")

def info(text):
    print(f"{C}[INFO]{RESET} {text}")

def warn(text):
    print(f"{Y}[WAIT]{RESET} {text}")

def error(text):
    print(f"{R}[ERROR]{RESET} {text}")

def check_permission():
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Vui lòng chạy lệnh:")
        print(f"{Y}termux-setup-storage{RESET}")
        sys.exit(1)

def countdown(t):
    """Hiển thị đếm ngược đẹp mắt"""
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r{Y}[WAIT] Đang đợi mở lần tiếp theo trong: {timer} ...{RESET}", end="")
        time.sleep(1)
        t -= 1
    print("\r" + " " * 50 + "\r", end="") # Xóa dòng đếm ngược

def main():
    check_permission()
    banner()
    
    # --- PHẦN 1: COPY FILE ---
    info("Đang kiểm tra thư mục Scripts...")
    
    if os.path.exists(SOURCE_PATH):
        # Tạo thư mục đích nếu chưa có
        os.makedirs(DEST_PATH, exist_ok=True)
        
        count = 0
        try:
            files = os.listdir(SOURCE_PATH)
            total_files = len([f for f in files if os.path.isfile(os.path.join(SOURCE_PATH, f))])
            
            if total_files == 0:
                warn("Thư mục Scripts trống, không có gì để copy.")
            else:
                for f in files:
                    src = os.path.join(SOURCE_PATH, f)
                    dst = os.path.join(DEST_PATH, f)
                    if os.path.isfile(src):
                        shutil.copy2(src, dst) # copy2 giữ nguyên metadata tốt hơn
                        count += 1
                        print(f"  ➜ Đã chép: {f}")
                
                log(f"Hoàn tất copy {count}/{total_files} file vào Autoexecute.")
        except Exception as e:
            error(f"Lỗi khi copy: {e}")
    else:
        error("Không tìm thấy thư mục Delta/Scripts! (Bỏ qua bước copy)")

    print("-" * 44)

    # --- PHẦN 2: NHẬP SỐ LƯỢNG VÀ MỞ GAME ---
    while True:
        try:
            raw_input = input(f"{B}➤ Nhập số lần bạn muốn mở game (Ví dụ: 5): {RESET}")
            loop_count = int(raw_input)
            if loop_count > 0:
                break
            else:
                error("Vui lòng nhập số lớn hơn 0.")
        except ValueError:
            error("Vui lòng chỉ nhập số!")

    print(f"\n{G}>>> BẮT ĐẦU QUÁ TRÌNH MỞ GAME {loop_count} LẦN <<<{RESET}")

    for i in range(1, loop_count + 1):
        print(f"\n{C}{B}--- [ Lần thứ {i} / {loop_count} ] ---{RESET}")
        
        try:
            # Lệnh mở URL
            os.system(f'termux-open-url "{GAME_URL}"')
            log(f"Đã gửi lệnh mở Roblox.")
        except Exception as e:
            error(f"Không thể mở link: {e}")

        # Nếu chưa phải lần cuối thì mới đếm ngược
        if i < loop_count:
            countdown(DELAY_SECONDS)
    
    print("\n" + "="*44)
    print(f"{G}{B}   (✔) ĐÃ HOÀN TẤT TOÀN BỘ CÔNG VIỆC!{RESET}")
    print("="*44)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[STOP] Đã dừng chương trình.{RESET}")
