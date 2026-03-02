# ==================== นำเข้า Libraries ====================
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


# ==================== คลาส Layout เครื่องคิดเลข ====================
class CalculatorLayout(QWidget):
    """
    คลาสสำหรับสร้าง UI ของเครื่องคิดเลข
    - สร้างปุ่มสำหรับตัวเลข และตัวดำเนินการ
    - จัดการการคำนวณ
    - แสดงผลลัพธ์บนแสดงผล
    """
    def __init__(self):
        super().__init__()

        # ==================== สร้าง Layout ====================
        layout = QGridLayout()
        layout.setSpacing(10)  # ระยะห่างระหว่างปุ่ม
        layout.setContentsMargins(10, 10, 10, 10)  # ระยะห่างรอบขอบ

        # ==================== หน้าจอแสดงผล ====================
        self.display = QLabel("Standard")  #Standard  
        self.display = QLabel("0")  # แสดงตัวเลข/ผลลัพธ์
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # ชิดขวา
        self.display.setMinimumHeight(80)  # ความสูง
        self.display.setStyleSheet("font-size: 36px;")  # ขนาดฟอนต์
        layout.addWidget(self.display, 0, 0, 2, 4)  # วางแสดงผลให้ยาว 2 แถว 4 คอลัมน์

        # ==================== แถวที่ 2: ปุ่มอื่น ๆ ====================
        self.create_button("⌫", 2, 0, layout, self.on_backspace)  # ลบตัวสุดท้าย
        self.create_button("AC", 2, 1, layout, self.on_clear)  # ล้างหมด
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))  # เปอร์เซ็นต์
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))  # หาร

        # ==================== แถวที่ 3: ตัวเลข 7, 8, 9 ====================
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))  # คูณ

        # ==================== แถวที่ 4: ตัวเลข 4, 5, 6 ====================
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))  # ลบ

        # ==================== แถวที่ 5: ตัวเลข 1, 2, 3 ====================
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))  # บวก

        # ==================== แถวที่ 6: ตัวเลข 0 และปุ่มสุดท้าย ====================
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)  # ปุ่ม 0 ยาว 2 คอลัมน์
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)  # จุดทศนิยม
        self.create_button("=", 6, 3, layout, self.on_equals)  # เท่ากับ

        # ==================== ขยายเต็มขนาด ====================
        # ตั้งให้ทุกคอลัมน์มีความกว้างเท่ากัน
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        # ตั้งให้ทุกแถวมีความสูงเท่ากัน
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        # ==================== ตัวแปรเก็บสถานะเครื่องคิดเลข ====================
        self.current_input = "0"      # เลขที่พิมพ์ล่าสุด
        self.operator = None          # ตัวดำเนินการที่เลือก (+, -, ×, ÷, %)
        self.previous_value = None    # เลขตัวแรกที่ป้อน
        self.new_number = True        # flag: จำเป็นต้องพิมพ์เลขใหม่หรือไม่

    # ==================== ฟังก์ชันสร้างปุ่ม ====================
    def create_button(self, text, row, col, layout, callback):
        """
        สร้างปุ่มและเชื่อมต่อกับการทำงาน
        
        Args:
            text: ข้อความบนปุ่ม
            row: ตำแหน่งแถว
            col: ตำแหน่งคอลัมน์
            layout: Grid layout ที่ใช้
            callback: ฟังก์ชันที่เรียกเมื่อกดปุ่ม
        """
        btn = QPushButton(text)
        layout.addWidget(btn, row, col)
        btn.clicked.connect(callback)

    # ==================== ฟังก์ชันเมื่อกดตัวเลข ====================
    def on_number(self, num):
        """
        เมื่อกดปุ่มตัวเลข (0-9)
        - หากต้องพิมพ์เลขใหม่ ให้แทนที่เลข
        - หากไม่ใช่ ให้ต่อเลขเดิม
        
        ตัวอย่าง:
        1. กด "5" -> แสดง "5"
        2. กด "3" -> แสดง "53" (ต่อเลข)
        3. กด "+" -> new_number = True
        4. กด "2" -> แสดง "2" (เลขใหม่)
        """
        if self.new_number:
            # ✓ flag = True: เพิ่งกดตัวดำเนินการจบแล้ว
            # ต้องเริ่มเลขใหม่
            self.current_input = num
            self.new_number = False
        else:
            # ✗ flag = False: กำลังพิมพ์ตัวเลขต่อเนื่อง
            if self.current_input == "0":
                # ถ้าแสดง "0" ให้แทนที่ (ไม่ใช่ "05")
                self.current_input = num
            else:
                # ต่อเลข: "123" + "4" = "1234"
                self.current_input += num
        
        self.update_display()

    # ==================== ฟังก์ชันเมื่อกดตัวดำเนินการ ====================
    def on_operator(self, op):
        """
        เมื่อกดปุ่มตัวดำเนินการ (+, -, ×, ÷, %)
        - ถ้ามีตัวดำเนินการค้างอยู่ ให้คำนวณเสร็จก่อน
        - เก็บค่าปัจจุบันเป็น previous_value
        - ตั้งค่า flag เพื่อระบุว่าต้องเลขใหม่
        
        ตัวอย่าง: "5 + 3 +"
        1. กด "5" -> current_input = "5"
        2. กด "+" -> previous_value = 5, operator = "+", new_number = True
        3. กด "3" -> current_input = "3"
        4. กด "+" -> on_equals() คำนวณ 5+3=8, แล้วเก็บ 8 เป็น previous_value
        """
        if self.operator is not None and not self.new_number:
            # มีตัวดำเนินการค้างอยู่ คำนวณเลย
            self.on_equals()
        
        self.previous_value = float(self.current_input)
        self.operator = op
        self.new_number = True

    # ==================== ฟังก์ชันเมื่อกดเท่ากับ ====================
    def on_equals(self):
        """
        เมื่อกดปุ่มเท่ากับ
        - คำนวณผลลัพธ์จากค่า previous_value, operator, และ current_input
        - จัดการหารด้วยศูนย์
        - แสดงผลลัพธ์บนหน้าจอ
        
        ตัวอย่าง: "5 + 3 ="
        previous_value = 5
        operator = "+"
        current_input = "3"
        result = 5 + 3 = 8
        """
        if self.operator is None or self.previous_value is None:
            return

        current = float(self.current_input)
        result = 0

        # ทำการคำนวณตามตัวดำเนินการ
        if self.operator == "+":
            result = self.previous_value + current
        elif self.operator == "−":
            result = self.previous_value - current
        elif self.operator == "×":
            result = self.previous_value * current
        elif self.operator == "÷":
            if current != 0:
                result = self.previous_value / current
            else:
                # หารด้วยศูนย์ แสดง Error
                self.current_input = "Error"
                self.update_display()
                return
        elif self.operator == "%":
            result = self.previous_value % current

        # แสดงผลลัพธ์ (เป็นจำนวนเต็มหากไม่มีทศนิยม)
        self.current_input = str(int(result) if result == int(result) else result)
        self.operator = None
        self.previous_value = None
        self.new_number = True
        self.update_display()

    # ==================== ฟังก์ชันเมื่อกดจุดทศนิยม ====================
    def on_decimal(self):
        """
        เมื่อกดปุ่มจุดทศนิยม
        - เพิ่มจุดให้กับเลขปัจจุบัน (หากยังไม่มี)
        - ป้องกันการมีจุดมากกว่า 1 ตัว (เช่น "3.14.159" ผิด)
        
        ตัวอย่าง:
        - "5" + "." = "5."
        - "5." + "." = "5." (ไม่เปลี่ยน)
        - "5." + "2" = "5.2"
        """
        if "." not in self.current_input:
            self.current_input += "."
            self.new_number = False
        self.update_display()

    # ==================== ฟังก์ชันเมื่อกดลบ ====================
    def on_backspace(self):
        """
        เมื่อกดปุ่มลบ (⌫)
        - ลบตัวอักษรตัวสุดท้ายออก
        - หากเป็นตัวเลขตัวสุดท้าย ให้แสดง 0
        
        ตัวอย่าง:
        - "123" + "⌫" = "12"
        - "1" + "⌫" = "0"
        - "5.3" + "⌫" = "5."
        """
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self.new_number = False
        self.update_display()

    # ==================== ฟังก์ชันเมื่อกดล้างหมด ====================
    def on_clear(self):
        """
        เมื่อกดปุ่มล้าง (AC - All Clear)
        - ล้างค่าทั้งหมด
        - รีเซ็ตสถานะเครื่องคิดเลขให้เหมือนตอนเริ่มต้น
        
        ตัวอย่าง: "5 + 3" -> AC -> "0"
        """
        self.current_input = "0"
        self.operator = None
        self.previous_value = None
        self.new_number = True
        self.update_display()

    # ==================== ฟังก์ชันอัพเดตหน้าจอ ====================
    def update_display(self):
        """
        อัพเดตข้อความบนหน้าจอแสดงผล
        ใช้ every time เมื่อ current_input เปลี่ยนแปลง
        เพื่อให้หน้าจอแสดงค่าล่าสุดเสมอ
        """
        self.display.setText(self.current_input)


# ==================== คลาสหน้าต่างหลัก ====================
class MainWindow(QMainWindow):
    """หน้าต่างหลักของแอปพลิเคชันเครื่องคิดเลข"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")  # ชื่อหน้าต่าง
        self.setFixedSize(320, 480)  # ขนาดหน้าต่าง
        self.setCentralWidget(CalculatorLayout())  # วางวิดเจ็ต Layout ลงไป


# ==================== ฟังก์ชัน main ====================
def main():
    """
    ฟังก์ชันหลักเพื่อรันแอปพลิเคชัน
    - สร้าง QApplication
    - สร้าง MainWindow
    - แสดงหน้าต่าง
    - รันลูปเหตุการณ์
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# ==================== จุดเริ่มต้นของโปรแกรม ====================
if __name__ == "__main__":
    main()
