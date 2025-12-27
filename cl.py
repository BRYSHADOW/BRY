import os
import shutil
import time
import subprocess
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "https://www.roblox.com/vi/games/2753915549/Blox-Fruits"
KEYWORD_SEARCH = "delta" 

def log(text):
    print(f"\033[92m[AUTO]\033[0m {text}")

def error(text):
    print(f"\033[91m[ERROR]\033[0m {text}")

def check_permission():
    if not os.access("/storage/emulated/0/", os.R_OK):
        error("Chưa cấp quyền bộ nhớ! Chạy: termux-setup-storage")
        sys.exit(1)

def find_packages():
    log(f"Đang tìm ứng dụng chứa chữ '{KEYWORD_SEARCH}'...")
    try:
        # Dùng đường dẫn tuyệt đối để tránh lỗi not found
        cmd = "/system/bin/pm list packages" 
        output = subprocess.getoutput(cmd)
        
        found_packages = []
        for line in output.splitlines():
            if KEYWORD_SEARCH in line:
                pkg_name = line.replace("package:", "").strip()
                found_packages.append(pkg_name)
        
        if not found_packages:
            error(f"Không tìm thấy package nào tên '{KEYWORD_SEARCH}'.")
            return []
        
        # Lọc bớt trùng lặp nếu có
        found_packages = list(set(found_packages))
        log(f"Đã tìm thấy: {found_packages}")
        return found_packages
    except Exception as e:
        error(f"Lỗi tìm package: {e}")
        return []

def open_apps(packages):
    log("Đang mở ứng dụng...")
    for pkg in packages:
        print(f"\n--- Đang mở: {pkg} ---")
        
        # Dùng đường dẫn tuyệt đối cho monkey
        cmd_monkey = f"/system/bin/monkey -p {pkg} -c android.intent.category.LAUNCHER 1"
        
        try:
            # Chạy lệnh và ẩn output rác đi cho gọn
            subprocess.call(cmd_monkey, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log(f"-> Đã gửi lệnh mở {pkg}")
        except Exception as e:
            error(f"Lỗi khi mở app: {e}")

        time.sleep(3) 

def main():
    check_permission()
    
    # 1. COPY FILE (Đã sửa lỗi PermissionError)
    log("Bắt đầu copy scripts...")
    if os.path.exists(SOURCE_PATH):
        if not os.path.exists(DEST_PATH):
            try:
                os.makedirs(DEST_PATH)
            except OSError:
                pass # Bỏ qua nếu thư mục đã tồn tại
        
        count = 0
        files = os.listdir(SOURCE_PATH)
        for f in files:
            src = os.path.join(SOURCE_PATH, f)
            dst = os.path.join(DEST_PATH, f)
            
            if os.path.isfile(src):
                try:
                    # QUAN TRỌNG: Dùng copyfile thay vì copy2 để tránh lỗi Permission
                    shutil.copyfile(src, dst)
                    count += 1
                except Exception as e:
                    error(f"Không thể copy {f}: {e}")
                    
        log(f"Đã copy xong {count} file.")
    else:
        error(f"Không thấy thư mục nguồn: {SOURCE_PATH}")

    # 2. TÌM VÀ MỞ APP
    pkgs = find_packages()
    if pkgs:
        open_apps(pkgs)
    else:
        log("Bỏ qua mở App (Không tìm thấy tên).")

    # 3. MỞ LINK GAME
    log("Đang mở link game...")
    try:
        os.system(f'termux-open-url "{GAME_URL}"')
    except:
        pass
    
    log("HOÀN TẤT.")

if __name__ == "__main__":
    main()
