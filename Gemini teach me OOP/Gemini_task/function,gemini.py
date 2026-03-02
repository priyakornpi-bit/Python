def heal(amount):
    confirm = input("Do you want to heal? (yes/no): ")
    confirm = confirm.lower()
    if confirm == "yes":
        print(f"heal + {amount}")
    else:
        print("Heal cancelled.")


heal(100)
heal(50)