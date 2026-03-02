"""
priyakorn pichitmarn
683040494-9
P3m 
"""
from P3f import get_inputs, more_saving

if __name__ == "__main__":
    current = get_inputs()
    new = more_saving(current)
    print(f"You had {current:.2f} Baht.")
    print(f"Now you have {new:.2f} Baht.")