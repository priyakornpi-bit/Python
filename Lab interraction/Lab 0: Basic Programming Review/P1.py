"""
priyakorn pichitmarn
683040494-9
P1
"""
Number_of_row = int(input("Number of row: "))
Number_of_for_column = int(input("Number of column: "))

for i in range(Number_of_row):
    for j in range(Number_of_for_column):
        print(j + 1, end="\t")
    print()