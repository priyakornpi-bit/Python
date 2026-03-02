import random
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

