#Priyakorn Pichitmarn
#683040494-9

# ==================== นำเข้า Libraries ====================
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton, QSizePolicy)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont

# ==================== คลาส Layout เครื่องคิดเลข ====================
class CalculatorLayout(QWidget):
    """
    คลาสสำหรับสร้าง UI เครื่องคิดเลข Windows Standard
    - Header: ปุ่มเมนู, ชื่อ Standard, ปุ่มประวัติ
    - Display: QLineEdit แสดงตัวเลข
    - Buttons: Grid layout สำหรับปุ่มตัวเลขและตัวดำเนินการ
    """
    def __init__(self):
        super().__init__()
        # ==================== สถานะการคำนวณ ====================
        self.current_display = "0"  # ค่าที่แสดงบนหน้าจอ
        self.previous_value = 0  # ตัวเลขตัวแรกสำหรับการคำนวณ
        self.operator = None  # ตัวดำเนินการที่เลือก (+, −, ×, ÷, %)
        self.new_number = True  # True = กำลังเริ่มพิมพ์เลขใหม่
        
        # ==================== Layout หลัก ====================
        main_layout = QVBoxLayout()
        
        # ==================== Header: เมนู + ชื่อ + ประวัติ ====================
        header_layout = QHBoxLayout()
        
        # ปุ่มเมนู (icon ☰ = hamburger menu) - ยังไม่เชื่อมฟังก์ชัน
        menu_btn = QPushButton("☰")
        menu_btn.setMaximumWidth(50)
        menu_btn.setFont(QFont("Arial", 12))
        header_layout.addWidget(menu_btn)
        
        # ชื่อตัวเครื่องคิดเลข (Standard)
        standard_label = QLabel("Standard")
        standard_label.setFont(QFont("Arial", 16, QFont.Bold))
        header_layout.addWidget(standard_label)

        # ช่องว่าง เพื่อดันปุ่มประวัติไปทางขวา
        header_layout.addStretch()
        
        # ปุ่มประวัติ (icon 🕐 = นาฬิกา) - ยังไม่เชื่อมฟังก์ชัน
        history_btn = QPushButton("🕐")
        history_btn.setMaximumWidth(50)
        history_btn.setFont(QFont("Arial", 16))
        header_layout.addWidget(history_btn)
        
        main_layout.addLayout(header_layout)
        
        # ==================== หน้าจอแสดงผล ====================
        self.display = QLineEdit()
        self.display.setReadOnly(True)  # อ่านได้เท่านั้น ห้ามแก้ไข
        self.display.setAlignment(Qt.AlignRight)  # ชิดขวา
        self.display.setText("0")  # ค่าเริ่มต้น
        self.display.setMinimumHeight(80)  # ความสูง
        self.display.setFont(QFont("Arial", 32))  # ฟอนต์ใหญ่
        main_layout.addWidget(self.display)
        
        # ==================== Grid Layout สำหรับปุ่ม ====================
        layout = QGridLayout()
        layout.setSpacing(5)  # ระยะห่างระหว่างปุ่ม
        layout.setContentsMargins(5, 5, 5, 5)  # ระยะห่างรอบขอบ
        
        # ฟังก์ชันสร้างปุ่ม
        def create_button(text):
            """สร้างปุ่มและเชื่อมต่อกับ callback"""
            btn = QPushButton(text)
            btn.setMinimumSize(65, 55)  # ขนาดขั้นต่ำ
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # ขยายเต็ม
            btn.setFont(QFont("Arial", 12))
            # เมื่อกดปุ่ม เรียก button_clicked พร้อมนำค่า text
            btn.clicked.connect(lambda checked, t=text: self.button_clicked(t))
            return btn

        # ==================== แถวที่ 1: ปุ่มพิเศษ (%, CE, C, ⌫) ====================
        layout.addWidget(create_button("%"), 1, 0)   # เปอร์เซ็นต์
        layout.addWidget(create_button("CE"), 1, 1)  # Clear Entry (ล้างตัวล่าสุด)
        layout.addWidget(create_button("C"), 1, 2)   # Clear (ล้างทั้งหมด)
        layout.addWidget(create_button("⌫"), 1, 3)   # Backspace (ลบตัวสุดท้าย)

        # ==================== แถวที่ 2: ปุ่มฟังก์ชันวิทยาศาสตร์ ====================
        layout.addWidget(create_button("¹/ₓ"), 2, 0)  # 1 หารด้วย x
        layout.addWidget(create_button("x²"), 2, 1)   # x ยกกำลัง 2
        layout.addWidget(create_button("²√x"), 2, 2)  # รากที่ 2 ของ x
        layout.addWidget(create_button("÷"), 2, 3)    # หาร

        # ==================== แถวที่ 3: ตัวเลข 7, 8, 9 ====================
        layout.addWidget(create_button("7"), 3, 0)
        layout.addWidget(create_button("8"), 3, 1)
        layout.addWidget(create_button("9"), 3, 2)
        layout.addWidget(create_button("×"), 3, 3)    # คูณ

        # ==================== แถวที่ 4: ตัวเลข 4, 5, 6 ====================
        layout.addWidget(create_button("4"), 4, 0)
        layout.addWidget(create_button("5"), 4, 1)
        layout.addWidget(create_button("6"), 4, 2)
        layout.addWidget(create_button("−"), 4, 3)    # ลบ

        # ==================== แถวที่ 5: ตัวเลข 1, 2, 3 ====================
        layout.addWidget(create_button("1"), 5, 0)
        layout.addWidget(create_button("2"), 5, 1)
        layout.addWidget(create_button("3"), 5, 2)
        layout.addWidget(create_button("+"), 5, 3)    # บวก

        # ==================== แถวที่ 6: ตัวเลข 0, จุดทศนิยม, เท่ากับ ====================
        layout.addWidget(create_button("+/-"), 6, 0)  # เปลี่ยนเครื่องหมาย
        layout.addWidget(create_button("0"), 6, 1)
        layout.addWidget(create_button("."), 6, 2)    # จุดทศนิยม
        
        # ปุ่มเท่ากับ สีพิเศษ (สีฟ้า)
        btn_equal = create_button("=")
        btn_equal.setStyleSheet("background-color: #0078D4; color: white;")
        layout.addWidget(btn_equal, 6, 3)

        main_layout.addLayout(layout)
        self.setLayout(main_layout)
    
    # ==================== ฟังก์ชันจัดการปุ่ม ====================
    def button_clicked(self, text):
        """
        ฟังก์ชันสำหรับจัดการเมื่อกดปุ่ม
        
        ตัวอักษร text มาจากปุ่มที่กด
        ตรวจสอบว่าเป็นตัวเลข ตัวดำเนินการ หรือพิเศษ แล้วจัดการให้เหมาะสม
        """
        if text.isdigit():  # ✓ เป็นตัวเลข (0-9)
            if self.current_display == "0":
                # ถ้าแสดง "0" ให้แทนที่ด้วยตัวเลขใหม่
                self.current_display = text
            else:
                # ถ้ามีตัวเลขอยู่แล้ว ให้ต่อเลข
                self.current_display += text
                
        elif text == ".":  # ✓ เป็นจุดทศนิยม
            # ตรวจว่ามี "." อยู่แล้วหรือไม่
            if "." not in self.current_display:
                self.current_display += text
                
        elif text == "C":  # ✓ ปุ่ม Clear (ล้างหมด)
            self.current_display = "0"
            self.operator = None
            self.previous_value = 0
            self.new_number = True
            
        elif text == "CE":  # ✓ ปุ่ม Clear Entry (ล้างตัวล่าสุด)
            self.current_display = "0"
            self.new_number = True
            
        elif text == "⌫":  # ✓ ปุ่ม Backspace (ลบตัวสุดท้าย)
            if len(self.current_display) > 1:
                self.current_display = self.current_display[:-1]
            else:
                self.current_display = "0"
                
        elif text == "+/-":  # ✓ ปุ่มเปลี่ยนเครื่องหมาย
            if self.current_display != "0":
                if self.current_display.startswith("-"):
                    self.current_display = self.current_display[1:]
                else:
                    self.current_display = "-" + self.current_display
                    
        elif text in ["+", "−", "×", "÷", "%"]:  # ✓ ตัวดำเนินการ
            # ถ้ากดตัวดำเนินการซ้ำหลังกรอกเลขตัวที่สอง ให้คำนวณก่อน
            if self.operator is not None and not self.new_number:
                self.calculate()
            
            # เก็บค่าปัจจุบันเป็นตัวเลขตัวแรก และรอเลขตัวที่สอง
            self.previous_value = float(self.current_display)
            self.operator = text
            self.new_number = True
            
        elif text == "=":  # ✓ ปุ่มเท่ากับ
            # คำนวณเมื่อมี operator และพิมพ์เลขตัวที่สองแล้ว
            if self.operator is not None and not self.new_number:
                self.calculate()
        
        elif text == "x²":  # ✓ ยกกำลัง 2
            try:
                val = float(self.current_display)
                self.current_display = str(val ** 2)
            except:
                pass
                
        elif text == "²√x":  # ✓ รากที่ 2
            try:
                val = float(self.current_display)
                self.current_display = str(val ** 0.5)
            except:
                pass
                
        elif text == "¹/ₓ":  # ✓ 1 หารด้วย x
            try:
                val = float(self.current_display)
                if val != 0:
                    self.current_display = str(1 / val)
            except:
                pass

        # อัพเดตหน้าจอให้เห็นค่าใหม่เสมอ
        self.display.setText(self.current_display)
    

# ==================== คลาสหน้าต่างหลัก ====================
class MainWindow(QMainWindow):
    """หน้าต่างหลักของแอปพลิเคชันเครื่องคิดเลข Windows"""
    def __init__(self): 
        super().__init__()

        self.setWindowTitle("Calculator")  # ชื่อหน้าต่าง
        self.setCentralWidget(CalculatorLayout())  # วาง layout ลงไป
        self.resize(320, 470)  # ขนาดหน้าต่าง

# ==================== จุดเริ่มต้นของโปรแกรม ====================
if __name__ == "__main__":
    # สร้าง QApplication (แอปพลิเคชันหลัก)
    app = QApplication(sys.argv)

    # สร้างและแสดงหน้าต่าง
    window = MainWindow()
    window.show()

    # รันลูปเหตุการณ์ (ปล่อยให้ app รันจนกว่าผู้ใช้ปิดหน้าต่าง)
    sys.exit(app.exec())
