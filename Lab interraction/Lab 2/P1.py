"""
priyakorn pichitmarn
683040494-9
P1 - Driver's license
"""
def check_driving_age():
    current_year = 2024
    try:
        birth_year_input = input("Enter a birth year: ")
        birth_year = int(birth_year_input)
        age = current_year - birth_year
        print(f"Your age is {age}")
        if age < 0 or age > 120:
            print("Invalid age.")
        elif age < 18:
            print("Sorry kid.")
        elif age > 85:
            print("You are good to go.")
            print("Please be extra careful when driving!")
        else:
            print("You are good to go.")
    except ValueError as e:
        print(f"Catch ValueError: {e}")

if __name__ == "__main__":
    check_driving_age()