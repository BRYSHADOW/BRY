import os
import shutil
import time
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "roblox://placeId=2753915549" 
DELAY_SECONDS = 15

# --- MÀU SẮC ---
R, G, Y, C, B, RESET = "\033[91m", "\033[92m", "\033[93m", "\033[96m", "\033[1m", "\033[0m"

def banner():
    os.system('clear')
    print(f"{C}{B}╔══════════════════════════════════════════╗")
    print(f"║      AUTO DELTA EXECUTOR - VIP V3        ║")
    print(f"╚══════════════════════════════════════════╝{RESET}")

def log(text): print(f"{G}[OK]{RESET} {text}")
def error(text): print(f"{R}[LỖI]{RESET} {text}")

def check_permission():
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền! Chạy: termux-setup-storage")
        sys.exit(1)

# HÀM XÓA BỘ ĐỆM BÀN PHÍM (Fix lỗi tự Enter)
def flush_input():
    try:
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    except: pass

def countdown(t):
    while t:
        print(f"\r{Y}[CHỜ] Mở lại sau: {t}s ...{RESET}", end="")
        time.sleep(1)
        t -= 1
    print("\r" + " " * 30 + "\r", end="")

def main():
    check_permission()
    banner()
    
    # 1. COPY FILE
    if os.path.exists(SOURCE_PATH):
        os.makedirs(DEST_PATH, exist_ok=True)
        try:
            files = [f for f in os.listdir(SOURCE_PATH) if os.path.isfile(os.path.join(SOURCE_PATH, f))]
            count = 0
            for f in files:
                shutil.copy2(os.path.join(SOURCE_PATH, f), os.path.join(DEST_PATH, f))
                count += 1
            log(f"Đã copy {count} script.")
        except Exception as e: error(f"Lỗi copy: {e}")
    else:
        error("Không thấy thư mục Scripts.")

    print("-" * 40)
    
    # 2. NHẬP SỐ LƯỢNG (Đã Fix lỗi trôi lệnh)
    # Xả bộ đệm để tránh lệnh Enter cũ dính vào
    flush_input() 
    time.sleep(0.5) 
    
    loop_count = 4
    while True:
        try:
            print(f"{Y}➤ Bạn muốn mở bao nhiêu lần?{RESET}")
            print(f"  (Nhấn {B}Enter{RESET} để lấy mặc định là {B}4{RESET})")
            raw = input(f"{C}➜ Nhập số: {RESET}")
            
            if raw.strip() == "":
                log("Đã chọn mặc định: 4 lần.")
                loop_count = 4
                break
            
            loop_count = int(raw)
            if loop_count > 0:
                break
            else:
                error("Phải nhập số lớn hơn 0!")
        except ValueError:
            error("Vui lòng chỉ nhập số (hoặc nhấn Enter)!")
        except EOFError:
            # Nếu vẫn bị lỗi này, nghĩa là đang paste code
            print(f"\n{R}[CẢNH BÁO] Đừng paste code trực tiếp! Hãy lưu vào file.{RESET}")
            sys.exit()

    print(f"\n{G}>>> BẮT ĐẦU CHẠY {loop_count} LẦN <<<{RESET}")

    # 3. CHẠY LOOP
    for i in range(1, loop_count + 1):
        print(f"\n{C}--- Lần {i} / {loop_count} ---{RESET}")
        try:
            os.system(f'termux-open-url "{GAME_URL}"')
            log("Đã mở Roblox.")
        except: pass

        if i < loop_count:
            countdown(DELAY_SECONDS)
    
    print(f"\n{G}✔ HOÀN TẤT.{RESET}")

if __name__ == "__main__":
    main()
