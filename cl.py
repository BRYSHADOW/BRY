import os
import shutil
import time
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "roblox://placeId=2753915549" 
DELAY_SECONDS = 15  # Thời gian nghỉ giữa các lần mở

# --- MÀU SẮC ---
R = "\033[91m" 
G = "\033[92m" 
Y = "\033[93m" 
C = "\033[96m" 
B = "\033[1m"  
RESET = "\033[0m"

def banner():
    os.system('clear')
    print(f"{C}{B}╔══════════════════════════════════════════╗")
    print(f"║        AUTO DELTA EXECUTOR V2            ║")
    print(f"╚══════════════════════════════════════════╝{RESET}")

def log(text):
    print(f"{G}[OK]{RESET} {text}")

def error(text):
    print(f"{R}[ERROR]{RESET} {text}")

def check_permission():
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Chạy: termux-setup-storage")
        sys.exit(1)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r{Y}[WAIT] Mở lại sau: {timer} ...{RESET}", end="")
        time.sleep(1)
        t -= 1
    print("\r" + " " * 40 + "\r", end="")

def main():
    check_permission()
    banner()
    
    # 1. COPY FILE
    if os.path.exists(SOURCE_PATH):
        os.makedirs(DEST_PATH, exist_ok=True)
        try:
            files = os.listdir(SOURCE_PATH)
            count = 0
            for f in files:
                src = os.path.join(SOURCE_PATH, f)
                if os.path.isfile(src):
                    shutil.copy2(src, os.path.join(DEST_PATH, f))
                    count += 1
            log(f"Đã copy {count} script vào Autoexecute.")
        except Exception as e:
            error(f"Lỗi copy: {e}")
    else:
        error("Không tìm thấy thư mục Scripts.")

    # 2. NHẬP SỐ LƯỢNG (CÓ XỬ LÝ LỖI EOF)
    loop_count = 4 # Mặc định
    print("-" * 40)
    try:
        # Thêm thời gian chờ hoặc nhắc nhở
        raw = input(f"{B}➤ Nhập số lần mở game (Mặc định 4): {RESET}")
        if raw.strip():
            loop_count = int(raw)
    except (ValueError, EOFError):
        # Nếu nhập sai hoặc lỗi EOF (do paste code), tự động lấy mặc định
        print(f"\n{Y}⚠ Không nhận được số, tự động chạy mặc định 4 lần...{RESET}")
        time.sleep(2)

    print(f"{G}>>> SẼ MỞ GAME {loop_count} LẦN <<<{RESET}")

    # 3. CHẠY LOOP
    for i in range(1, loop_count + 1):
        print(f"\n{C}--- Lần {i}/{loop_count} ---{RESET}")
        try:
            os.system(f'termux-open-url "{GAME_URL}"')
            log(f"Đã mở Roblox.")
        except: pass

        if i < loop_count:
            countdown(DELAY_SECONDS)
    
    print(f"\n{G}HOÀN TẤT.{RESET}")

if __name__ == "__main__":
    main()
