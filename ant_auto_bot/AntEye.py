import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab

class AntEye:
    def __init__(self, region):
        # region คือพิกัดหน้าจอ (ซ้าย, บน, ขวา, ล่าง) ที่เราต้องการให้ AI จ้องมอง
        self.region = region 
        
    def get_number(self):
        # 1. แคปภาพหน้าจอเฉพาะจุดที่กำหนด (เช่น มุมขวาบนที่มีเลข Food)
        img = ImageGrab.grab(bbox=self.region)
        
        # 2. แปลงภาพเป็นขาวดำ (Grayscale) เพื่อให้ OCR อ่านตัวเลขได้แม่นยำขึ้น
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
        
        # 3. สั่งให้ Tesseract อ่านตัวเลขจากภาพ
        # config='--psm 7 -c tessedit_char_whitelist=0123456789' บังคับให้อ่านแค่ตัวเลข
        text = pytesseract.image_to_string(img_cv, config='--psm 7 -c tessedit_char_whitelist=0123456789')
        
        # คืนค่าตัวเลขที่อ่านได้ ถ้าอ่านไม่ออกให้คืนค่า 0
        try:
            return int(text.strip())
        except ValueError:
            return 0

# --- วิธีนำไปใช้งานจริง ---
# สมมติว่าพิกัดของตัวเลข Food บนจอ Emulator ของคุณอยู่ตรงกล่องพิกัด (100, 50, 200, 80)
food_eye = AntEye(region=(100, 50, 200, 80))

# เรียกดูตัวเลขแบบ Real-time
current_food = food_eye.get_number()
print(f"ตอนนี้มีอาหาร: {current_food} ชิ้น")