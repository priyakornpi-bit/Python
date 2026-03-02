# Python Basic Exercises with Answers

## สารบัญ

- บทที่ 1: Python Learning Roadmap
- บทที่ 2: Python Basics
- บทที่ 3: Control Flow
- บทที่ 4: Functions
- บทที่ 5: Data Structures
- บทที่ 6: File Handling
- บทที่ 7: Object-Oriented Programming (OOP)
- บทที่ 8: Error Handling
- บทที่ 9: Modules and Packages
- บทที่ 10: Review and Summary

# บทที่ 1: Python Learning Roadmap

## ข้อที่ 66: พิมพ์ข้อความ Hello, World!
### 🧠 โจทย์
เขียนโปรแกรมที่พิมพ์ข้อความ 'Hello, World!' ออกมาทางหน้าจอ

### 📌 แนวคิดที่เกี่ยวข้อง
ฟังก์ชัน print เป็นฟังก์ชันพื้นฐานใน Python ที่ใช้สำหรับแสดงผลข้อมูลออกทางหน้าจอ เป็นจุดเริ่มต้นของการเรียนรู้การเขียนโปรแกรม เพราะช่วยให้เห็นผลลัพธ์ของโค้ดได้ทันที การใช้สตริงใน Python สามารถทำได้โดยใช้เครื่องหมายคำพูดคู่หรือเดี่ยว

### 💻 โค้ดตัวอย่าง
```python
print("Hello, World!")
```

### ✅ คำอธิบายคำตอบ
- `print("Hello, World!")`: เรียกใช้ฟังก์ชัน print และส่งสตริง "Hello, World!" เป็นอาร์กิวเมนต์
- ผลลัพธ์ที่ได้คือ Hello, World! แสดงบนหน้าจอ
- เพราะ print จะแสดงค่าที่ส่งเข้าไปโดยตรง ไม่มีการคำนวณเพิ่มเติม

---

## ข้อที่ 67: สร้างตัวแปรและพิมพ์ค่า
### 🧠 โจทย์
สร้างตัวแปรชื่อ 'greeting' ที่มีค่าเป็น 'Hi' และพิมพ์ค่าของตัวแปรนั้นออกมา

### 📌 แนวคิดที่เกี่ยวข้อง
ตัวแปรใน Python ใช้สำหรับเก็บค่าข้อมูล และสามารถอ้างอิงได้โดยชื่อ การกำหนดค่าให้ตัวแปรใช้เครื่องหมาย = การพิมพ์ตัวแปรช่วยให้เห็นค่าที่เก็บอยู่ในหน่วยความจำ

### 💻 โค้ดตัวอย่าง
```python
greeting = "Hi"
print(greeting)
```

### ✅ คำอธิบายคำตอบ
- `greeting = "Hi"`: กำหนดตัวแปร greeting ให้มีค่าเป็นสตริง "Hi"
- `print(greeting)`: พิมพ์ค่าของตัวแปร greeting ออกมา
- ผลลัพธ์คือ Hi เพราะ print แสดงค่าของตัวแปร

---

## ข้อที่ 68: เพิ่มคอมเมนต์เหนือคำสั่ง print
### 🧠 โจทย์
เพิ่มคอมเมนต์เหนือคำสั่ง print เพื่ออธิบายว่าคำสั่งนั้นทำอะไร

### 📌 แนวคิดที่เกี่ยวข้อง
คอมเมนต์ใน Python ใช้ # เพื่อให้โปรแกรมเมอร์อธิบายโค้ด คอมเมนต์จะไม่ถูก execute โดย Python interpreter ช่วยให้โค้ดอ่านง่ายและบำรุงรักษาได้ดี

### 💻 โค้ดตัวอย่าง
```python
# This print statement displays a message
print("Hello")
```

### ✅ คำอธิบายคำตอบ
- `# This print statement displays a message`: คอมเมนต์อธิบายคำสั่งต่อไป
- `print("Hello")`: พิมพ์สตริง "Hello"
- ผลลัพธ์คือ Hello คอมเมนต์ไม่ส่งผลต่อการทำงาน

---

## ข้อที่ 69: โปรแกรมทักทายส่วนตัว
### 🧠 โจทย์
เขียนโปรแกรมที่ถามชื่อผู้ใช้และพิมพ์คำทักทายส่วนตัวออกมา

### 📌 แนวคิดที่เกี่ยวข้อง
ฟังก์ชัน input ใช้รับข้อมูลจากผู้ใช้ การใช้ตัวแปรเพื่อเก็บข้อมูลที่รับมา การรวมสตริงเพื่อสร้างข้อความทักทาย

### 💻 โค้ดตัวอย่าง
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

### ✅ คำอธิบายคำตอบ
- `name = input("What is your name? ")`: รับชื่อจากผู้ใช้และเก็บในตัวแปร name
- `print(f"Hello, {name}!")`: ใช้ f-string เพื่อรวมข้อความกับชื่อ
- ผลลัพธ์ขึ้นกับชื่อที่ผู้ใช้ป้อน เช่น Hello, Alice!

---

## ข้อที่ 70: หาผลรวมของรายการตัวเลข
### 🧠 โจทย์
สร้างรายการที่มีสามตัวเลขและพิมพ์ผลรวมของตัวเลขเหล่านั้น

### 📌 แนวคิดที่เกี่ยวข้อง
ลิสต์ใน Python เป็นโครงสร้างข้อมูลที่เก็บหลายค่า ฟังก์ชัน sum ใช้หาผลรวมของตัวเลขในลิสต์ การเข้าถึงองค์ประกอบในลิสต์ด้วยดัชนี

### 💻 โค้ดตัวอย่าง
```python
numbers = [1, 2, 3]
print(sum(numbers))
```

### ✅ คำอธิบายคำตอบ
- `numbers = [1, 2, 3]`: สร้างลิสต์ที่มีตัวเลข 1, 2, 3
- `print(sum(numbers))`: คำนวณและพิมพ์ผลรวม
- ผลลัพธ์คือ 6 เพราะ 1+2+3=6

---

## ข้อที่ 71: ใช้ f-string จัดรูปแบบข้อความ
### 🧠 โจทย์
ใช้ f-string เพื่อจัดรูปแบบข้อความที่มีตัวแปร

### 📌 แนวคิดที่เกี่ยวข้อง
f-string เป็นวิธีการจัดรูปแบบสตริงใน Python 3.6+ ช่วยให้แทรกตัวแปรเข้าไปในสตริงได้ง่าย ทำให้โค้ดอ่านง่ายและมีประสิทธิภาพ

### 💻 โค้ดตัวอย่าง
```python
age = 25
print(f"I am {age} years old.")
```

### ✅ คำอธิบายคำตอบ
- `age = 25`: กำหนดตัวแปร age
- `print(f"I am {age} years old.")`: ใช้ f-string แทรกค่า age
- ผลลัพธ์คือ I am 25 years old.

---

## ข้อที่ 72: คำนวณพื้นที่วงกลม
### 🧠 โจทย์
เขียนโปรแกรมที่คำนวณพื้นที่วงกลมโดยใช้รัศมีที่ผู้ใช้ป้อน (ใช้ math.pi)

### 📌 แนวคิดที่เกี่ยวข้อง
โมดูล math มีค่าคงที่ pi สำหรับการคำนวณทางคณิตศาสตร์ สูตรพื้นที่วงกลมคือ pi * r^2 การนำเข้าค่าจากโมดูลด้วย import

### 💻 โค้ดตัวอย่าง
```python
import math
r = float(input("Enter radius: "))
area = math.pi * r ** 2
print(f"Area: {area}")
```

### ✅ คำอธิบายคำตอบ
- `import math`: นำเข้าโมดูล math
- `r = float(input("Enter radius: "))`: รับรัศมีและแปลงเป็น float
- `area = math.pi * r ** 2`: คำนวณพื้นที่
- `print(f"Area: {area}")`: พิมพ์ผลลัพธ์
- ผลลัพธ์ขึ้นกับรัศมีที่ป้อน

---

## ข้อที่ 73: สร้างพจนานุกรมและรับข้อมูล
### 🧠 โจทย์
สร้างพจนานุกรมที่มีคีย์ 'name' และ 'age' รับข้อมูลจากผู้ใช้ และพิมพ์ข้อมูลนั้น

### 📌 แนวคิดที่เกี่ยวข้อง
พจนานุกรมเก็บข้อมูลเป็นคู่ key-value การเข้าถึงค่าด้วยคีย์ การรับข้อมูลจากผู้ใช้ด้วย input

### 💻 โค้ดตัวอย่าง
```python
info = {}
info['name'] = input("Enter name: ")
info['age'] = input("Enter age: ")
print(info)
```

### ✅ คำอธิบายคำตอบ
- `info = {}`: สร้างพจนานุกรมว่าง
- `info['name'] = input("Enter name: ")`: เพิ่มคีย์ name
- `info['age'] = input("Enter age: ")`: เพิ่มคีย์ age
- `print(info)`: พิมพ์พจนานุกรม
- ผลลัพธ์เป็น {'name': 'Alice', 'age': '25'} หรือตามที่ป้อน

---

## ข้อที่ 74: ตรวจสอบเลขคู่หรือคี่
### 🧠 โจทย์
เขียนโปรแกรมที่ตรวจสอบว่าตัวเลขเป็นคู่หรือคี่

### 📌 แนวคิดที่เกี่ยวข้อง
ตัวดำเนินการ % หาเศษจากการหาร ถ้า n % 2 == 0 คือเลขคู่ ใช้ if-else สำหรับการตัดสินใจ

### 💻 โค้ดตัวอย่าง
```python
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### ✅ คำอธิบายคำตอบ
- `n = int(input("Enter a number: "))`: รับตัวเลข
- `if n % 2 == 0:`: ตรวจสอบเศษ
- `print("Even")` หรือ `print("Odd")`: พิมพ์ผล
- ผลลัพธ์ขึ้นกับตัวเลขที่ป้อน

---

## ข้อที่ 75: พิมพ์ผลคูณของ 3
### 🧠 โจทย์
ใช้ลูปเพื่อพิมพ์ 5 ผลคูณแรกของ 3

### 📌 แนวคิดที่เกี่ยวข้อง
ลูป for ใช้สำหรับการทำซ้ำ range(1, 6) สร้างลำดับ 1 ถึง 5 การคำนวณ 3 * i สำหรับแต่ละ i

### 💻 โค้ดตัวอย่าง
```python
for i in range(1, 6):
    print(3 * i)
```

### ✅ คำอธิบายคำตอบ
- `for i in range(1, 6):`: ลูป i จาก 1 ถึง 5
- `print(3 * i)`: พิมพ์ 3*i
- ผลลัพธ์คือ 3, 6, 9, 12, 15

---

# บทที่ 2: Python Basics

## ข้อที่ 76: พิมพ์สีที่ชอบ
### 🧠 โจทย์
พิมพ์สีที่คุณชอบออกมา

### 📌 แนวคิดที่เกี่ยวข้อง
การใช้ print เพื่อแสดงสตริง สตริงเป็นชนิดข้อมูลพื้นฐานใน Python การเขียนโค้ดที่เรียบง่ายและตรงไปตรงมา

### 💻 โค้ดตัวอย่าง
```python
print("Blue")
```

### ✅ คำอธิบายคำตอบ
- `print("Blue")`: พิมพ์สตริง "Blue"
- ผลลัพธ์คือ Blue
- โค้ดนี้แสดงการใช้ print พื้นฐาน

---

## ข้อที่ 77: สร้างตัวแปรปีเกิด
### 🧠 โจทย์
สร้างตัวแปรสำหรับปีเกิดของคุณและพิมพ์มันออกมา

### 📌 แนวคิดที่เกี่ยวข้อง
ตัวแปรเก็บค่าต่างๆ ในหน่วยความจำ ชนิดข้อมูล int สำหรับตัวเลขจำนวนเต็ม การพิมพ์ตัวแปรเพื่อแสดงค่า

### 💻 โค้ดตัวอย่าง
```python
birth_year = 1995
print(birth_year)
```

### ✅ คำอธิบายคำตอบ
- `birth_year = 1995`: กำหนดตัวแปร
- `print(birth_year)`: พิมพ์ค่า
- ผลลัพธ์คือ 1995

---

## ข้อที่ 78: เขียนคอมเมนต์อธิบายสตริง
### 🧠 โjoทย์
เขียนคอมเมนต์ที่อธิบายว่าสตริงคืออะไร

### 📌 แนวคิดที่เกี่ยวข้อง
คอมเมนต์ใช้ # และไม่ถูก execute สตริงคือลำดับของตัวอักษร ช่วยให้โค้ดมีเอกสารประกอบ

### 💻 โค้ดตัวอย่าง
```python
# A string is a sequence of characters
print("String example")
```

### ✅ คำอธิบายคำตอบ
- `# A string is a sequence of characters`: คอมเมนต์
- `print("String example")`: พิมพ์สตริง
- ผลลัพธ์คือ String example

---

## ข้อที่ 79: ถามอาหารที่ชอบ
### 🧠 โjoทย์
ถามผู้ใช้ว่าอาหารที่ชอบคืออะไรและพิมพ์มันกลับไป

### 📌 แนวคิดที่เกี่ยวข้อง
input รับข้อมูลจากผู้ใช้ ตัวแปรเก็บข้อมูลที่รับ การแสดงข้อมูลที่รับมา

### 💻 โค้ดตัวอย่าง
```python
food = input("What's your favorite food? ")
print(food)
```

### ✅ คำอธิบายคำตอบ
- `food = input("What's your favorite food? ")`: รับข้อมูล
- `print(food)`: พิมพ์กลับ
- ผลลัพธ์ขึ้นกับที่ผู้ใช้ป้อน

---

## ข้อที่ 80: สร้างลิสต์วันในสัปดาห์
### 🧠 โjoทย์
สร้างลิสต์ของวันในสัปดาห์และพิมพ์วันที่สาม

### 📌 แนวคิดที่เกี่ยวข้อง
ลิสต์เป็นโครงสร้างข้อมูลแบบ mutable ดัชนีเริ่มจาก 0 การเข้าถึงด้วย [2] สำหรับตัวที่สาม

### 💻 โค้ดตัวอย่าง
```python
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(days[2])
```

### ✅ คำอธิบายคำตอบ
- `days = [...]`: สร้างลิสต์
- `print(days[2])`: พิมพ์ตัวที่ 3
- ผลลัพธ์คือ Wednesday

---

## ข้อที่ 81: ใช้ type() ตรวจสอบชนิดข้อมูล
### 🧠 โjoทย์
ใช้ฟังก์ชัน type() เพื่อตรวจสอบชนิดข้อมูลของตัวแปร

### 📌 แนวคิดที่เกี่ยวข้อง
type() คืนค่าชนิดของอ็อบเจกต์ ช่วยในการ debug และตรวจสอบข้อมูล ชนิดข้อมูลพื้นฐาน: int, str, list, etc.

### 💻 โค้ดตัวอย่าง
```python
x = 42
print(type(x))
```

### ✅ คำอธิบายคำตอบ
- `x = 42`: กำหนดตัวแปร
- `print(type(x))`: พิมพ์ชนิด
- ผลลัพธ์คือ <class 'int'>

---

## ข้อที่ 82: แปลงองศาเซลเซียสเป็นฟาเรนไฮต์
### 🧠 โjoทย์
เขียนโปรแกรมที่แปลงองศาเซลเซียสเป็นฟาเรนไฮต์

### 📌 แนวคิดที่เกี่ยวข้อง
สูตร F = C * 9/5 + 32 การคำนวณทางคณิตศาสตร์ใน Python การรับและแสดงผลตัวเลข

### 💻 โค้ดตัวอย่าง
```python
c = float(input("Enter Celsius: "))
f = c * 9/5 + 32
print(f"Fahrenheit: {f}")
```

### ✅ คำอธิบายคำตอบ
- `c = float(input(...))`: รับค่า C
- `f = c * 9/5 + 32`: คำนวณ
- `print(...)`: พิมพ์ผล
- ผลลัพธ์ขึ้นกับค่า C

---

## ข้อที่ 83: สร้างสตริงหลายบรรทัดและนับคำ
### 🧠 โjoทย์
สร้างสตริงหลายบรรทัดและนับจำนวนคำในนั้น

### 📌 แนวคิดที่เกี่ยวข้อง
สตริงหลายบรรทัดใช้ """ หรือ ''' เมธอด split() แยกคำ len() นับจำนวน

### 💻 โค้ดตัวอย่าง
```python
text = """This is a
multi-line string."""
words = text.split()
print(len(words))
```

### ✅ คำอธิบายคำตอบ
- `text = """..."""`: สร้างสตริงหลายบรรทัด
- `words = text.split()`: แยกเป็นลิสต์คำ
- `print(len(words))`: นับและพิมพ์
- ผลลัพธ์คือจำนวนคำ

---

## ข้อที่ 84: ใช้การดำเนินการบูลีน
### 🧠 โjoทย์
ใช้การดำเนินการบูลีนเพื่อตรวจสอบเงื่อนไข

### 📌 แนวคิดที่เกี่ยวข้อง
ตัวดำเนินการ and, or, not ค่าบูลีน True/False การรวมเงื่อนไข

### 💻 โค้ดตัวอย่าง
```python
a = True
b = False
print(a and b)
```

### ✅ คำอธิบายคำตอบ
- `a = True; b = False`: กำหนดค่าบูลีน
- `print(a and b)`: ตรวจสอบ and
- ผลลัพธ์คือ False

---

## ข้อที่ 85: รับข้อมูลและพิมพ์เป็นตัวพิมพ์ใหญ่
### 🧠 โjoทย์
เขียนโปรแกรมที่รับข้อมูลและพิมพ์ออกมาเป็นตัวพิมพ์ใหญ่

### 📌 แนวคิดที่เกี่ยวข้อง
เมธอด upper() ของสตริง input รับสตริง การแปลงตัวพิมพ์

### 💻 โค้ดตัวอย่าง
```python
text = input("Enter text: ")
print(text.upper())
```

### ✅ คำอธิบายคำตอบ
- `text = input(...)`: รับข้อความ
- `print(text.upper())`: แปลงและพิมพ์
- ผลลัพธ์เป็นตัวพิมพ์ใหญ่

---

# บทที่ 3: Control Flow

## ข้อที่ 86: ตรวจสอบตัวเลขบวก
### 🧠 โjoทย์
เขียนคำสั่ง if เพื่อตรวจสอบว่าตัวเลขเป็นบวกหรือไม่

### 📌 แนวคิดที่เกี่ยวข้อง
if statement ใช้สำหรับการตัดสินใจ การเปรียบเทียบด้วย > การทำงานตามเงื่อนไข

### 💻 โค้ดตัวอย่าง
```python
n = 5
if n > 0:
    print("Positive")
```

### ✅ คำอธิบายคำตอบ
- `n = 5`: กำหนดค่า
- `if n > 0:`: ตรวจสอบ
- `print("Positive")`: พิมพ์ถ้าเป็นบวก
- ผลลัพธ์คือ Positive

---

## ข้อที่ 87: พิมพ์ตัวเลข 1 ถึง 5
### 🧠 โjoทย์
ใช้ลูป for เพื่อพิมพ์ตัวเลข 1 ถึง 5

### 📌 แนวคิดที่เกี่ยวข้อง
for loop กับ range() range(1, 6) สร้าง 1,2,3,4,5 การทำซ้ำตามลำดับ

### 💻 โค้ดตัวอย่าง
```python
for i in range(1, 6):
    print(i)
```

### ✅ คำอธิบายคำตอบ
- `for i in range(1, 6):`: ลูป i จาก 1 ถึง 5
- `print(i)`: พิมพ์ i
- ผลลัพธ์คือ 1 2 3 4 5

---

## ข้อที่ 88: ลูป while พิมพ์ Hello
### 🧠 โjoทย์
เขียนลูป while ที่พิมพ์ "Hello" 3 ครั้ง

### 📌 แนวคิดที่เกี่ยวข้อง
while loop ทำงานตราบใดที่เงื่อนไขเป็นจริง ตัวนับเพื่อควบคุมจำนวนรอบ การเพิ่มตัวนับในลูป

### 💻 โค้ดตัวอย่าง
```python
count = 0
while count < 3:
    print("Hello")
    count += 1
```

### ✅ คำอธิบายคำตอบ
- `count = 0`: เริ่มตัวนับ
- `while count < 3:`: ตรวจสอบ
- `print("Hello")`: พิมพ์
- `count += 1`: เพิ่มตัวนับ
- ผลลัพธ์คือ Hello 3 ครั้ง

---

## ข้อที่ 89: ตรวจสอบเลขคู่หรือคี่ด้วย if
### 🧠 โjoทย์
เขียนโปรแกรมที่ตรวจสอบว่าตัวเลขเป็นคู่หรือคี่โดยใช้ if

### 📌 แนวคิดที่เกี่ยวข้อง
% หาเศษ if-else สำหรับสองทางเลือก การตัดสินใจแบบมีเงื่อนไข

### 💻 โค้ดตัวอย่าง
```python
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### ✅ คำอธิบายคำตอบ
- `n = int(input(...))`: รับตัวเลข
- `if n % 2 == 0:`: ตรวจสอบ
- พิมพ์ Even หรือ Odd
- ผลลัพธ์ตามตัวเลข

---

## ข้อที่ 90: หาผลรวมด้วย for loop
### 🧠 โjoทย์
ใช้ลูป for เพื่อหาผลรวมของตัวเลขในลิสต์

### 📌 แนวคิดที่เกี่ยวข้อง
ลูป for วนผ่านองค์ประกอบ ตัวแปรสะสมผลรวม การบวกค่าทีละตัว

### 💻 โค้ดตัวอย่าง
```python
nums = [1, 2, 3, 4]
total = 0
for num in nums:
    total += num
print(total)
```

### ✅ คำอธิบายคำตอบ
- `nums = [1,2,3,4]`: ลิสต์ตัวเลข
- `total = 0`: เริ่มผลรวม
- `for num in nums: total += num`: บวกทีละตัว
- `print(total)`: พิมพ์ 10

---

## ข้อที่ 91: ลูป while กับ break
### 🧠 โjoทย์
ใช้ลูป while ที่มีเงื่อนไข break

### 📌 แนวคิดที่เกี่ยวข้อง
break ออกจากลูปก่อนกำหนด while ทำงานจนเงื่อนไขเป็นเท็จหรือ break การควบคุมการทำงานของลูป

### 💻 โค้ดตัวอย่าง
```python
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
```

### ✅ คำอธิบายคำตอบ
- `i = 0`: เริ่ม
- `while i < 10:`: ลูป
- `print(i)`: พิมพ์
- `if i == 5: break`: ออกเมื่อ i=5
- ผลลัพธ์ 0 ถึง 5

---

## ข้อที่ 92: if-else แยกกลุ่มอายุ
### 🧠 โjoทย์
เขียน if-else แบบซ้อนเพื่อแยกกลุ่มอายุ (เด็ก, วัยรุ่น, ผู้ใหญ่)

### 📌 แนวคิดที่เกี่ยวข้อง
if-elif-else สำหรับหลายเงื่อนไข การเปรียบเทียบช่วงอายุ การตัดสินใจแบบหลายทาง

### 💻 โค้ดตัวอย่าง
```python
age = 15
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
else:
    print("Adult")
```

### ✅ คำอธิบายคำตอบ
- `age = 15`: กำหนดอายุ
- `if age < 13:`: ตรวจเด็ก
- `elif age < 20:`: วัยรุ่น
- `else:`: ผู้ใหญ่
- ผลลัพธ์ Teen

---

## ข้อที่ 93: for loop กับ continue
### 🧠 โjoทย์
ใช้ลูป for กับ continue เพื่อข้ามเลขคู่

### 📌 แนวคิดที่เกี่ยวข้อง
continue ข้ามรอบปัจจุบัน for loop วนตามลำดับ การควบคุมการทำงานในลูป

### 💻 โค้ดตัวอย่าง
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### ✅ คำอธิบายคำตอบ
- `for i in range(10):`: ลูป 0-9
- `if i % 2 == 0: continue`: ข้ามคู่
- `print(i)`: พิมพ์คี่
- ผลลัพธ์ 1,3,5,7,9

---

## ข้อที่ 94: หาตัวเลขใหญ่สุดในลิสต์
### 🧠 โjoทย์
ใช้ลูปเพื่อหาตัวเลขใหญ่สุดในลิสต์

### 📌 แนวคิดที่เกี่ยวข้อง
ตัวแปรเก็บค่าสูงสุด วนลูปเปรียบเทียบ อัปเดตค่าสูงสุด

### 💻 โค้ดตัวอย่าง
```python
nums = [3, 1, 4, 1, 5]
max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num
print(max_num)
```

### ✅ คำอธิบายคำตอบ
- `nums = [...]`: ลิสต์
- `max_num = nums[0]`: เริ่มด้วยตัวแรก
- `for num in nums: if num > max_num: max_num = num`: อัปเดต
- `print(max_num)`: พิมพ์ 5

---

## ข้อที่ 95: while loop ตรวจสอบข้อมูล
### 🧠 โjoทย์
เขียนลูป while ที่ตรวจสอบข้อมูลผู้ใช้จนถูกต้อง

### 📌 แนวคิดที่เกี่ยวข้อง
while วนจนเงื่อนไขเป็นเท็จ การตรวจสอบความถูกต้อง การรับข้อมูลซ้ำ

### 💻 โค้ดตัวอย่าง
```python
while True:
    age = int(input("Enter age: "))
    if age > 0:
        print("Valid")
        break
    else:
        print("Invalid")
```

### ✅ คำอธิบายคำตอบ
- `while True:`: ลูปไม่สิ้นสุด
- `age = int(input(...))`: รับอายุ
- `if age > 0: ... break`: ถาถูกต้อง ออกลูป
- ผลลัพธ์ตามที่ป้อน

---

# บทที่ 4: Functions

## ข้อที่ 96: ฟังก์ชันพิมพ์ Hi
### 🧠 โjoทย์
กำหนดฟังก์ชันที่พิมพ์ "Hi"

### 📌 แนวคิดที่เกี่ยวข้อง
def กำหนดฟังก์ชัน ฟังก์ชันเป็นบล็อกโค้ดที่ใช้ซ้ำ เรียกฟังก์ชันด้วยชื่อ()

### 💻 โค้ดตัวอย่าง
```python
def say_hi():
    print("Hi")

say_hi()
```

### ✅ คำอธิบายคำตอบ
- `def say_hi():`: กำหนดฟังก์ชัน
- `print("Hi")`: พิมพ์ในฟังก์ชัน
- `say_hi()`: เรียกฟังก์ชัน
- ผลลัพธ์ Hi

---

## ข้อที่ 97: ฟังก์ชันทักทายด้วยชื่อ
### 🧠 โjoทย์
สร้างฟังก์ชันที่รับชื่อและทักทาย

### 📌 แนวคิดที่เกี่ยวข้อง
พารามิเตอร์รับค่าเข้า การใช้ตัวแปรในฟังก์ชัน การส่งค่าผ่านฟังก์ชัน

### 💻 โค้ดตัวอย่าง
```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

### ✅ คำอธิบายคำตอบ
- `def greet(name):`: พารามิเตอร์ name
- `print(f"Hello, {name}")`: ใช้ name
- `greet("Alice")`: ส่ง "Alice"
- ผลลัพธ์ Hello, Alice

---

## ข้อที่ 98: lambda หารสอง
### 🧠 โjoทย์
เขียน lambda ที่คูณตัวเลขด้วย 2

### 📌 แนวคิดที่เกี่ยวข้อง
lambda สำหรับฟังก์ชันนิรนาม นิพจน์แบบย่อ ใช้สำหรับการคำนวณง่ายๆ

### 💻 โค้ดตัวอย่าง
```python
double = lambda x: x * 2
print(double(5))
```

### ✅ คำอธิบายคำตอบ
- `double = lambda x: x * 2`: กำหนด lambda
- `print(double(5))`: เรียกและพิมพ์
- ผลลัพธ์ 10

---

## ข้อที่ 99: ฟังก์ชันบวกสองตัวเลข
### 🧠 โjoทย์
เขียนฟังก์ชันที่บวกสองตัวเลขและคืนผลลัพธ์

### 📌 แนวคิดที่เกี่ยวข้อง
return คืนค่า ฟังก์ชันคำนวณและส่งผลกลับ การใช้ค่าที่คืน

### 💻 โค้ดตัวอย่าง
```python
def add(a, b):
    return a + b

print(add(3, 4))
```

### ✅ คำอธิบายคำตอบ
- `def add(a, b): return a + b`: ฟังก์ชันบวก
- `print(add(3, 4))`: พิมพ์ผล
- ผลลัพธ์ 7

---

## ข้อที่ 100: ฟังก์ชันตรวจสอบสตริงว่าง
### 🧠 โjoทย์
สร้างฟังก์ชันที่ตรวจสอบว่าสตริงว่างหรือไม่

### 📌 แนวคิดที่เกี่ยวข้อง
การเปรียบเทียบสตริง คืนค่าบูลีน การใช้ if ในฟังก์ชัน

### 💻 โค้ดตัวอย่าง
```python
def is_empty(s):
    return s == ""

print(is_empty(""))
```

### ✅ คำอธิบายคำตอบ
- `def is_empty(s): return s == ""`: ตรวจสอบ
- `print(is_empty(""))`: พิมพ์ True
- ผลลัพธ์ True

---

## ข้อที่ 101: lambda ใน map ยกกำลังสอง
### 🧠 โjoทย์
ใช้ lambda ใน map เพื่อยกกำลังสองลิสต์

### 📌 แนวคิดที่เกี่ยวข้อง
map ใช้ฟังก์ชันกับแต่ละองค์ lambda เป็นฟังก์ชันนิรนาม list() แปลง map เป็นลิสต์

### 💻 โค้ดตัวอย่าง
```python
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)
```

### ✅ คำอธิบายคำตอบ
- `nums = [1,2,3]`: ลิสต์
- `squared = list(map(lambda x: x**2, nums))`: map ยกกำลัง
- `print(squared)`: [1,4,9]

---

## ข้อที่ 102: ฟังก์ชัน recursive หาแฟกทอเรียล
### 🧠 โjoทย์
เขียนฟังก์ชัน recursive ที่คำนวณแฟกทอเรียล

### 📌 แนวคิดที่เกี่ยวข้อง
recursive เรียกตัวเอง ฐานคือ n==0 return 1 ลดปัญหา n * factorial(n-1)

### 💻 โค้ดตัวอย่าง
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

### ✅ คำอธิบายคำตอบ
- `def factorial(n):`: กำหนด
- `if n == 0: return 1`: ฐาน
- `return n * factorial(n-1)`: recursive
- `print(factorial(5))`: 120

---

## ข้อที่ 103: ฟังก์ชันมี default parameter
### 🧠 โjoทย์
สร้างฟังก์ชันที่มีพารามิเตอร์เริ่มต้น

### 📌 แนวคิดที่เกี่ยวข้อง
default parameter ใช้ = ถ้าไม่ส่ง จะใช้ค่าเริ่มต้น ทำให้ฟังก์ชันยืดหยุ่น

### 💻 โค้ดตัวอย่าง
```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")
```

### ✅ คำอธิบายคำตอบ
- `def greet(name="Guest"):`: default "Guest"
- `greet()`: Hello, Guest
- `greet("Alice")`: Hello, Alice

---

## ข้อที่ 104: ฟังก์ชันเรียงลิสต์เอง
### 🧠 โjoทย์
ใช้ฟังก์ชันที่เรียงลิสต์โดยไม่ใช้ built-in sort

### 📌 แนวคิดที่เกี่ยวข้อง
bubble sort หรือ insertion วนลูปเปรียบเทียบและสลับ การเรียงข้อมูลด้วยตนเอง

### 💻 โค้ดตัวอย่าง
```python
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(sort_list([3,1,4,1,5]))
```

### ✅ คำอธิบายคำตอบ
- `def sort_list(lst):`: ฟังก์ชัน
- ลูปเปรียบเทียบและสลับ
- `print(...)`: [1,1,3,4,5]

---

## ข้อที่ 105: higher-order function
### 🧠 โjoทย์
เขียน higher-order function ที่รับฟังก์ชันเป็นอาร์กิวเมนต์

### 📌 แนวคิดที่เกี่ยวข้อง
ฟังก์ชันที่รับฟังก์ชันอื่น เรียกฟังก์ชันที่ส่งมา ใช้สำหรับการประมวลผลทั่วไป

### 💻 โค้ดตัวอย่าง
```python
def apply_func(func, x):
    return func(x)

print(apply_func(lambda y: y*2, 5))
```

### ✅ คำอธิบายคำตอบ
- `def apply_func(func, x): return func(x)`: รับฟังก์ชัน
- `print(apply_func(lambda y: y*2, 5))`: ส่ง lambda
- ผลลัพธ์ 10

---

# บทที่ 5: Data Structures

## ข้อที่ 106: สร้างลิสต์ผลไม้
### 🧠 โjoทย์
สร้างลิสต์ที่มี 3 ผลไม้และพิมพ์มัน

### 📌 แนวคิดที่เกี่ยวข้อง
ลิสต์เก็บหลายค่า ใช้ [] สร้าง พิมพ์ทั้งลิสต์

### 💻 โค้ดตัวอย่าง
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

### ✅ คำอธิบายคำตอบ
- `fruits = ["apple", "banana", "cherry"]`: ลิสต์
- `print(fruits)`: ['apple', 'banana', 'cherry']

---

## ข้อที่ 107: สร้าง tuple พิกัด
### 🧠 โjoทย์
สร้าง tuple ของพิกัดและเข้าถึงองค์ประกอบแรก

### 📌 แนวคิดที่เกี่ยวข้อง
tuple immutable ใช้ () เข้าถึงด้วย [0] ไม่สามารถเปลี่ยนแปลง

### 💻 โค้ดตัวอย่าง
```python
coords = (10, 20)
print(coords[0])
```

### ✅ คำอธิบายคำตอบ
- `coords = (10, 20)`: tuple
- `print(coords[0])`: 10

---

## ข้อที่ 108: สร้างพจนานุกรม
### 🧠 โjoทย์
สร้างพจนานุกรมด้วยหนึ่งคู่ key-value

### 📌 แนวคิดที่เกี่ยวข้อง
dict ใช้ {} key: value เข้าถึงด้วย key

### 💻 โค้ดตัวอย่าง
```python
person = {"name": "Alice"}
print(person)
```

### ✅ คำอธิบายคำตอบ
- `person = {"name": "Alice"}`: dict
- `print(person)`: {'name': 'Alice'}

---

## ข้อที่ 109: เพิ่มในลิสต์
### 🧠 โjoทย์
เพิ่มรายการในลิสต์และพิมพ์ลิสต์ที่อัปเดต

### 📌 แนวคิดที่เกี่ยวข้อง
append() เพิ่มต่อท้าย ลิสต์ mutable เปลี่ยนแปลงได้

### 💻 โค้ดตัวอย่าง
```python
fruits = ["apple"]
fruits.append("banana")
print(fruits)
```

### ✅ คำอธิบายคำตอบ
- `fruits = ["apple"]`: ลิสต์
- `fruits.append("banana")`: เพิ่ม
- `print(fruits)`: ['apple', 'banana']

---

## ข้อที่ 110: ตรวจสอบ key ใน dict
### 🧠 โjoทย์
ตรวจสอบว่าคีย์มีอยู่ในพจนานุกรมหรือไม่

### 📌 แนวคิดที่เกี่ยวข้อง
in ตรวจสอบ key คืน True/False ใช้สำหรับเงื่อนไข

### 💻 โค้ดตัวอย่าง
```python
d = {"a": 1}
print("a" in d)
```

### ✅ คำอธิบายคำตอบ
- `d = {"a": 1}`: dict
- `print("a" in d)`: True

---

## ข้อที่ 111: เพิ่มใน set
### 🧠 โjoทย์
เพิ่มองค์ประกอบใน set และพิมพ์มัน

### 📌 แนวคิดที่เกี่ยวข้อง
set เก็บ unique add() เพิ่ม ไม่เรียงลำดับ

### 💻 โค้ดตัวอย่าง
```python
s = {1, 2}
s.add(3)
print(s)
```

### ✅ คำอธิบายคำตอบ
- `s = {1, 2}`: set
- `s.add(3)`: เพิ่ม 3
- `print(s)`: {1,2,3}

---

## ข้อที่ 112: ลบซ้ำในลิสต์ด้วย set
### 🧠 โjoทย์
เขียนโปรแกรมลบรายการซ้ำในลิสต์โดยใช้ set

### 📌 แนวคิดที่เกี่ยวข้อง
set ไม่มีซ้ำ แปลงลิสต์เป็น set แล้วกลับ สูญเสียลำดับเดิม

### 💻 โค้ดตัวอย่าง
```python
lst = [1, 2, 2, 3]
unique = list(set(lst))
print(unique)
```

### ✅ คำอธิบายคำตอบ
- `lst = [1,2,2,3]`: ลิสต์มีซ้ำ
- `unique = list(set(lst))`: แปลงเป็น set แล้ว list
- `print(unique)`: [1,2,3]

---

## ข้อที่ 113: นับความถี่คำด้วย dict
### 🧠 โjoทย์
ใช้พจนานุกรมเพื่อนับความถี่ของคำในสตริง

### 📌 แนวคิดที่เกี่ยวข้อง
split() แยกคำ dict เก็บ count get() เริ่มจาก 0

### 💻 โค้ดตัวอย่าง
```python
text = "hello world hello"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
```

### ✅ คำอธิบายคำตอบ
- `words = text.split()`: ['hello', 'world', 'hello']
- `for word in words: freq[word] = freq.get(word, 0) + 1`: นับ
- `print(freq)`: {'hello': 2, 'world': 1}

---

## ข้อที่ 114: list comprehension กรองเลขคู่
### 🧠 โjoทย์
ใช้ list comprehension เพื่อกรองเลขคู่

### 📌 แนวคิดที่เกี่ยวข้อง
[expr for item in list if condition] สร้างลิสต์ใหม่ เงื่อนไขกรอง

### 💻 โค้ดตัวอย่าง
```python
nums = [1,2,3,4,5]
evens = [n for n in nums if n % 2 == 0]
print(evens)
```

### ✅ คำอธิบายคำตอบ
- `nums = [1,2,3,4,5]`: ลิสต์
- `evens = [n for n in nums if n % 2 == 0]`: กรองคู่
- `print(evens)`: [2,4]

---

## ข้อที่ 115: เข้าถึง dict ซ้อน
### 🧠 โjoทย์
สร้างพจนานุกรมซ้อนและเข้าถึงค่าลึก

### 📌 แนวคิดที่เกี่ยวข้อง
dict ใน dict เข้าถึงด้วย ['key']['subkey'] โครงสร้างข้อมูลซ้อน

### 💻 โค้ดตัวอย่าง
```python
data = {"user": {"name": "Alice", "age": 25}}
print(data["user"]["name"])
```

### ✅ คำอธิบายคำตอบ
- `data = {"user": {"name": "Alice", "age": 25}}`: dict ซ้อน
- `print(data["user"]["name"])`: Alice

---

# บทที่ 6: File Handling

## ข้อที่ 116: เขียน Hello ในไฟล์
### 🧠 โjoทย์
เขียน "Hello" ลงในไฟล์

### 📌 แนวคิดที่เกี่ยวข้อง
open() เปิดไฟล์ mode 'w' write() เขียน with ปิดอัตโนมัติ

### 💻 โค้ดตัวอย่าง
```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

### ✅ คำอธิบายคำตอบ
- `with open("file.txt", "w") as f:`: เปิดไฟล์
- `f.write("Hello")`: เขียน
- ไฟล์มี "Hello"

---

## ข้อที่ 117: อ่านและพิมพ์ไฟล์
### 🧠 โjoทย์
อ่านเนื้อหาจากไฟล์และพิมพ์ออกมา

### 📌 แนวคิดที่เกี่ยวข้อง
mode 'r' อ่าน read() อ่านทั้งหมด with จัดการไฟล์

### 💻 โค้ดตัวอย่าง
```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
```

### ✅ คำอธิบายคำตอบ
- `with open("file.txt", "r") as f:`: เปิดอ่าน
- `content = f.read()`: อ่าน
- `print(content)`: พิมพ์เนื้อหา

---

## ข้อที่ 118: ตรวจสอบไฟล์มีอยู่
### 🧠 โjoทย์
ตรวจสอบว่าฟァイルมีอยู่หรือไม่

### 📌 แนวคิดที่เกี่ยวข้อง
os.path.exists() คืน True ถ้ามี ใช้สำหรับเงื่อนไข

### 💻 โค้ดตัวอย่าง
```python
import os
print(os.path.exists("file.txt"))
```

### ✅ คำอธิบายคำตอบ
- `import os`: นำเข้า
- `print(os.path.exists("file.txt"))`: True ถ้ามี

---

## ข้อที่ 119: เพิ่มในไฟล์
### 🧠 โjoทย์
เพิ่มข้อความต่อท้ายไฟล์ที่มีอยู่

### 📌 แนวคิดที่เกี่ยวข้อง
mode 'a' append write() เพิ่ม ไม่ลบเนื้อหาเดิม

### 💻 โค้ดตัวอย่าง
```python
with open("file.txt", "a") as f:
    f.write(" World")
```

### ✅ คำอธิบายคำตอบ
- `with open("file.txt", "a") as f:`: เปิดเพิ่ม
- `f.write(" World")`: เพิ่ม
- ไฟล์มี "Hello World"

---

## ข้อที่ 120: อ่านไฟล์ทีละบรรทัด
### 🧠 โjoทย์
อ่านไฟล์ทีละบรรทัด

### 📌 แนวคิดที่เกี่ยวข้อง
readlines() อ่านเป็นลิสต์ หรือ for line in f: แต่ละบรรทัด

### 💻 โค้ดตัวอย่าง
```python
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### ✅ คำอธิบายคำตอบ
- `with open("file.txt", "r") as f:`: เปิด
- `for line in f:`: วนบรรทัด
- `print(line.strip())`: พิมพ์ตัด \n

---

## ข้อที่ 121: เขียนลิสต์สตริงในไฟล์
### 🧠 โjoทย์
เขียนลิสต์ของสตริงลงในไฟล์

### 📌 แนวคิดที่เกี่ยวข้อง
writelines() เขียนลิสต์ แต่ละสตริงเป็นบรรทัด join ด้วย \n

### 💻 โค้ดตัวอย่าง
```python
lines = ["Line 1", "Line 2"]
with open("file.txt", "w") as f:
    f.writelines(line + "\n" for line in lines)
```

### ✅ คำอธิบายคำตอบ
- `lines = ["Line 1", "Line 2"]`: ลิสต์
- `f.writelines(line + "\n" for line in lines)`: เขียนทีละบรรทัด

---

## ข้อที่ 122: คัดลอกไฟล์
### 🧠 โjoทย์
คัดลอกเนื้อหาจากไฟล์หนึ่งไปอีกไฟล์

### 📌 แนวคิดที่เกี่ยวข้อง
อ่านจากไฟล์ต้นทาง เขียนไปปลายทาง with สำหรับทั้งสอง

### 💻 โค้ดตัวอย่าง
```python
with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
    dst.write(src.read())
```

### ✅ คำอธิบายคำตอบ
- `with open("source.txt", "r") as src, open("dest.txt", "w") as dst:`: เปิดสองไฟล์
- `dst.write(src.read())`: คัดลอก

---

## ข้อที่ 123: นับบรรทัดในไฟล์
### 🧠 โjoทย์
นับจำนวนบรรทัดในไฟล์

### 📌 แนวคิดที่เกี่ยวข้อง
readlines() แล้ว len หรือวนลูปนับ len(f.readlines())

### 💻 โค้ดตัวอย่าง
```python
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
```

### ✅ คำอธิบายคำตอบ
- `lines = f.readlines()`: อ่านเป็นลิสต์
- `print(len(lines))`: นับบรรทัด

---

## ข้อที่ 124: จัดการข้อผิดพลาดไฟล์
### 🧠 โjoทย์
จัดการข้อผิดพลาดเมื่อไฟล์ไม่พบ

### 📌 แนวคิดที่เกี่ยวข้อง
FileNotFoundError PermissionError try open

### 💻 โค้ดตัวอย่าง
```python
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

### ✅ คำอธิบายคำตอบ
- `try: with open(...)`: ลองเปิด
- `except FileNotFoundError:`: จับ
- `print("File not found")`: แสดง

---

## ข้อที่ 125: เขียนไฟล์ CSV แบบง่าย
### 🧠 โjoทย์
เขียนไฟล์ CSV แบบง่ายและอ่านกลับ

### 📌 แนวคิดที่เกี่ยวข้อง
เขียนด้วย , คั่น แต่ละบรรทัดเป็น record อ่านและแยกด้วย split

### 💻 โค้ดตัวอย่าง
```python
with open("data.csv", "w") as f:
    f.write("name,age\nAlice,25\nBob,30")

with open("data.csv", "r") as f:
    for line in f:
        print(line.strip().split(","))
```

### ✅ คำอธิบายคำตอบ
- เขียน "name,age\nAlice,25\nBob,30"
- อ่านและ split ด้วย ,

---

# บทที่ 7: Object-Oriented Programming (OOP)

## ข้อที่ 126: คลาสด้วยหนึ่งแอตทริบิวต์
### 🧠 โjoทย์
กำหนดคลาสที่มีหนึ่งแอตทริบิวต์

### 📌 แนวคิดที่เกี่ยวข้อง
class กำหนดคลาส __init__ เริ่มต้น self อ้างอิง instance

### 💻 โค้ดตัวอย่าง
```python
class Dog:
    def __init__(self, name):
        self.name = name
```

### ✅ คำอธิบายคำตอบ
- `class Dog:`: คลาส
- `def __init__(self, name): self.name = name`: เริ่มต้น

---

## ข้อที่ 127: สร้าง instance และพิมพ์แอตทริบิวต์
### 🧠 โjoทย์
สร้าง instance และพิมพ์แอตทริบิวต์

### 📌 แนวคิดที่เกี่ยวข้อง
Dog("Buddy") สร้างอ็อบเจกต์ . เข้าถึงแอตทริบิวต์ พิมพ์ค่า

### 💻 โค้ดตัวอย่าง
```python
dog = Dog("Buddy")
print(dog.name)
```

### ✅ คำอธิบายคำตอบ
- `dog = Dog("Buddy")`: สร้าง
- `print(dog.name)`: Buddy

---

## ข้อที่ 128: เพิ่มเมธอดพิมพ์ข้อความ
### 🧠 โjoทย์
เพิ่มเมธอดที่พิมพ์ข้อความ

### 📌 แนวคิดที่เกี่ยวข้อง
def ในคลาสเป็นเมธอด self พารามิเตอร์แรก เรียกด้วย instance.method()

### 💻 โค้ดตัวอย่าง
```python
class Cat:
    def meow(self):
        print("Meow")

cat = Cat()
cat.meow()
```

### ✅ คำอธิบายคำตอบ
- `def meow(self): print("Meow")`: เมธอด
- `cat = Cat()`: สร้าง
- `cat.meow()`: Meow

---

## ข้อที่ 129: __init__ ด้วยพารามิเตอร์
### 🧠 โjoทย์
ใช้ __init__ ด้วยพารามิเตอร์

### 📌 แนวคิดที่เกี่ยวข้อง
__init__ รับพารามิเตอร์ กำหนดแอตทริบิวต์ เรียกอัตโนมัติเมื่อสร้าง

### 💻 โค้ดตัวอย่าง
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name, p.age)
```

### ✅ คำอธิบายคำตอบ
- `def __init__(self, name, age):`: รับ name, age
- `self.name = name; self.age = age`: กำหนด
- `p = Person("Alice", 25)`: สร้าง
- `print(p.name, p.age)`: Alice 25

---

## ข้อที่ 130: คลาสลูกสืบทอด
### 🧠 โjoทย์
สร้างคลาสลูกที่สืบทอด

### 📌 แนวคิดที่เกี่ยวข้อง
class Sub(Super): สืบทอด ได้แอตทริบิวต์และเมธอดจากพ่อ เพิ่มหรือ override

### 💻 โค้ดตัวอย่าง
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

dog = Dog("Buddy")
print(dog.name)
```

### ✅ คำอธิบายคำตอบ
- `class Dog(Animal):`: สืบทอด
- `dog = Dog("Buddy")`: ใช้ __init__ ของ Animal
- `print(dog.name)`: Buddy

---

## ข้อที่ 131: override เมธอด
### 🧠 โjoทย์
override เมธอดในคลาสลูก

### 📌 แนวคิดที่เกี่ยวข้อง
เมธอดชื่อเดียวกันในลูก แทนที่พ่อ polymorphism

### 💻 โค้ดตัวอย่าง
```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print(dog.speak())
```

### ✅ คำอธิบายคำตอบ
- `class Dog(Animal): def speak(self): return "Woof"`: override
- `dog = Dog()`: สร้าง
- `print(dog.speak())`: Woof

---

## ข้อที่ 132: encapsulation ด้วย private
### 🧠 โjoทย์
ใช้ encapsulation ด้วยแอตทริบิวต์ private

### 📌 แนวคิดที่เกี่ยวข้อง
__ แอตทริบิวต์ private เข้าถึงไม่ได้จากภายนอกโดยตรง ใช้เมธอด getter/setter

### 💻 โค้ดตัวอย่าง
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
print(acc.get_balance())
```

### ✅ คำอธิบายคำตอบ
- `self.__balance = balance`: private
- `def get_balance(self): return self.__balance`: getter
- `print(acc.get_balance())`: 100

---

## ข้อที่ 133: multiple inheritance
### 🧠 โjoทย์
สร้าง multiple inheritance

### 📌 แนวคิดที่เกี่ยวข้อง
class Sub(A, B): สืบทอดหลาย ได้จากทั้งสอง ระวัง conflict

### 💻 โค้ดตัวอย่าง
```python
class A:
    def method_a(self):
        return "A"

class B:
    def method_b(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.method_a(), c.method_b())
```

### ✅ คำอธิบายคำตอบ
- `class C(A, B):`: สืบทอด A และ B
- `c = C()`: สร้าง
- `print(c.method_a(), c.method_b())`: A B

---

## ข้อที่ 134: polymorphism กับลิสต์อ็อบเจกต์
### 🧠 โjoทย์
ใช้ polymorphism กับลิสต์ของอ็อบเจกต์

### 📌 แนวคิดที่เกี่ยวข้อง
เมธอดชื่อเดียวกันพฤติกรรมต่าง วนลูปเรียกเมธอด ขึ้นกับคลาส

### 💻 โค้ดตัวอย่าง
```python
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```

### ✅ คำอธิบายคำตอบ
- `animals = [Dog(), Cat()]`: ลิสต์อ็อบเจกต์
- `for animal in animals: print(animal.speak())`: เรียก speak แต่ละตัว
- Woof Meow (สมมติ Cat มี speak "Meow")

---

## ข้อที่ 135: hierarchy สำหรับ shape
### 🧠 โjoทย์
สร้าง hierarchy คลาสสำหรับ shape

### 📌 แนวคิดที่เกี่ยวข้อง
Shape พ่อ Rectangle, Circle ลูก แต่ละมี area()

### 💻 โค้ดตัวอย่าง
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

rect = Rectangle(4, 5)
print(rect.area())
```

### ✅ คำอธิบายคำตอบ
- `class Rectangle(Shape):`: สืบทอด
- `def area(self): return self.w * self.h`: คำนวณ
- `print(rect.area())`: 20

---

# บทที่ 8: Error Handling

## ข้อที่ 136: try-except หารด้วยศูนย์
### 🧠 โjoทย์
ใช้ try-except สำหรับการหารด้วยศูนย์

### 📌 แนวคิดที่เกี่ยวข้อง
ZeroDivisionError try ลอง except จับ ป้องกัน crash

### 💻 โค้ดตัวอย่าง
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### ✅ คำอธิบายคำตอบ
- `try: result = 10 / 0`: ลองหาร
- `except ZeroDivisionError:`: จับ
- `print("Cannot divide by zero")`: แสดงข้อความ

---

## ข้อที่ 137: จับ ValueError
### 🧠 โjoทย์
จับ ValueError

### 📌 แนวคิดที่เกี่ยวข้อง
ValueError เมื่อแปลงผิด int("abc") ผิด except ValueError

### 💻 โค้ดตัวอย่าง
```python
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
```

### ✅ คำอธิบายคำตอบ
- `try: num = int("abc")`: แปลงผิด
- `except ValueError:`: จับ
- `print("Invalid number")`: แสดง

---

## ข้อที่ 138: พิมพ์ใน finally
### 🧠 โjoทย์
พิมพ์ข้อความใน finally

### 📌 แนวคิดที่เกี่ยวข้อง
finally ทำงานเสมอ หลัง try-except cleanup

### 💻 โค้ดตัวอย่าง
```python
try:
    print("Try")
except:
    print("Except")
finally:
    print("Finally")
```

### ✅ คำอธิบายคำตอบ
- `try: print("Try")`: Try
- `finally: print("Finally")`: Finally เสมอ

---

## ข้อที่ 139: raise custom exception
### 🧠 โjoทย์
raise exception ที่กำหนดเอง

### 📌 แนวคิดที่เกี่ยวข้อง
class MyError(Exception): pass raise MyError("message") except จับ

### 💻 โค้ดตัวอย่าง
```python
class MyError(Exception):
    pass

try:
    raise MyError("Something wrong")
except MyError as e:
    print(e)
```

### ✅ คำอธิบายคำตอบ
- `raise MyError("Something wrong")`: โยน
- `except MyError as e: print(e)`: จับและพิมพ์

---

## ข้อที่ 140: จัดการหลาย exception
### 🧠 โjoทย์
จัดการหลายประเภท exception

### 📌 แนวคิดที่เกี่ยวข้อง
except (Type1, Type2): หรือ except แยก ตามประเภทต่างกัน

### 💻 โค้ดตัวอย่าง
```python
try:
    x = int(input())
    y = 10 / x
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Division error")
```

### ✅ คำอธิบายคำตอบ
- `try: x = int(input()); y = 10 / x`: ลอง
- `except ValueError:`: จับแปลงผิด
- `except ZeroDivisionError:`: จับหารศูนย์

---

## ข้อที่ 141: else กับ try
### 🧠 โjoทย์
ใช้ else กับ try

### 📌 แนวคิดที่เกี่ยวข้อง
else ทำงานถ้าไม่ except หลัง try ไม่มี error สำหรับโค้ดสำเร็จ

### 💻 โค้ดตัวอย่าง
```python
try:
    num = int("5")
except ValueError:
    print("Error")
else:
    print("Success:", num)
```

### ✅ คำอธิบายคำตอบ
- `try: num = int("5")`: สำเร็จ
- `else: print("Success:", num)`: Success: 5

---

## ข้อที่ 142: nested try-except
### 🧠 โjoทย์
ใช้ nested try-except

### 📌 แนวคิดที่เกี่ยวข้อง
try ใน try except ใน except จัดการ error ซ้อน

### 💻 โค้ดตัวอย่าง
```python
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Inner")
except:
    print("Outer")
```

### ✅ คำอธิบายคำตอบ
- `try: try: x = 1 / 0 except: print("Inner")`: Inner
- ไม่มี outer เพราะ inner จับได้

---

## ข้อที่ 143: ฟังก์ชันกับ error handling
### 🧠 โjoทย์
สร้างฟังก์ชันที่มี error handling

### 📌 แนวคิดที่เกี่ยวข้อง
try ในฟังก์ชัน return หรือ raise จัดการในฟังก์ชัน

### 💻 โค้ดตัวอย่าง
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 0))
```

### ✅ คำอธิบายคำตอบ
- `def divide(a, b): try: return a / b except: return "Cannot divide by zero"`: ฟังก์ชัน
- `print(divide(10, 0))`: Cannot divide by zero

---

## ข้อที่ 144: จัดการ file error
### 🧠 โjoทย์
จัดการข้อผิดพลาดของไฟล์

### 📌 แนวคิดที่เกี่ยวข้อง
FileNotFoundError PermissionError try open

### 💻 โค้ดตัวอย่าง
```python
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

### ✅ คำอธิบายคำตอบ
- `try: with open(...)`: ลองเปิด
- `except FileNotFoundError:`: จับ
- `print("File not found")`: แสดง

---

## ข้อที่ 145: retry mechanism
### 🧠 โjoทย์
สร้างกลไก retry ด้วย exception

### 📌 แนวคิดที่เกี่ยวข้อง
ลูป try นับครั้ง break เมื่อสำเร็จ

### 💻 โค้ดตัวอย่าง
```python
attempts = 3
for i in range(attempts):
    try:
        # some operation
        print("Success")
        break
    except:
        print(f"Attempt {i+1} failed")
```

### ✅ คำอธิบายคำตอบ
- `for i in range(3): try: print("Success"); break except: print(f"Attempt {i+1} failed")`: ลอง 3 ครั้ง
- ถ้าสำเร็จ break ถ้าไม่ ลองต่อ

---

# บทที่ 9: Modules and Packages

## ข้อที่ 146: import math ใช้ pi
### 🧠 โjoทย์
import math และใช้ pi

### 📌 แนวคิดที่เกี่ยวข้อง
import math math.pi ค่า pi ใช้ในคำนวณ

### 💻 โค้ดตัวอย่าง
```python
import math
print(math.pi)
```

### ✅ คำอธิบายคำตอบ
- `import math`: นำเข้า
- `print(math.pi)`: 3.14159...

---

## ข้อที่ 147: import datetime พิมพ์ now
### 🧠 โjoทย์
import datetime และพิมพ์เวลาปัจจุบัน

### 📌 แนวคิดที่เกี่ยวข้อง
from datetime import datetime datetime.now() แสดงเวลา

### 💻 โค้ดตัวอย่าง
```python
from datetime import datetime
print(datetime.now())
```

### ✅ คำอธิบายคำตอบ
- `from datetime import datetime`: นำเข้า
- `print(datetime.now())`: เวลาปัจจุบัน

---

## ข้อที่ 148: ใช้ random สร้างตัวเลข
### 🧠 โjoทย์
ใช้ random เพื่อสร้างตัวเลขสุ่ม

### 📌 แนวคิดที่เกี่ยวข้อง
import random random.randint(a, b) สุ่ม integer

### 💻 โค้ดตัวอย่าง
```python
import random
print(random.randint(1, 10))
```

### ✅ คำอธิบายคำตอบ
- `import random`: นำเข้า
- `print(random.randint(1, 10))`: สุ่ม 1-10

---

## ข้อที่ 149: import specific function
### 🧠 โjoทย์
import ฟังก์ชันเฉพาะจากโมดูล

### 📌 แนวคิดที่เกี่ยวข้อง
from module import func ใช้ func โดยตรง ไม่ต้อง module.func

### 💻 โค้ดตัวอย่าง
```python
from math import sqrt
print(sqrt(16))
```

### ✅ คำอธิบายคำตอบ
- `from math import sqrt`: นำเข้าเฉพาะ
- `print(sqrt(16))`: 4.0

---

## ข้อที่ 150: สร้างโมดูลและ import
### 🧠 โjoทย์
สร้างโมดูลง่ายๆ และ import มัน

### 📌 แนวคิดที่เกี่ยวข้อง
ไฟล์ .py เป็นโมดูล import mymodule เรียกฟังก์ชันจากนั้น

### 💻 โค้ดตัวอย่าง
# ใน mymodule.py
def hello():
    print("Hello from module")

# ใน main.py
import mymodule
mymodule.hello()
```

### ✅ คำอธิบายคำตอบ
- สร้าง mymodule.py ด้วย def hello()
- `import mymodule`: นำเข้า
- `mymodule.hello()`: Hello from module

---

## ข้อที่ 151: ใช้ os รายชื่อไดเรกทอรี
### 🧠 โjoทย์
ใช้ os เพื่อรายชื่อไดเรกทอรี

### 📌 แนวคิดที่เกี่ยวข้อง
import os os.listdir(path) ลิสต์ไฟล์และโฟลเดอร์

### 💻 โค้ดตัวอย่าง
```python
import os
print(os.listdir("."))
```

### ✅ คำอธิบายคำตอบ
- `import os`: นำเข้า
- `print(os.listdir("."))`: รายชื่อใน current dir

---

## ข้อที่ 152: จัดการ import error
### 🧠 โjoทย์
จัดการข้อผิดพลาดในการ import

### 📌 แนวคิดที่เกี่ยวข้อง
try import except ImportError แสดงข้อความถ้าไม่มี

### 💻 โค้ดตัวอย่าง
```python
try:
    import nonexistent
except ImportError:
    print("Module not found")
```

### ✅ คำอธิบายคำตอบ
- `try: import nonexistent`: ลอง
- `except ImportError:`: จับ
- `print("Module not found")`: แสดง

---

## ข้อที่ 153: install และ import third-party
### 🧠 โjoทย์
ติดตั้งและ import โมดูลภายนอก (เช่น requests)

### 📌 แนวคิดที่เกี่ยวข้อง
pip install requests import requests ใช้สำหรับ HTTP

### 💻 โค้ดตัวอย่าง
# ใน terminal: pip install requests
import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
```

### ✅ คำอธิบายคำตอบ
- ติดตั้ง requests
- `import requests`: นำเข้า
- `response = requests.get(...)`: ส่ง request
- `print(response.status_code)`: 200

---

## ข้อที่ 154: สร้าง package ด้วย submodules
### 🧠 โjoทย์
สร้าง package ด้วย submodules

### 📌 แนวคิดที่เกี่ยวข้อง
โฟลเดอร์ __init__.py submodule.py ในโฟลเดอร์ import package.submodule

### 💻 โค้ดตัวอย่าง
# โฟลเดอร์ mypackage/
# __init__.py
# submodule.py: def func(): pass

from mypackage import submodule
submodule.func()
```

### ✅ คำอธิบายคำตอบ
- สร้างโครงสร้าง
- `from mypackage import submodule`: นำเข้า
- `submodule.func()`: เรียก

---

## ข้อที่ 155: จัดการ virtual environments
### 🧠 โjoทย์
จัดการ virtual environments สำหรับ dependencies

### 📌 แนวคิดที่เกี่ยวข้อง
python -m venv myenv source myenv/bin/activate (mac) pip install ใน env แยก dependencies

### 💻 โค้ดตัวอย่าง
# ใน terminal:
python -m venv myenv
source myenv/bin/activate  # mac
pip install requests
python -c "import requests; print('Installed')"
```

### ✅ คำอธิบายคำตอบ
- สร้าง venv
- activate
- install ใน env
- import สำเร็จ

---

# บทที่ 10: Review and Summary

## ข้อที่ 156: รายชื่อ 5 พื้นฐาน Python
### 🧠 โjoทย์
รายชื่อ 5 พื้นฐานของ Python

### 📌 แนวคิดที่เกี่ยวข้อง
syntax, variables, data types, comments, print พื้นฐานที่จำเป็น

### 💻 โค้ดตัวอย่าง
```python
basics = ["Syntax", "Variables", "Data Types", "Comments", "Print"]
print(basics)
```

### ✅ คำอธิบายคำตอบ
- `basics = [...]`: ลิสต์
- `print(basics)`: ['Syntax', 'Variables', 'Data Types', 'Comments', 'Print']

---

## ข้อที่ 157: อธิบายฟังก์ชัน
### 🧠 โjoทย์
อธิบายว่าฟังก์ชันคืออะไร

### 📌 แนวคิดที่เกี่ยวข้อง
ฟังก์ชันคือบล็อกโค้ดที่ใช้ซ้ำ รับ input คืน output def ชื่อ(พารามิเตอร์)

### 💻 โค้ดตัวอย่าง
```python
def explain():
    print("A function is a reusable block of code")

explain()
```

### ✅ คำอธิบายคำตอบ
- `def explain(): print("A function is a reusable block of code")`: กำหนด
- `explain()`: A function is a reusable block of code

---

## ข้อที่ 158: ชื่อ 3 data structures
### 🧠 โjoทย์
ชื่อ 3 โครงสร้างข้อมูล

### 📌 แนวคิดที่เกี่ยวข้อง
list, tuple, dict เก็บและจัดการข้อมูล แต่ละมีลักษณะเฉพาะ

### 💻 โค้ดตัวอย่าง
```python
structures = ["List", "Tuple", "Dictionary"]
print(structures)
```

### ✅ คำอธิบายคำตอบ
- `structures = ["List", "Tuple", "Dictionary"]`: ลิสต์
- `print(structures)`: แสดง

---

## ข้อที่ 159: เขียนคลาสง่ายๆ
### 🧠 โjoทย์
เขียนคลาสง่ายๆ

### 📌 แนวคิดที่เกี่ยวข้อง
class ชื่อ: def __init__(self): pass blueprint สำหรับอ็อบเจกต์

### 💻 โค้ดตัวอย่าง
```python
class SimpleClass:
    pass

obj = SimpleClass()
print("Class created")
```

### ✅ คำอธิบายคำตอบ
- `class SimpleClass: pass`: คลาสว่าง
- `obj = SimpleClass()`: สร้าง instance
- `print("Class created")`: Class created

---

## ข้อที่ 160: จัดการ exception พื้นฐาน
### 🧠 โjoทย์
จัดการ exception พื้นฐาน

### 📌 แนวคิดที่เกี่ยวข้อง
try: code except: handle ป้องกัน error แสดงข้อความ

### 💻 โค้ดตัวอย่าง
```python
try:
    1 / 0
except:
    print("Error occurred")
```

### ✅ คำอธิบายคำตอบ
- `try: 1 / 0`: error
- `except: print("Error occurred")`: จับและแสดง

---

## ข้อที่ 161: import และใช้โมดูล
### 🧠 โjoทย์
import และใช้โมดูล

### 📌 แนวคิดที่เกี่ยวข้อง
import module module.function() ใช้ฟังก์ชันจากภายนอก

### 💻 โค้ดตัวอย่าง
```python
import math
print(math.sqrt(4))
```

### ✅ คำอธิบายคำตอบ
- `import math`: นำเข้า
- `print(math.sqrt(4))`: 2.0

---

## ข้อที่ 162: สร้างโปรแกรมสมบูรณ์ด้วยคลาสและ error handling
### 🧠 โjoทย์
สร้างโปรแกรมสมบูรณ์ด้วยคลาสและ error handling

### 📌 แนวคิดที่เกี่ยวข้อง
รวม OOP และ exception คลาสจัดการข้อมูล try-except ในเมธอด

### 💻 โค้ดตัวอย่าง
```python
class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

calc = Calculator()
print(calc.divide(10, 2))
print(calc.divide(10, 0))
```

### ✅ คำอธิบายคำตอบ
- `class Calculator: def divide(self, a, b): try: return a / b except: return "Cannot divide by zero"`: คลาส
- `calc = Calculator()`: สร้าง
- `print(calc.divide(10, 2))`: 5.0
- `print(calc.divide(10, 0))`: Cannot divide by zero

---

## ข้อที่ 163: สร้างโมดูลและใช้ในสคริปต์อื่น
### 🧠 โjoทย์
สร้างโมดูลและใช้ในสคริปต์อื่น

### 📌 แนวคิดที่เกี่ยวข้อง
ไฟล์ .py เป็นโมดูล import ในไฟล์อื่น เรียกฟังก์ชันข้ามไฟล์

### 💻 โค้ดตัวอย่าง
# mymod.py
def add(x, y):
    return x + y

# main.py
import mymod
print(mymod.add(3, 4))
```

### ✅ คำอธิบายคำตอบ
- สร้าง mymod.py ด้วย def add
- `import mymod`: นำเข้า
- `print(mymod.add(3, 4))`: 7

---

## ข้อที่ 164: ไตร่ตรองการเรียนรู้
### 🧠 โjoทย์
ไตร่ตรองการเรียนรู้

### 📌 แนวคิดที่เกี่ยวข้อง
คิดถึงสิ่งที่เรียน จุดแข็ง จุดอ่อน แผนต่อไป

### 💻 โค้ดตัวอย่าง
```python
reflection = "Learned basics to advanced Python"
print(reflection)
```

### ✅ คำอธิบายคำตอบ
- `reflection = "Learned basics to advanced Python"`: สตริง
- `print(reflection)`: แสดง

---

## ข้อที่ 165: วางแผนโปรเจกต์เล็ก
### 🧠 โjoทย์
วางแผนโปรเจกต์เล็กโดยใช้สิ่งที่เรียน

### 📌 แนวคิดที่เกี่ยวข้อง
เลือกโปรเจกต์ง่าย ใช้ concepts ต่างๆ เช่น calculator, todo list

### 💻 โค้ดตัวอย่าง
```python
plan = "Build a simple calculator using classes and functions"
print(plan)
```

### ✅ คำอธิบายคำตอบ
- `plan = "Build a simple calculator using classes and functions"`: แผน
- `print(plan)`: แสดงแผน