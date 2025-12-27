import os
import shutil
import time
import subprocess
import sys

# --- CẤU HÌNH ---
SOURCE_PATH = "/storage/emulated/0/Delta/Scripts/"
DEST_PATH = "/storage/emulated/0/Delta/Autoexecute/"
GAME_URL = "https://ro.blox.com/ch/Ebh5?is_retargeting=false&pid=experiencestart_mobileweb&af_dp=https%3A%2F%2Fwww.roblox.com%2Fgames%2Fstart%3Fplaceid%3D2753915549%26joinAttemptId%3Dd25eee06-0ce0-47dd-8f0c-d52cb5a52c29&af_web_dp=https%3A%2F%2Fwww.roblox.com%2Fgames%2Fstart%3Fplaceid%3D2753915549%26joinAttemptId%3Dd25eee06-0ce0-47dd-8f0c-d52cb5a52c29&deep_link_value=https%3A%2F%2Fwww.roblox.com%2Fgames%2Fstart%3Fplaceid%3D2753915549%26joinAttemptId%3Dd25eee06-0ce0-47dd-8f0c-d52cb5a52c29"

# Từ khóa tìm package (để tự động tìm tên đúng của app Delta/Roblox)
KEYWORD_SEARCH = "delta" # Nếu không tìm thấy, hãy thử đổi thành "roblox"

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
        # Dùng /system/bin/pm thay vì pm trần
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
            
        log(f"Đã tìm thấy: {found_packages}")
        return found_packages
    except Exception as e:
        error(f"Lỗi tìm package: {e}")
        return []

def open_apps(packages):
    log("Đang mở ứng dụng...")
    
    for pkg in packages:
        print(f"\n--- Đang mở: {pkg} ---")
        
        # CÁCH 1: Dùng Monkey (Thêm /system/bin/)
        # Đây là cách hiệu quả nhất cho máy không root
        cmd_monkey = f"/system/bin/monkey -p {pkg} -c android.intent.category.LAUNCHER 1"
        
        # CÁCH 2: Dùng AM Start (Dự phòng)
        cmd_am = f"/system/bin/am start -n {pkg}/com.roblox.client.ActivityShim"
        
        try:
            # Thử cách 1 trước
            log(f"Đang thử mở bằng Monkey...")
            output = subprocess.getoutput(cmd_monkey)
            
            if "not found" in output:
                error("Vẫn lỗi 'not found'. Đang thử cách 2 (AM Start)...")
                # Thử cách 2
                subprocess.call(cmd_am, shell=True)
            elif "Events injected" in output:
                 log("-> Lệnh Monkey đã gửi thành công.")
            else:
                # In ra để xem có lỗi gì khác không
                print(output)
                
        except Exception as e:
            error(f"Lỗi: {e}")

        time.sleep(3) # Đợi 3s để máy load

def main():
    check_permission()
    
    # 1. COPY FILE
    log("Bắt đầu copy scripts...")
    if os.path.exists(SOURCE_PATH):
        if not os.path.exists(DEST_PATH):
            os.makedirs(DEST_PATH)
        
        count = 0
        for f in os.listdir(SOURCE_PATH):
            src = os.path.join(SOURCE_PATH, f)
            dst = os.path.join(DEST_PATH, f)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                count += 1
        log(f"Đã copy {count} file.")
    else:
        error("Không tìm thấy thư mục Scripts nguồn.")

    # 2. TÌM VÀ MỞ APP
    pkgs = find_packages()
    if pkgs:
        open_apps(pkgs)
    else:
        log("Bỏ qua mở App do không tìm thấy tên package.")

    # 3. MỞ LINK GAME
    log("Đang mở link game...")
    # Dùng termux-open-url (lệnh chuẩn của termux)
    os.system(f'termux-open-url "{GAME_URL}"')
    
    log("HOÀN TẤT.")

if __name__ == "__main__":
    main()
