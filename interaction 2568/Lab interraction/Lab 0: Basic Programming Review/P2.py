"""
priyakorn pichitmarn
683040494-9
P2
"""

Number_of_row = int(input("Number of row: "))
Number_of_for_column = int(input("Number of column: "))

mid_row = Number_of_row // 2
mid_col = Number_of_for_column// 2


for r in range(Number_of_row):
    for c in range(Number_of_for_column):
        
        if r == 0 or r == Number_of_row - 1 or c == 0 or c == Number_of_for_column - 1:
            print("*", end=" ")
        elif r == mid_row and c == mid_col:
            print("x", end=" ")
        else:
            print("A", end=" ")
    print()