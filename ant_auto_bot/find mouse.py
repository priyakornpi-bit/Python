import pyautogui
import time

print("🎯 โปรแกรมเรดาร์หาพิกัดเมาส์ (กด Ctrl+C ที่ Terminal เพื่อหยุดการทำงาน)")
print("--------------------------------------------------")

try:
    while True:
        # ดึงพิกัด X, Y ของเมาส์ ณ วินาทีนั้น
        x, y = pyautogui.position()
        # ปริ้นท์ทับบรรทัดเดิมไปเรื่อยๆ จะได้ไม่อ่านยาก
        print(f"📍 พิกัดปัจจุบัน -> X: {x:<4} | Y: {y:<4}", end="\r")
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\n\n✅ ปิดโปรแกรมเรดาร์เรียบร้อยครับ!")