# 🎓 Python OOP: 100 Exercises (Expert Level)
## ระดับมหาวิทยาลัย + Advanced Concepts

---

## 📊 โครงสร้างการจัดการแบบฝึกหัด

| TIER | Module | Exercises | Level | Focus |
|------|--------|-----------|-------|-------|
| 1️⃣ | Module 2 | Ex 1-10 | ⭐ | Classes & Objects + Factory Pattern |
| 2️⃣ | Module 3 | Ex 11-20 | ⭐⭐ | Methods & Type Hints |
| 3️⃣ | Module 4 | Ex 21-30 | ⭐⭐ | Encapsulation + Validation |
| 4️⃣ | Module 5 | Ex 31-40 | ⭐⭐ | Inheritance + MRO |
| 5️⃣ | Module 6 | Ex 41-50 | ⭐⭐ | Polymorphism + Protocols |
| 6️⃣ | Module 7 | Ex 51-60 | ⭐⭐ | Abstract Classes + Interfaces |
| 7️⃣ | Module 8 | Ex 61-70 | ⭐⭐ | Inner Classes + Composition |
| 8️⃣ | Module 9 | Ex 71-80 | ⭐⭐⭐ | SOLID + Design Patterns |
| 9️⃣ | Advanced | Ex 81-90 | ⭐⭐⭐ | Decorators + Metaclasses |
| 🔟 | Expert | Ex 91-100 | ⭐⭐⭐ | Real-world + Performance |

---

# 🏆 TIER 1: Module 2 - Classes & Objects (Ex 1-10)

## **Ex 1: ⭐ Simple Class Definition**
**Topic:** Basic class structure
**Concepts:** class, attributes, methods, constructor

สร้าง class `Dog` ที่:
- มี attributes: name, breed, age
- มี methods: bark(), get_age_in_dog_years()
- implement constructor ที่รับ parameters

```python
# Expected Output:
# Dog 'Buddy' is a Golden Retriever
# 🐕 Woof! Woof!
# Max is 7 years old (equivalent to 49 in dog years)
```

**Critical Thinking:**
- ทำไม constructor จึงสำคัญ?
- เมื่อไรที่ใช้ self และเมื่อไรไม่ใช้?

---

## **Ex 2: ⭐ Object Identity vs Equality**
**Topic:** `is` vs `==`

สร้าง 3 objects จาก class เดียวกัน และเปรียบเทียบ:
- ใช้ `==` (equality)
- ใช้ `is` (identity)
- ใช้ `id()` เพื่อดู memory address

**Expected Output:**
```
dog1 == dog2: True (same data)
dog1 is dog2: False (different objects)
id(dog1): 140234567890123
id(dog2): 140234567890456
```

**Critical Thinking:**
- เหตุใดจึงต้องแยกความแตกต่าง?
- ใช้ในสถานการณ์ใด?

---

## **Ex 3: ⭐ Class Attributes vs Instance Attributes**
**Topic:** Shared vs unique data

ทำให้เข้าใจความแตกต่างโดย:
- Class attribute: นับจำนวน objects ทั้งหมด
- Instance attributes: ข้อมูลของแต่ละ object

```python
class Counter:
    count = 0  # class attribute
    
    def __init__(self, value):
        self.value = value  # instance attribute
        Counter.count += 1

# Expected Output:
# Counter.count: 3 (ทั้งหมด 3 objects)
# obj1.value: 10
# obj2.value: 20
```

**Critical Thinking:**
- โจทร์ปัญหาเมื่อปนสับ class vs instance attributes?
- ใช้ case ใดเหมาะสมกว่า?

---

## **Ex 4: ⭐⭐ Factory Pattern (Class Method)**
**Topic:** Alternate constructors

สร้าง class `Person` ที่:
- มี normal `__init__`
- มี `@classmethod` factory method สำหรับสร้าง objects แบบต่างๆ

```python
# Normal constructor
person1 = Person("Alice", 25)

# Factory methods
person2 = Person.from_birth_year("Bob", 1995)
person3 = Person.from_string("Charlie,30")
```

**Critical Thinking:**
- เมื่อไรใช้ factory method แทน `__init__`?
- ข้อดี-ข้อเสีย?

---

## **Ex 5: ⭐⭐ Static Method vs Class Method**
**Topic:** `@staticmethod` vs `@classmethod`

สร้าง class `Math` ด้วยทั้งสองประเภท:
- `@staticmethod`: ไม่ต้อง self/cls
- `@classmethod`: ใช้ cls parameter

```python
# Expected:
Math.add(5, 3)  # 8 (static)
Math.from_string("10+5")  # 15 (class method)
```

**Critical Thinking:**
- ความแตกต่างทำให้ผลกระทบอะไร?
- เลือกใช้เมื่อไร?

---

## **Ex 6: ⭐⭐ Object Copying (Shallow vs Deep)**
**Topic:** `copy.copy()` vs `copy.deepcopy()`

สร้าง class `Person` ที่มี nested object (Address):
- ทำ shallow copy
- ทำ deep copy
- แสดงผลความแตกต่าง

```python
# Expected:
# Shallow copy: แก้ address จะส่งผลต่อ original
# Deep copy: แก้ address ไม่มีผล
```

**Critical Thinking:**
- ปัญหาเมื่อลืม deepcopy?
- ใช้ case ในโลกจริง?

---

## **Ex 7: ⭐⭐ Singleton Pattern**
**Topic:** Single instance pattern

สร้าง class `Database` ที่:
- อนุญาต object เพียง 1 ตัวเท่านั้น
- ทุกครั้งที่เรียก `Database()` จะได้ object เดียวกัน

```python
# Expected:
db1 = Database()
db2 = Database()
assert db1 is db2  # True
```

**Critical Thinking:**
- ประโยชน์ของ singleton?
- ปัญหากับ thread safety?

---

## **Ex 8: ⭐⭐ Object Serialization**
**Topic:** JSON/Pickle conversion

สร้าง class ที่:
- Convert to JSON
- Convert from JSON
- Handle nested objects

```python
# Expected:
person = Person("Alice", 25)
json_str = person.to_json()
person2 = Person.from_json(json_str)
assert person == person2
```

**Critical Thinking:**
- ปัญหาความปลอดภัย?
- ข้อแม้เมื่อ serialize?

---

## **Ex 9: ⭐⭐ Repr vs Str**
**Topic:** `__repr__()` vs `__str__()`

สร้าง class `Point` ด้วย:
- `__str__()`: readable for users (เช่น "Point(3, 4)")
- `__repr__()`: for developers (เช่น "Point(x=3, y=4)")

```python
p = Point(3, 4)
print(str(p))   # Output for users
print(repr(p))  # Output for developers
```

**Critical Thinking:**
- เมื่อไรใช้อะไร?
- ทำไมสำคัญ?

---

## **Ex 10: ⭐⭐ Comparison Methods (__eq__, __lt__, __gt__)**
**Topic:** Rich comparison methods

สร้าง class `Student` ด้วย:
- `__eq__()`: เปรียบเทียบ GPA
- `__lt__()`, `__gt__()`: ordering
- `@functools.total_ordering`: auto-generate rest

```python
# Expected:
student1 = Student("Alice", 3.8)
student2 = Student("Bob", 3.5)
assert student1 > student2
sorted([student2, student1])  # Auto-sorts
```

**Critical Thinking:**
- ใช้ทั้งสี่วิธีหรือบาง method?
- `total_ordering` ช่วยอะไร?

---

---

# 🏆 TIER 2: Module 3 - Methods & Type Hints (Ex 11-20)

## **Ex 11: ⭐⭐ Type Hints Basics**
**Topic:** PEP 484 - Type hints

สร้าง class `Calculator` ด้วย type hints:
```python
def add(self, a: int, b: int) -> int:
    return a + b

def divide(self, a: float, b: float) -> float:
    if b == 0:
        raise ValueError("...")
    return a / b
```

**Critical Thinking:**
- ทำไม type hints ช่วย?
- ใช้ mypy ตรวจสอบยังไง?

---

## **Ex 12: ⭐⭐ Type Hints with Collections**
**Topic:** List, Dict, Optional

```python
from typing import List, Dict, Optional, Union

class Database:
    def get_users(self) -> List[str]:
        pass
    
    def get_user_info(self, user_id: int) -> Dict[str, Any]:
        pass
    
    def find_user(self, name: str) -> Optional['User']:
        pass
```

**Critical Thinking:**
- `Optional` vs `Union` เมื่อไร?
- Generic types สำคัญไหม?

---

## **Ex 13: ⭐⭐ Method Overloading Simulation**
**Topic:** Multiple signatures (simulate overload)

```python
from functools import singledispatch

class Converter:
    def convert(self, value):
        # dispatch based on type
        if isinstance(value, int):
            return str(value)
        elif isinstance(value, str):
            return int(value)
```

**Critical Thinking:**
- Python มี true overloading หรือไม่?
- ทางเลือกคืออะไร?

---

## **Ex 14: ⭐⭐ Method Chaining**
**Topic:** Fluent interface

```python
class QueryBuilder:
    def select(self, *cols):
        self.columns = cols
        return self  # return self for chaining
    
    def where(self, condition):
        self.condition = condition
        return self
    
    def build(self):
        return f"SELECT {self.columns} WHERE {self.condition}"

# Usage:
query = QueryBuilder().select('id', 'name').where('age > 18').build()
```

**Critical Thinking:**
- ประโยชน์ของ method chaining?
- ปัญหาอะไร?

---

## **Ex 15: ⭐⭐ Keyword-only Arguments**
**Topic:** `*` separator

```python
class Config:
    def __init__(self, name, *, debug=False, timeout=30):
        # ต้องส่ง debug และ timeout ด้วย keyword เท่านั้น
        self.name = name
        self.debug = debug
        self.timeout = timeout

# Valid:
Config("app", debug=True, timeout=60)

# Invalid:
Config("app", True, 60)  # TypeError
```

**Critical Thinking:**
- ประโยชน์ของ keyword-only?
- เมื่อไรใช้?

---

## **Ex 16: ⭐⭐ Default Mutable Arguments Pitfall**
**Topic:** Dangerous default arguments

```python
# ❌ WRONG
class Container:
    def add_item(self, item, items=[]):  # Mutable default!
        items.append(item)
        return items

# ✅ CORRECT
class Container:
    def add_item(self, item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items
```

**Critical Thinking:**
- เหตุใดจึงเป็นปัญหา?
- มีวิธีป้องกัน?

---

## **Ex 17: ⭐⭐ VarArgs (*args, **kwargs)**
**Topic:** Variable arguments

```python
class Logger:
    def log(self, *args, **kwargs):
        level = kwargs.get('level', 'INFO')
        message = ' '.join(str(arg) for arg in args)
        print(f"[{level}] {message}")

# Usage:
logger.log("User", "login", "success", level="INFO")
logger.log("Error:", "Connection failed", level="ERROR")
```

**Critical Thinking:**
- `*args` vs `**kwargs` เมื่อไร?
- ใช้ยังไงอย่างถูก?

---

## **Ex 18: ⭐⭐ Callback Methods**
**Topic:** Function/method as parameter

```python
class Button:
    def __init__(self, label, callback):
        self.label = label
        self.callback = callback
    
    def click(self):
        self.callback()

def on_click():
    print("Button clicked!")

button = Button("Submit", on_click)
button.click()
```

**Critical Thinking:**
- Event handling ทำงานยังไง?
- ใช้ lambda ได้ยังไง?

---

## **Ex 19: ⭐⭐ Context Manager Protocol**
**Topic:** `__enter__`, `__exit__`

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage with 'with' statement:
with FileHandler("data.txt") as f:
    data = f.read()
```

**Critical Thinking:**
- Context manager ช่วยเรื่องอะไร?
- `__exit__` parameters คืออะไร?

---

## **Ex 20: ⭐⭐ Iterator Protocol**
**Topic:** `__iter__()`, `__next__()`

```python
class CountUp:
    def __init__(self, max):
        self.current = 0
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current

# Usage:
for num in CountUp(5):
    print(num)  # 1, 2, 3, 4, 5
```

**Critical Thinking:**
- Generator vs Iterator?
- ใช้ `yield` หรือ iterator protocol?

---

---

# 🏆 TIER 3: Module 4 - Encapsulation (Ex 21-30)

## **Ex 21: ⭐⭐ Private Attributes Naming Convention**
**Topic:** `_` vs `__`

```python
class Account:
    def __init__(self):
        self._balance = 1000    # Protected (weak private)
        self.__pin = 1234       # Private (name mangling)
    
    def get_balance(self):
        return self._balance

# Account name mangling:
# account.__pin → account._Account__pin
```

**Critical Thinking:**
- Naming convention vs enforcement?
- Python ไม่ enforce หรือ?

---

## **Ex 22: ⭐⭐ Name Mangling Pitfall**
**Topic:** Subclass access

```python
class Parent:
    def __init__(self):
        self.__private = "secret"

class Child(Parent):
    def access_parent_private(self):
        # ❌ Can't access self.__private (mangled to Parent.__private)
        # ✅ Can access self._Parent__private (if really needed)
        pass
```

**Critical Thinking:**
- Name mangling มีประโยชน์?
- หรือควรใช้ `_protected` แทน?

---

## **Ex 23: ⭐⭐ Property Decorator Pattern**
**Topic:** Lazy initialization

```python
class User:
    def __init__(self, name):
        self._name = name
        self._email_cache = None
    
    @property
    def email(self):
        if self._email_cache is None:
            self._email_cache = self._fetch_email()  # Expensive operation
        return self._email_cache
    
    def _fetch_email(self):
        # Simulate DB query
        return f"{self._name.lower()}@example.com"

# Usage:
user = User("Alice")
print(user.email)  # Fetch once
print(user.email)  # From cache
```

**Critical Thinking:**
- Caching pattern ทำไมสำคัญ?
- ปัญหาเมื่อ invalidate cache?

---

## **Ex 24: ⭐⭐ Property Validation**
**Topic:** Setter validation

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = None
        self.celsius = celsius  # Use setter for validation
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Usage:
temp = Temperature(25)
temp.celsius = -273.16  # Raises ValueError
```

**Critical Thinking:**
- Validation ที่ไหนเหมาะ? Property setter or method?
- Error handling strategy?

---

## **Ex 25: ⭐⭐ Computed Properties**
**Topic:** Properties without backing field

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        """Computed on-the-fly"""
        return 3.14159 * self.radius ** 2
    
    @property
    def diameter(self):
        return 2 * self.radius

# Usage:
circle = Circle(5)
print(circle.area)  # 78.54... (no backing field!)
```

**Critical Thinking:**
- ใช้ property หรือ method?
- Performance impact?

---

## **Ex 26: ⭐⭐ Data Classes (@dataclass)**
**Topic:** PEP 557 - Automatic implementation

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"
    skills: list = field(default_factory=list)  # Mutable default

# Auto-generates: __init__, __repr__, __eq__, __hash__
person = Person("Alice", 25)
```

**Critical Thinking:**
- `@dataclass` vs manual `__init__`?
- `field(default_factory=list)` ทำไมจำเป็น?

---

## **Ex 27: ⭐⭐ Descriptor Protocol**
**Topic:** `__get__()`, `__set__()`, `__delete__()`

```python
class PositiveInt:
    """Descriptor for positive integers"""
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Must be positive!")
        obj.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name

class Product:
    price = PositiveInt()
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Usage:
product = Product("Apple", 10)
product.price = -5  # Raises ValueError
```

**Critical Thinking:**
- Descriptor ทำงานยังไง?
- ใช้เมื่อไร? (vs property)

---

## **Ex 28: ⭐⭐⭐ Slots for Memory Optimization**
**Topic:** `__slots__`

```python
class OptimizedPoint:
    __slots__ = ['x', 'y']  # Fixed attributes
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison:
# OptimizedPoint uses much less memory!
```

**Critical Thinking:**
- `__slots__` ประหยัด memory ได้เท่าไร?
- ข้อเสีย?

---

## **Ex 29: ⭐⭐⭐ Weak References**
**Topic:** `weakref` module

```python
import weakref

class Observer:
    def update(self):
        print("Updated!")

subject_ref = weakref.ref(Observer())
# observer = subject_ref()  # Get object if still alive
# observer.update() if observer else print("Observer garbage collected")
```

**Critical Thinking:**
- Circular reference ปัญหา?
- Weak reference แก้ไข?

---

## **Ex 30: ⭐⭐⭐ Custom Attribute Access (__getattr__, __setattr__)**
**Topic:** Dynamic attributes

```python
class FlexibleDict:
    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        return f"Attribute {name} not found"
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            raise AttributeError("Cannot set private attributes!")
        self.__dict__[name] = value

# Usage:
obj = FlexibleDict()
obj.name = "Alice"
obj._private = "secret"  # Raises AttributeError
```

**Critical Thinking:**
- `__getattr__` vs `__getattribute__`?
- ข้อเสีย?

---

---

# 🏆 TIER 4: Module 5 - Inheritance (Ex 31-40)

## **Ex 31: ⭐⭐ Simple Inheritance**
**Topic:** Parent-child relationship

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Expected:
dog = Dog()
assert isinstance(dog, Animal)
assert isinstance(dog, Dog)
```

**Critical Thinking:**
- `isinstance` vs `issubclass`?
- Override คืออะไร?

---

## **Ex 32: ⭐⭐ Super() Usage**
**Topic:** Call parent methods

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def describe(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent __init__
        self.model = model
    
    def describe(self):
        return super().describe() + f", Model: {self.model}"
```

**Critical Thinking:**
- ทำไม `super()` ดีกว่า `Parent.__init__(self)`?
- Dynamic dispatch ทำงานยังไง?

---

## **Ex 33: ⭐⭐ Multi-level Inheritance Chain**
**Topic:** A → B → C → D

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return super().method() + " -> B"

class C(B):
    def method(self):
        return super().method() + " -> C"

class D(C):
    def method(self):
        return super().method() + " -> D"

# Output:
# "A -> B -> C -> D"
```

**Critical Thinking:**
- MRO (Method Resolution Order) ทำงานยังไง?
- `D.__mro__` ให้อะไร?

---

## **Ex 34: ⭐⭐⭐ Diamond Problem & MRO**
**Topic:** Multiple inheritance with common ancestor

```python
class Animal:
    def speak(self):
        return "Sound"

class Flyer(Animal):
    pass

class Swimmer(Animal):
    pass

class Duck(Flyer, Swimmer):  # Diamond!
    pass

# Which speak() does Duck use?
# Answer: follows C3 linearization (MRO)

# Check:
print(Duck.__mro__)
```

**Critical Thinking:**
- Python แก้ diamond problem ยังไง?
- MRO algorithm คืออะไร?

---

## **Ex 35: ⭐⭐⭐ Cooperative Multiple Inheritance**
**Topic:** Mixins

```python
class Timestamped:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class Loggable:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logs = []

class User(Timestamped, Loggable):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

# All __init__ methods called in correct order!
```

**Critical Thinking:**
- Cooperative inheritance ทำไมต้อง `*args, **kwargs`?
- `super()` chain ทำงาน?

---

## **Ex 36: ⭐⭐ Method Resolution Order (MRO) Deep Dive**
**Topic:** C3 linearization

```python
# Complex inheritance graph
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(C): pass
class F(D, E): pass

# Print MRO:
for cls in F.__mro__:
    print(cls)

# Understand the order!
```

**Critical Thinking:**
- Linearization rules?
- Monotonicity, consistency?

---

## **Ex 37: ⭐⭐ Preventing Inheritance (Final)**
**Topic:** Sealed classes

```python
class Final:
    """Cannot be subclassed"""
    def __init_subclass__(cls, **kwargs):
        raise TypeError(f"Cannot subclass {cls.__name__}")

class MyClass(Final):
    pass

# TypeError: Cannot subclass Final
```

**Critical Thinking:**
- ทำไมต้องป้องกัน subclass?
- ใช้ใน Python ยังไง?

---

## **Ex 38: ⭐⭐ Abstract Base Classes (ABC)**
**Topic:** Force implementation

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2
    
    # Missing perimeter() → TypeError!

# circle = Circle()  # Raises TypeError
```

**Critical Thinking:**
- Interface design pattern?
- `abstractmethod` enforcement?

---

## **Ex 39: ⭐⭐ Template Method Pattern**
**Topic:** Skeleton algorithm in parent

```python
class DataProcessor(ABC):
    def process(self):
        data = self.load_data()
        data = self.transform(data)
        self.save(data)
    
    @abstractmethod
    def load_data(self): pass
    
    @abstractmethod
    def transform(self, data): pass
    
    @abstractmethod
    def save(self, data): pass

# Subclass only implements abstract methods
```

**Critical Thinking:**
- Template method ทำไมดี?
- Inversion of control?

---

## **Ex 40: ⭐⭐⭐ Virtual Subclasses**
**Topic:** Register without inheriting

```python
from abc import ABC

class Container(ABC):
    @abstractmethod
    def __contains__(self, item):
        pass

# Register list as virtual subclass
Container.register(list)

# Now:
assert issubclass(list, Container)
assert isinstance([], Container)

# But list doesn't actually inherit!
```

**Critical Thinking:**
- Virtual subclasses ประโยชน์?
- ใช้ case?

---

---

# 🏆 TIER 5: Module 6 - Polymorphism (Ex 41-50)

## **Ex 41: ⭐⭐ Method Overriding**
**Topic:** Same method name, different behavior

```python
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} with credit card"

class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} via PayPal"

# Usage:
methods = [CreditCard(), PayPal()]
for method in methods:
    print(method.pay(100))  # Different behavior!
```

**Critical Thinking:**
- Polymorphism คืออะไร?
- ทำไมดี?

---

## **Ex 42: ⭐⭐ Duck Typing**
**Topic:** "If it quacks like a duck..."

```python
class Guitar:
    def play(self):
        return "🎸 Strumming..."

class Piano:
    def play(self):
        return "🎹 Playing..."

def perform(instrument):
    # No type checking! Just call play()
    print(instrument.play())

perform(Guitar())  # Works!
perform(Piano())   # Works!
perform("strings") # Crashes! No play() method
```

**Critical Thinking:**
- Static vs dynamic typing?
- Disadvantage ของ duck typing?

---

## **Ex 43: ⭐⭐ Operator Overloading**
**Topic:** `__add__`, `__mul__`, `__eq__`, etc.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Usage:
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Calls __add__
v4 = v1 * 2   # Calls __mul__
```

**Critical Thinking:**
- Operator overloading ทำไมเปลี่ยนแปลง?
- ใช้เมื่อไร?

---

## **Ex 44: ⭐⭐ Reflection (Introspection)**
**Topic:** Examine object at runtime

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice", 25)

# Reflection:
print(dir(person))          # All attributes/methods
print(vars(person))         # Instance __dict__
print(isinstance(person, Person))
print(hasattr(person, 'greet'))
print(getattr(person, 'name'))
print(callable(person.greet))
```

**Critical Thinking:**
- `dir()` vs `vars()`?
- Reflection ใช้เมื่อไร?

---

## **Ex 45: ⭐⭐ Protocol Typing (Structural Subtyping)**
**Topic:** PEP 544 - Runtime-checkable protocols

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self):
        return "🔵"

class Square:
    def draw(self):
        return "⬜"

# Check protocol without inheritance:
def render(obj):
    if isinstance(obj, Drawable):
        print(obj.draw())

render(Circle())  # Works!
```

**Critical Thinking:**
- Structural vs nominal typing?
- Protocol ใช้เมื่อไร?

---

## **Ex 46: ⭐⭐⭐ Type Checking with isinstance**
**Topic:** Smart type checking

```python
def process(obj):
    if isinstance(obj, list):
        return f"List with {len(obj)} items"
    elif isinstance(obj, dict):
        return f"Dict with keys: {obj.keys()}"
    elif isinstance(obj, (int, float)):
        return f"Number: {obj}"
    else:
        return "Unknown type"

# Better approach: use type(obj) only if needed
```

**Critical Thinking:**
- `isinstance` vs `type()`?
- EAFP vs LBYL?

---

## **Ex 47: ⭐⭐ Single Dispatch (Polymorphism by Type)**
**Topic:** `functools.singledispatch`

```python
from functools import singledispatch

@singledispatch
def process(arg):
    print(f"Processing: {arg}")

@process.register(int)
def _(arg):
    print(f"Processing integer: {arg * 2}")

@process.register(str)
def _(arg):
    print(f"Processing string: {arg.upper()}")

# Usage:
process(5)       # Integer version
process("hello") # String version
```

**Critical Thinking:**
- Single dispatch vs multiple dispatch?
- Use case?

---

## **Ex 48: ⭐⭐⭐ Multiple Dispatch Simulation**
**Topic:** Different behavior based on multiple types

```python
from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    def process(self, arg):
        raise NotImplementedError
    
    @process.register(int)
    def _(self, arg):
        return arg * 2
    
    @process.register(str)
    def _(self, arg):
        return arg.upper()

# Usage:
p = Processor()
print(p.process(5))      # 10
print(p.process("hello")) # HELLO
```

**Critical Thinking:**
- True multiple dispatch (ที่บางภาษาสนับสนุน)?
- Python limitations?

---

## **Ex 49: ⭐⭐ Composition over Inheritance**
**Topic:** HAS-A vs IS-A

```python
# ❌ Wrong approach (IS-A)
class Bird(Animal):
    pass

class Penguin(Bird):  # IS-A bird
    def fly(self):
        raise NotImplementedError("Can't fly!")

# ✅ Better approach (HAS-A)
class Bird:
    def __init__(self, name):
        self.name = name
        self.wings = Wings()  # HAS-A wings

class FlyingBird(Bird):
    def fly(self):
        return self.wings.flap()

class Penguin(Bird):
    # Doesn't inherit fly(), uses composition
    pass
```

**Critical Thinking:**
- IS-A vs HAS-A ใช้เมื่อไร?
- Problem with IS-A approach?

---

## **Ex 50: ⭐⭐⭐ Liskov Substitution Principle (LSP)**
**Topic:** Subtypes must be substitutable

```python
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Cannot fly!")

# ❌ LSP Violation!
# Penguin cannot substitute Bird in fly() context

# ✅ Better design:
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def swim(self):
        return "Swimming"
```

**Critical Thinking:**
- LSP ทำไมสำคัญ?
- Consequences ของ LSP violation?

---

---

# 📝 เนื้อหาเพิ่มเติม (Ex 51-100)

## 🏆 TIER 6: Module 7 - Abstract Classes (Ex 51-60)
- Ex 51-55: Abstract methods, multiple abstracts
- Ex 56-60: Abstract properties, factory patterns

## 🏆 TIER 7: Module 8 - Inner Classes (Ex 61-70)
- Ex 61-65: Inner classes, nested structures
- Ex 66-70: Closures, lambda, function objects

## 🏆 TIER 8: Module 9 - SOLID Principles (Ex 71-80)
- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

## 🏆 TIER 9: Advanced (Ex 81-90)
- Ex 81-85: Decorators (@decorator patterns)
- Ex 86-90: Metaclasses, Descriptors advanced

## 🏆 TIER 10: Expert (Ex 91-100)
- Ex 91-95: Real-world projects (e.g., ORM, API)
- Ex 96-100: Performance optimization, memory

---

# 🎯 Learning Recommendations

**สำหรับมือใหม่:**
- เริ่มจาก Ex 1-20 (Module 2-3)
- ทำความเข้าใจพื้นฐาน

**สำหรับระดับกลาง:**
- Ex 21-50 (Module 4-6)
- เข้าใจ design patterns

**สำหรับ Advanced:**
- Ex 51-100 (Module 7-10)
- Master OOP + real-world application

---

# 📌 Summary

แต่ละข้อประกอบด้วย:
1. ✅ **Topic** - หัวข้อหลัก
2. ✅ **Difficulty** - ระดับยาก (⭐, ⭐⭐, ⭐⭐⭐)
3. ✅ **Concepts** - Concepts ที่ต้องรู้
4. ✅ **Code Examples** - โค้ดตัวอย่าง
5. ✅ **Critical Thinking** - คำถามเพื่อคิด
6. ✅ **Expected Output** - Output ที่ควรได้

**ขอให้สำเร็จในการ master Python OOP! 🚀**
