"""
priyakorn pichitmarn
683040494-9
P2 - Password validation
"""
SPECIALS = set("!@#$%^&*?")

def validate_password(passwd: str):
    errors = []
    if len(passwd) < 8:
        errors.append("Password must be at least 8 characters long")
    if not any(c.isupper() for c in passwd):
        errors.append("Password must contain at least one uppercase letter")
    if not any(c.isdigit() for c in passwd):
        errors.append("Password must contain at least one number")
    if not any(c in SPECIALS for c in passwd):
        errors.append("Password must contain at least one special character (!@#$%^&*?)")
    return errors

if __name__ == "__main__":
    passwd = input("Enter your password: ").strip()
    problems = validate_password(passwd)
    if problems:
        for p in problems:
            print(f"- {p}")
    else:
        print("There you go! The password is valid.")