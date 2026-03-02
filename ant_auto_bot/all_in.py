# ชื่อไฟล์: ant_ai_bot.py (อัดทุกอย่างไว้ในนี้)

# ==========================================
# ส่วนที่ 0: Import เครื่องมือทั้งหมดที่ต้องใช้
# ==========================================
import cv2
import numpy as np           # ต้องใช้คู่กับ cv2 เพื่อแปลงภาพ
import pytesseract
from PIL import ImageGrab
import pyautogui
import time                  # ใช้สำหรับหน่วงเวลาให้ AI ไม่คลิกรัวเกินไป
import random
# from stable_baselines3 import DQN  (เดี๋ยวค่อยเปิดใช้ตอนทำสมอง)

# ==========================================
# บล็อกที่ 1: GAME DATA (ฐานข้อมูลมดและ Perks)
# ==========================================
class AntCard:
    def __init__(self, name, cost_food, cost_chitin, hp, damage):
        self.name = name
        self.cost_food = cost_food
        self.cost_chitin = cost_chitin
        self.hp = hp
        self.damage = damage

# ลิสต์มดทั้งหมด (คุณสามารถแก้ตัวเลขให้เป๊ะตาม Wiki ได้เลยครับ!)
AVAILABLE_ANTS = [
    AntCard("Worker", cost_food=10, cost_chitin=0, hp=20, damage=2),
    AntCard("Warrior", cost_food=25, cost_chitin=0, hp=100, damage=15),
    AntCard("Ranger", cost_food=30, cost_chitin=5, hp=60, damage=25),
    AntCard("Tank", cost_food=50, cost_chitin=15, hp=250, damage=5)
]

# ==========================================
# บล็อกที่ 2: VISION (ระบบดวงตา AI - แคปจออ่านเลข)
# ==========================================
class AntEye:
    def __init__(self, region):
        # region คือพิกัด (X ซ้าย, Y บน, X ขวา, Y ล่าง) บนหน้าจอ
        self.region = region 
        
    def get_number(self):
        try:
            # 1. แคปภาพหน้าจอเฉพาะจุดที่กำหนด
            img = ImageGrab.grab(bbox=self.region)
            
            # 2. แปลงเป็นอาร์เรย์และทำภาพเป็นขาวดำ (ลด Noise ให้ OCR)
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
            
            # 3. ให้ Tesseract อ่านเลข (บังคับให้อ่านเฉพาะ 0-9)
            text = pytesseract.image_to_string(img_cv, config='--psm 7 -c tessedit_char_whitelist=0123456789')
            
            # คืนค่าตัวเลข ถ้าว่างเปล่าจะเกิด Error เลยดักไว้ด้วย Try-Except
            return int(text.strip())
        except Exception:
            # ถ้าอ่านไม่ออก หรือจอกระพริบ ให้คืนค่า 0 ชั่วคราว
            return 0

# ==========================================
# บล็อกที่ 3: ENVIRONMENT & ACTIONS (มือกดจอและกฎกติกา)
# ==========================================
class AntEnvironment:
    def __init__(self):
        # ⚠️ พิกัดดวงตา: คุณต้องเปลี่ยนตัวเลขให้ตรงกับกรอบ UI อาหารบนจอคุณ
        self.food_eye = AntEye(region=(100, 50, 200, 80)) 
        self.chitin_eye = AntEye(region=(250, 50, 350, 80))
        
        # ⚠️ พิกัดมือ: ตำแหน่งการ์ดบนจอ Mac (X, Y) ที่จะให้เมาส์ไปกด
        self.card_positions = {
            "Worker": (300, 800),
            "Warrior": (400, 800),
            "Ranger": (500, 800),
            "Tank": (600, 800)
        }

    def get_state(self):
        # สั่งให้ AI ลืมตาดูหน้าจอ
        food = self.food_eye.get_number()
        chitin = self.chitin_eye.get_number()
        return food, chitin

    def step(self, action_name):
        # 1. จัดการแอคชัน (คลิกเมาส์)
        if action_name == "Wait":
            pass # นิ่งไว้ รออาหารเด้ง
        elif action_name in self.card_positions:
            # ดึงพิกัดการ์ดแล้วสั่งคลิก
            x, y = self.card_positions[action_name]
            pyautogui.click(x, y)
            print(f"👉 AI เลื่อนเมาส์ไปคลิกการ์ด: {action_name}")
            
        # 2. หน่วงเวลาให้เกมรันแอนิเมชันแป๊บนึง
        time.sleep(1.0) 
        
        # 3. คืนค่าสถานะใหม่กลับไป
        new_food, new_chitin = self.get_state()
        return new_food, new_chitin

# ==========================================
# บล็อกที่ 4: MAIN LOOP (ห้องทำงานหลัก)
# ==========================================
if __name__ == "__main__":
    print("--- 🚀 เริ่มเดินเครื่อง AI Ant Colony ---")
    
    # 1. สร้างโลกจำลอง (เชื่อมเกม)
    env = AntEnvironment()
    
    # 2. จำลองให้ AI ลองเล่น 10 เทิร์น (เดี๋ยวอนาคตจะเปลี่ยนรันด้วย DQN)
    for turn in range(1, 11):
        print(f"\n--- ⏱️ เทิร์นที่ {turn} ---")
        
        # AI มองหน้าจอ
        current_food, current_chitin = env.get_state()
        print(f"👀 AI มองเห็น -> Food: {current_food}, Chitin: {current_chitin}")
        
        # AI ใช้ความคิด (ทดสอบด้วยกฎ If-Else ง่ายๆ ไปก่อน)
        if current_food >= 50 and current_chitin >= 15:
            action = "Tank"
        elif current_food >= 25:
            action = "Warrior"
        elif current_food >= 10:
            action = "Worker"
        else:
            action = "Wait"
            
        print(f"🧠 AI ตัดสินใจทำ: {action}")
        
        # AI ลงมือทำ
        env.step(action)
        
    print("\n✅ จบการทดสอบระบบ 10 เทิร์นแรก!")