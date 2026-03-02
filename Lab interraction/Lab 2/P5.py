"""
priyakorn pichitmarn
683040494-9
P5 - Calculator, once again
"""
OPERATORS = {"+", "-", "*", "/", "//", "%", "**"}

def convert_token(s: str):
    """Try int, then float, otherwise keep as string."""
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s

def perform_op(a, op, b):
    """Perform operation or return an error string (without leading tab)."""
    # If either operand is a string -> cannot operate
    if isinstance(a, str) or isinstance(b, str):
        return None, "Cannot operate with strings"

    # Division by zero check for / and //
    if op in ("/", "//") and b == 0:
        return None, "divided by zero"
    if op == "%" and b == 0:
        return None, "divided by zero"

    # Mod with floats not allowed per spec/example
    if op == "%" and (isinstance(a, float) or isinstance(b, float)):
        return None, "Doesn't make any sense to mod with float."

    try:
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            res = a / b
        elif op == "//":
            res = a // b
        elif op == "%":
            res = a % b
        elif op == "**":
            res = a ** b
        else:
            return None, "Unsupported operator"
    except Exception as e:
        return None, str(e)
    return res, None

def process_file(filename: str):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"\tError: {filename} not found")
        return

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()
        print("-----")
        print(f"Processing: {stripped}")
        if stripped == "":
            print(f"\tError: Skipped {stripped}: not 3 terms")
            continue

        parts = stripped.split()
        if len(parts) != 3:
            print(f"\tError: Skipped {stripped}: not 3 terms")
            continue

        left_s, op, right_s = parts
        left = convert_token(left_s)
        right = convert_token(right_s)

        print(f"{left} is {type(left)}, {right} is {type(right)}")

        if isinstance(left, str) or isinstance(right, str):
            print(f"\tError: Cannot operate with strings")
            continue

        if op not in OPERATORS:
            print(f"\tError: Unsupported operator")
            continue

        result, err = perform_op(left, op, right)
        if err:
            print(f"\tError: {err}")
        else:
            print(f"{left} {op} {right} = {result}")

if __name__ == "__main__":
    fname = input("Enter input filename: ")
    process_file(fname)