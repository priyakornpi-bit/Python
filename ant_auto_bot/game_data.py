# ไฟล์: game_data.py

class AntCard:
    def __init__(self, name, cost_food, cost_chitin, hp, damage, role):
        self.name = name
        self.cost_food = cost_food       # ราคาที่ต้องใช้ Food
        self.cost_chitin = cost_chitin   # ราคาที่ต้องใช้ Chitin
        self.hp = hp                     # พลังชีวิต
        self.damage = damage             # พลังโจมตี
        self.role = role                 # หน้าที่ของมด
        
    def __str__(self):
        # ฟังก์ชันนี้ทำให้เราปริ้นท์ข้อมูลมดออกมาอ่านง่ายๆ
        return f"[{self.role}] {self.name} | ใช้ Food: {self.cost_food}, Chitin: {self.cost_chitin} | HP: {self.hp}, ATK: {self.damage}"

# ---------------------------------------------------------
# ฐานข้อมูลมด (Knowledge Base) ที่ AI จะดึงไปใช้อ้างอิง
# ---------------------------------------------------------
AVAILABLE_ANTS = {
    "Worker": AntCard(name="Worker", cost_food=10, cost_chitin=0, hp=20, damage=2, role="Gatherer"),
    "Warrior": AntCard(name="Warrior", cost_food=25, cost_chitin=0, hp=100, damage=15, role="Melee"),
    "Ranger": AntCard(name="Ranger", cost_food=30, cost_chitin=5, hp=60, damage=25, role="Ranged"),
    "Tank": AntCard(name="Tank", cost_food=50, cost_chitin=15, hp=250, damage=5, role="Defender")
}

# ส่วนนี้เอาไว้ทดสอบว่าโค้ดทำงานได้ไหม (เวลาเรากดรันเฉพาะไฟล์นี้)
if __name__ == "__main__":
    print("--- 📚 เปิดฐานข้อมูลสมอง AI ---")
    for ant_key, card_data in AVAILABLE_ANTS.items():
        print(card_data)