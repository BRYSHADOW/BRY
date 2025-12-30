import os
import shutil
import time
import sys
import random
import platform

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "roblox://placeId=2753915549" 
DELAY_SECONDS = 15

# --- MÀU SẮC NEON ---
R = "\033[38;5;196m" # Red Neon
G = "\033[38;5;46m"  # Green Matrix
C = "\033[38;5;51m"  # Cyan Neon
P = "\033[38;5;201m" # Pink Neon
Y = "\033[38;5;226m" # Yellow
W = "\033[1;37m"     # White Bold
GR = "\033[38;5;240m" # Gray
BG = "\033[48;5;235m" # Dark Background
RESET = "\033[0m"

# --- HÀM HỖ TRỢ VISUAL ---

def get_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def center(text, color=W):
    w = get_width()
    stripped = text.replace(R, "").replace(G, "").replace(C, "").replace(P, "").replace(Y, "").replace(W, "").replace(RESET, "")
    pad = (w - len(stripped)) // 2
    if pad < 0: pad = 0
    return " " * pad + color + text + RESET

def matrix_rain():
    """Hiệu ứng mưa ma trận"""
    os.system('clear')
    w = get_width()
    chars = "10 01 <> {} [] // -- ||"
    for _ in range(20): # Giảm xuống 20 cho nhanh hơn chút
        line = ""
        for _ in range(w // 3):
            line += random.choice(chars) + " "
        print(f"{G}{line}{RESET}")
        time.sleep(0.02)
    os.system('clear')

def spin_loading(text, duration):
    """Vòng xoay loading đẹp"""
    chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{center(f'{C}{chars[i % 8]} {text}... {chars[i % 8]}')}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * get_width() + "\r") # Xóa dòng

def msg_banner():
    os.system('clear')
    print(R + "=" * get_width() + RESET)
    logo = f"""
{C}██████╗  ██████╗ ██████╗ ██╗   ██╗██████╗ ███████╗
██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗╚══███╔╝
██████╔╝██║   ██║██████╔╝ ╚████╔╝ ██║  ██║  ███╔╝ 
██╔══██╗██║   ██║██╔══██╗  ╚██╔╝  ██║  ██║ ███╔╝  
██████╔╝╚██████╔╝██║  ██║   ██║   ██████╔╝███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚══════╝{RESET}
"""
    print(logo)
    print(center(f"{BG}  SYSTEM: ONLINE | USER: VIP | MODE: GOD  {RESET}"))
    print(R + "=" * get_width() + RESET)

def box_msg(title, msg, color=W):
    w = get_width() - 4
    print(center(f"{color}┌─ {title} {'─'*(w-len(title)-5)}┐"))
    print(center(f"{color}│ {msg.center(w-4)} │"))
    print(center(f"{color}└{'─'*(w-2)}┘"))

def flush_input():
    """Xóa bộ nhớ đệm bàn phím để tránh tự nhập"""
    try:
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    except:
        pass

# --- LOGIC CHÍNH ---

def main():
    # 1. INTRO
    matrix_rain()
    msg_banner()
    
    # Fake System Check
    print(center(f"{GR}Kiểm tra thông số hệ thống...{RESET}"))
    time.sleep(0.5)
    print(center(f"{GR}OS: {platform.system()} | Release: {platform.release()}{RESET}"))
    spin_loading(f"{P}Đang tối ưu hóa bộ nhớ RAM", 2)
    
    # 2. CHECK & COPY
    print("\n")
    script_count = 0
    if os.path.exists(SOURCE_PATH):
        if not os.path.exists(DEST_PATH):
            os.makedirs(DEST_PATH)
        
        files = os.listdir(SOURCE_PATH)
        real_files = [f for f in files if os.path.isfile(os.path.join(SOURCE_PATH, f))]
        
        # Hiệu ứng copy từng file
        for f in real_files:
            src = os.path.join(SOURCE_PATH, f)
            dst = os.path.join(DEST_PATH, f)
            shutil.copy2(src, dst)
            script_count += 1
            print(f"\r{G} [SYNC] >> {f}{RESET}", end="")
            time.sleep(0.05)
        
        print("\n")
        box_msg("REPORT", f"Đã đồng bộ thành công {script_count} Scripts", C)
    else:
        box_msg("ERROR", "Không tìm thấy thư mục Scripts!", R)

    # 3. NHẬP SỐ LƯỢNG
    print("\n")
    
    print(center(f"{Y}╔══════════════════════════════╗"))
    print(center(f"{Y}║   NHẬP SỐ LẦN CHẠY (ENTER=4) ║"))
    print(center(f"{Y}╚══════════════════════════════╝"))
    
    # --- ĐOẠN ĐƯỢC SỬA Ở ĐÂY ---
    time.sleep(0.5) # Chờ 0.5 giây để ổn định
    flush_input()   # Xóa sạch phím Enter thừa ngay trước khi nhập
    # ---------------------------

    loop_count = 4
    try:
        # Thêm khoảng trắng để dễ nhìn
        raw = input(f"\n{P}➤ INPUT COMMAND > {RESET}")
        if raw.strip():
            loop_count = int(raw)
    except: 
        pass

    # 4. START LOOP
    print("\n")
    spin_loading(f"{R}INITIATING LAUNCH SEQUENCE", 2)
    
    for i in range(1, loop_count + 1):
        os.system('clear')
        # Giao diện khi đang chạy
        print(f"{P}╔{'═'* (get_width()-2)}╗{RESET}")
        print(center(f"{P}║ CYBER-EXECUTE SESSION: {W}#{random.randint(10000, 99999)} {P}║"))
        print(f"{P}╠{'═'* (get_width()-2)}╣{RESET}")
        
        # Thanh tiến trình tổng
        percent = int((i / loop_count) * 100)
        bar_len = 20
        filled = int((i / loop_count) * bar_len)
        bar = "█" * filled + "░" * (bar_len - filled)
        
        print(center(f"{C}PROGRESS: [{bar}] {percent}%"))
        print(center(f"{Y}LOOP: {i}/{loop_count}"))
        print(f"{P}╚{'═'* (get_width()-2)}╝{RESET}")
        
        # Action
        print("\n")
        box_msg("ACTION", "INJECTING URL TO SYSTEM...", G)
        try:
            os.system(f'termux-open-url "{GAME_URL}"')
        except: pass
        
        if i < loop_count:
            # Countdown số to
            print("\n")
            remain = DELAY_SECONDS
            while remain > 0:
                # Hiệu ứng số đếm ngược thay đổi màu
                color = R if remain <= 3 else (Y if remain <= 7 else G)
                sys.stdout.write(f"\r{center(f'{GR}Next payload in: {color}>>> {remain:02d} <<< {GR}seconds')}")
                sys.stdout.flush()
                time.sleep(1)
                remain -= 1
    
    # 5. END
    os.system('clear')
    print(center(f"{G}╔══════════════════════════╗"))
    print(center(f"{G}║   BÔ RY ĐẸP TRAI VÃI LỒN  ║"))
    print(center(f"{G}╚══════════════════════════╝{RESET}"))
    print(center(f"{GR}(Press Enter to exit){RESET}"))
    input()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{R}[SYSTEM FAILURE] Error Detail: {e}{RESET}")
