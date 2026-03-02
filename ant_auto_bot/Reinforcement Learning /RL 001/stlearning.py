import gymnasium as gym

# 1. สร้าง Environment และสั่งให้เปิดหน้าต่างเกมด้วย render_mode="human"
env = gym.make("CartPole-v1", render_mode="human")

# 2. เริ่มต้นเกมใหม่ (Reset) เพื่อเตรียมพร้อม
state, info = env.reset()

# 3. สร้างลูปให้เกมเดินหน้าไป 1,000 เฟรม (หรือจนกว่าเราจะปิด)
for step in range(1000):
    # สุ่มเลือกแอคชัน (0 = ดันซ้าย, 1 = ดันขวา)
    action = env.action_space.sample() 
    
    # ส่งแอคชันไปให้ Environment เพื่อขยับรถเข็น
    # ระบบจะส่งค่าสถานะใหม่, รางวัล, และเช็คว่าเกมจบหรือยัง กลับมาให้
    state, reward, terminated, truncated, info = env.step(action)
    
    # ถ้าไม้พลองล้ม หรือรถวิ่งชนขอบ (terminated) ให้รีเซ็ตเกมใหม่
    if terminated or truncated:
        print(f"จบเกมที่เฟรม: {step} ... กำลังเริ่มรอบใหม่!")
        state, info = env.reset()

# 4. ปิดหน้าต่างเกมเมื่อจบลูป
env.close()