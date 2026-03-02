"""
priyakorn pichitmarn
683040494-9
P5 - Color List
"""
color = []
rcolor = []
while True:
    a = input("Enter a color: ")
    if a == "done":
        break
    color.append(a)

rcolor = color.copy()
rcolor.reverse()

print("Color in order:")
print(*color)
print("Color in reverse:")
print(*rcolor)

a = int(input("Enter color number: "))
print(color[a])