import os
import shutil
import time
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "roblox://placeId=2753915549" 
DELAY_SECONDS = 15

# --- HÀM HỖ TRỢ ---
def flush_input():
    """Xóa bộ nhớ đệm bàn phím để tránh lỗi tự nhập"""
    try:
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    except:
        pass

def main():
    os.system('clear')
    print("=== TOOL AUTO EXECUTE (LITE VERSION) ===\n")

    # 1. COPY FILE (Đơn giản hóa)
    if os.path.exists(SOURCE_PATH):
        if not os.path.exists(DEST_PATH):
            os.makedirs(DEST_PATH)
        
        files = os.listdir(SOURCE_PATH)
        count = 0
        print(f"[*] Đang đồng bộ từ: {SOURCE_PATH}")
        
        for f in files:
            full_src = os.path.join(SOURCE_PATH, f)
            if os.path.isfile(full_src):
                shutil.copy2(full_src, os.path.join(DEST_PATH, f))
                count += 1
                print(f"  + Đã chép: {f}")
        
        print(f"-> Hoàn tất! Đã chép {count} file.\n")
    else:
        print(f"[!] Lỗi: Không tìm thấy thư mục nguồn {SOURCE_PATH}\n")

    # 2. NHẬP SỐ LẦN CHẠY (Giữ fix lỗi trôi lệnh)
    flush_input() # Xóa phím thừa
    try:
        raw = input("➤ Nhập số lần chạy (Enter để mặc định là 4): ")
        loop_count = int(raw) if raw.strip() else 4
    except ValueError:
        loop_count = 4

    print(f"\n[*] Bắt đầu chạy {loop_count} lần với delay {DELAY_SECONDS}s...")
    time.sleep(1)

    # 3. VÒNG LẶP CHÍNH
    for i in range(1, loop_count + 1):
        print(f"\n----------------------------")
        print(f"[*] Đang chạy lần: {i}/{loop_count}")
        
        # Mở Game
        os.system(f'termux-open-url "{GAME_URL}"')
        print("-> Đã mở Roblox.")
        
        if i < loop_count:
            # Đếm ngược đơn giản
            print(f"-> Chờ {DELAY_SECONDS} giây cho lần tiếp theo...")
            for s in range(DELAY_SECONDS, 0, -1):
                sys.stdout.write(f"\r   Còn lại: {s}s ")
                sys.stdout.flush()
                time.sleep(1)
            print("\r   Đang chuyển tiếp...   ")

    print("\n\n=== HOÀN TẤT ===")
    input("Nhập Enter để thoát.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Đã dừng tool.")
