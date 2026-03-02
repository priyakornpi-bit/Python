import random 
class bitchy:
    def __init__(self, hp, name):
        self.name = name
        self.hp = hp
        self.max_hp = 125
        self.speed = 1\
    
    def introduce(self):
        return f"Hello, I'm {self.name}. Don't fuck my pussy!"
    
    def get_hit(self, damage):
        self.hit_damaged = random.randint(1,124)
        self.hp -= self.hit_damaged
        print(f"โดนตบไป {self.hit_damaged} ! เลือดเหลือ {self.hp}")

number_healing = random.randint(50,100)
current_hp = 100

def heal(number_healing):
    print(f"you can heal only {number_healing}")
    confirem_heal = input("confirm healing(y/n): ")
    confiremhealing = confirem_heal.lower()

    if confiremhealing == "y":
        print(f"healing ativate!!! +{number_healing}")
        return number_healing
    else:
        print("canceled!!")
        return 0
hp_gained = heal(number_healing)
current_hp = current_hp + hp_gained
print(f"HP:{current_hp}")
heal(number_healing)
        

# สร้างตัวละคร (ส่งค่า 125 และชื่อ Bitchy เข้าไป ตามที่คุณอยากได้)
p1 = bitchy(125, "Bitchy") 

# สั่งให้แนะนำตัว
print(p1.introduce())