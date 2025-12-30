import os
import shutil
import time
import sys
import random
import platform

# ================== CẤU HÌNH ==================
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH   = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL    = "roblox://placeId=2753915549"
DELAY_SECONDS = 15

# ================== ANSI COLORS ==================
R  = "\033[38;5;196m"
G  = "\033[38;5;46m"
C  = "\033[38;5;51m"
P  = "\033[38;5;201m"
Y  = "\033[38;5;226m"
W  = "\033[1;37m"
GR = "\033[38;5;240m"
BG = "\033[48;5;235m"
RESET = "\033[0m"

ANSI_CODES = [R, G, C, P, Y, W, GR, BG, RESET]

# ================== HÀM HIỂN THỊ ==================
def get_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def center(text, color=W):
    w = get_width()
    stripped = text
    for code in ANSI_CODES:
        stripped = stripped.replace(code, "")
    pad = (w - len(stripped)) // 2
    if pad < 0:
        pad = 0
    return " " * pad + color + text + RESET

def matrix_rain():
    os.system("clear")
    chars = ["10", "01", "<>", "{}", "[]", "//", "--", "||"]
    w = get_width()
    for _ in range(25):
        line = ""
        for _ in range(w // 3):
            line += random.choice(chars) + " "
        print(f"{G}{line}{RESET}")
        time.sleep(0.03)
    os.system("clear")

def spin_loading(text, duration):
    icons = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write("\r" + center(f"{C}{icons[i%8]} {text} {icons[i%8]}"))
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * get_width() + "\r")

def msg_banner():
    os.system("clear")
    print(R + "=" * get_width() + RESET)
    print(f"""{C}
██████╗  ██████╗ ██████╗ ██╗   ██╗██████╗ ███████╗
██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗╚══███╔╝
██████╔╝██║   ██║██████╔╝ ╚████╔╝ ██║  ██║  ███╔╝
██╔══██╗██║   ██║██╔══██╗  ╚██╔╝  ██║  ██║ ███╔╝
██████╔╝╚██████╔╝██║  ██║   ██║   ██████╔╝███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚══════╝
{RESET}""")
    print(center(f"{BG}  SYSTEM: ONLINE | USER: VIP | MODE: GOD  "))
    print(R + "=" * get_width() + RESET)

def box_msg(title, msg, color=W):
    w = get_width() - 6
    print(center(f"{color}┌─ {title} {'─'*(w-len(title)-2)}┐"))
    print(center(f"{color}│ {msg.center(w)} │"))
    print(center(f"{color}└{'─'*(w+2)}┘"))

# ================== MAIN ==================
def main():
    matrix_rain()
    msg_banner()

    print(center(f"{GR}Kiểm tra hệ thống...{RESET}"))
    time.sleep(0.5)
    print(center(f"{GR}OS: {platform.system()} | {platform.release()}{RESET}"))
    spin_loading("Đang tối ưu RAM", 2)

    print()
    count = 0
    if os.path.exists(SOURCE_PATH):
        os.makedirs(DEST_PATH, exist_ok=True)
        for f in os.listdir(SOURCE_PATH):
            src = os.path.join(SOURCE_PATH, f)
            dst = os.path.join(DEST_PATH, f)
            if os.path.isfile(src) and not os.path.exists(dst):
                shutil.copy2(src, dst)
                count += 1
                print(f"{G}[SYNC] {f}{RESET}")
                time.sleep(0.05)
        box_msg("REPORT", f"Đã đồng bộ {count} script", C)
    else:
        box_msg("ERROR", "Không tìm thấy thư mục Scripts", R)

    print()
    print(center(f"{Y}NHẬP SỐ LẦN CHẠY (ENTER = 4){RESET}"))
    loop = 4
    try:
        inp = input(f"{P}➤ INPUT > {RESET}")
        if inp.strip():
            loop = max(1, int(inp))
    except:
        loop = 4

    spin_loading("INIT LAUNCH SEQUENCE", 2)

    for i in range(1, loop + 1):
        os.system("clear")
        percent = int(i / loop * 100)
        bar_len = 20
        fill = int(i / loop * bar_len)
        bar = "█"*fill + "░"*(bar_len-fill)

        print(center(f"{C}PROGRESS [{bar}] {percent}%"))
        print(center(f"{Y}LOOP {i}/{loop}{RESET}"))
        print()

        box_msg("ACTION", "OPENING ROBLOX URL", G)

        if "termux" in platform.platform().lower():
            os.system(f'termux-open-url "{GAME_URL}"')

        if i < loop:
            for s in range(DELAY_SECONDS, 0, -1):
                col = R if s <= 3 else (Y if s <= 7 else G)
                sys.stdout.write("\r" + center(f"{GR}Next run in {col}{s:02d}{GR}s"))
                sys.stdout.flush()
                time.sleep(1)

    os.system("clear")
    print(center(f"{G}╔════════════════════════════╗"))
    print(center(f"{G}║   BÔ RY SYSTEM FINISHED    ║"))
    print(center(f"{G}╚════════════════════════════╝"))
    input(center(f"{GR}Press Enter to exit{RESET}"))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{R}[ERROR] {e}{RESET}")
