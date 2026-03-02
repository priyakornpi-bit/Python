"""
priyakorn pichitmarn
683040494-9
P3 - Phone number validation
"""
def clean_number(s: str) -> str:
    for ch in (" ", "-", "(", ")"):
        s = s.replace(ch, "")
    return s

def format_phone(num: str) -> str:
    return f"({num[:3]}) {num[3:6]}-{num[6:]}"

if __name__ == "__main__":
    s = input("Enter your phone number: ")
    cleaned = clean_number(s)
    print(f"Phone number (no special char): {cleaned}")

    all_digits = all(ch.isdigit() for ch in cleaned)
    correct_length = len(cleaned) == 10

    if not all_digits:
        print("Not all char are numbers.")
    if not correct_length:
        print("Invalid length.")
    if all_digits and correct_length:
        print(f"Formatted phone number: {format_phone(cleaned)}")

