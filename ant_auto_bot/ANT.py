import random

class AntEnvironment:
    def __init__(self, grid_size=5):
        # 1. กำหนดคุณสมบัติของเกม
        self.grid_size = grid_size  # ขนาดแผนที่ตาราง เช่น 5x5
        self.ant_pos = [0, 0]       # พิกัด [x, y] ของมด
        self.food_pos = [0, 0]      # พิกัด [x, y] ของอาหาร
        
    def reset(self):
        # 2. เริ่มเกม/รีเซ็ตเกม
        # สุ่มตำแหน่งมดและอาหารใหม่
        self.ant_pos = [random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)]
        self.food_pos = [random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)]
        
        # ป้องกันไม่ให้มดกับอาหารเกิดทับกันตั้งแต่เริ่ม
        while self.ant_pos == self.food_pos:
            self.food_pos = [random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)]
            
        # ส่งข้อมูล (State) กลับไปให้ AI เพื่อใช้ตัดสินใจตาแรก
        return self._get_state()

    def _get_state(self):
        # ฟังก์ชันซ่อน (Helper) สำหรับมัดรวมข้อมูลสิ่งที่ AI มองเห็น
        return (self.ant_pos[0], self.ant_pos[1], self.food_pos[0], self.food_pos[1])

    def step(self, action):
        # 3. จุดเปลี่ยนสถานะเกม (รับคำสั่งจาก AI)
        # สมมติให้ Action คือตัวเลข: 0=ขึ้น, 1=ลง, 2=ซ้าย, 3=ขวา
        
        # ... ตรงนี้คือจุดที่เราต้องเขียนโค้ดอัปเดตพิกัดมด ...
        
        # ตัวแปรที่จะส่งกลับให้ AI
        reward = 0       # คะแนนที่จะได้
        done = False     # เกมจบหรือยัง? (เช่น เก็บอาหารได้ถือว่าจบเกม)
        
        return self._get_state(), reward, done