"""
Priyakorn Pichitmarn
683040494-9
"""


from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QSpinBox)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import sys

# ================================
# คลาสหลักของแอปพลิเคชัน GUI
# ================================
class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # ตั้งชื่อของหน้าต่าง
        self.setWindowTitle("Product Inventory Manager")
        # ตั้งตำแหน่งและขนาดของหน้าต่าง (x, y, ความกว้าง, ความสูง)
        self.setGeometry(100, 100, 600, 400)

        # สร้างวิดเจตกลาง และเลย์เอาต์หลัก
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # QVBoxLayout จัดวิดเจตแนวตั้ง
        main_layout = QVBoxLayout(central_widget)

        # สร้างเลย์เอาต์สำหรับหมวดอินพุต
        # QHBoxLayout จัดวิดเจตแนวนอน
        input_layout = QHBoxLayout()

        # สร้างช่องกรอกชื่อสินค้า
        input_layout.addWidget(QLabel("Product Name:"))
        self.name_input = QLineEdit()
        # ตั้งข้อความแนะนำในช่องกรอก
        self.name_input.setPlaceholderText("Enter product name")
        input_layout.addWidget(self.name_input)

        # สร้างช่องกรอกจำนวนสินค้า
        input_layout.addWidget(QLabel("Quantity:"))
        self.qty_input = QSpinBox()
        # ตั้งค่าต่ำสุดและสูงสุดของจำนวน
        self.qty_input.setRange(0, 1000)
        input_layout.addWidget(self.qty_input)

        # สร้างปุ่มเพิ่มสินค้า
        # เชื่อมต่อการคลิกปุ่มกับฟังก์ชัน add_product
        self.add_btn = QPushButton("Add Product")
        self.add_btn.clicked.connect(self.add_product)
        input_layout.addWidget(self.add_btn)

        # สร้างปุ่มล้างข้อมูลทั้งหมด
        # เชื่อมต่อการคลิกปุ่มกับฟังก์ชัน clear_all
        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_all)
        input_layout.addWidget(self.clear_btn)

        # เพิ่มเลย์เอาต์อินพุตเข้าไปในเลย์เอาต์หลัก
        main_layout.addLayout(input_layout)

        # สร้างตารางแสดงข้อมูลสินค้า
        # กำหนดจำนวนแถวเริ่มต้นเป็น 0 และจำนวนคอลัมน์เป็น 3
        self.table = QTableWidget(0, 3)
        # ตั้งหัวตารางสำหรับแต่ละคอลัมน์
        self.table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Status"])

        # ตั้งคุณสมบัติเพิ่มเติมของคอลัมน์
        # ให้คอลัมน์สุดท้ายขยายเต็มพื้นที่ว่าง
        self.table.horizontalHeader().setStretchLastSection(True)
        # ตั้งความกว้างของคอลัมน์ชื่อสินค้า (200 พิกเซล)
        self.table.setColumnWidth(0, 200)
        # ตั้งความกว้างของคอลัมน์จำนวน (100 พิกเซล)
        self.table.setColumnWidth(1, 100)

        # เพิ่มตารางเข้าไปในเลย์เอาต์หลัก
        main_layout.addWidget(self.table)

    # ================================
    # ฟังก์ชันเพิ่มสินค้า wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    # ================================
    def add_product(self):
        """เพิ่มสินค้าใหม่เข้าไปในตารางสินค้า"""

        # ดึงข้อมูลสินค้าจากวิดเจตอินพุต
        # .text() ดึงข้อความจาก QLineEdit
        # .strip() ลบช่องว่างด้านหน้าและด้านหลัง
        name = self.name_input.text().strip()
        # .value() ดึงค่าตัวเลขจาก QSpinBox
        qty = self.qty_input.value()

        # ตรวจสอบความถูกต้องของชื่อสินค้า
        # ตรวจสอบว่าชื่อสินค้าไม่ว่างเปล่า
        if not name:
            return

        # กำหนดสถานะเก็บสินค้าจากจำนวนสินค้า
        if qty < 10:
            # สินค้าเหลือน้อย
            status_text = "Low Stock"
            bg_color = QColor("red")
        else:
            # สินค้าพอเพียง
            status_text = "In Stock"
            bg_color = QColor("lightgreen")

        # เพิ่มแถวใหม่ลงในตาราง
        # ดึงจำนวนแถวปัจจุบันในตาราง
        row_position = self.table.rowCount()
        # เพิ่มแถวใหม่ที่ต่ออกจากแถวสุดท้าย
        self.table.insertRow(row_position)

        # สร้างเซลล์ตารางสำหรับแต่ละคอลัมน์
        # QTableWidgetItem แทนข้อมูลในเซลล์เดียว
        name_item = QTableWidgetItem(name)
        qty_item = QTableWidgetItem(str(qty))
        status_item = QTableWidgetItem(status_text)

        # จัดตำแหน่งข้อความให้กึ่งกลาง
        # Qt.AlignCenter จัดตำแหน่งให้อยู่ตรงกลาง
        name_item.setTextAlignment(Qt.AlignCenter)
        qty_item.setTextAlignment(Qt.AlignCenter)
        status_item.setTextAlignment(Qt.AlignCenter)

        # ระบายสีเซลล์สถานะตามจำนวนสินค้า
        # ตั้งสีพื้นหลังตามอย่างสินค้า
        status_item.setBackground(bg_color)
        if qty < 10:
            # ตั้งสีตัวอักษรเป็นขาวเพื่อให้เห็นชัดขึ้นบนพื้นสีแดง
            status_item.setForeground(QColor("white"))

        # เพิ่มเซลล์เข้าไปในตารางตามตำแหน่งแถวและคอลัมน์ที่กำหนด
        self.table.setItem(row_position, 0, name_item)  # คอลัมน์ที่ 0: ชื่อสินค้า
        self.table.setItem(row_position, 1, qty_item)   # คอลัมน์ที่ 1: จำนวน
        self.table.setItem(row_position, 2, status_item) # คอลัมน์ที่ 2: สถานะ

        # ล้างข้อมูลจากช่องอินพุต
        # ล้างข้อความในช่องชื่อสินค้า
        self.name_input.clear()
        # รีเซตจำนวนสินค้าเป็น 0
        self.qty_input.setValue(0)
        # เลื่อนตัวชี้เมาส์กลับไปที่ช่องชื่อสินค้าเพื่อกรอกข้อมูลสินค้าถัดไป
        self.name_input.setFocus()

    # ================================
    # ฟังก์ชันล้างข้อมูล
    # ================================
    def clear_all(self):
        """ล้างข้อมูลสินค้าทั้งหมดจากตาราง"""
        # ตั้งจำนวนแถวเป็น 0 เพื่อลบข้อมูลทั้งหมด
        self.table.setRowCount(0)


# ================================
# ฟังก์ชันหลักของโปรแกรม
# ================================
def main():
    # สร้างอ็อบเจกต์ QApplication (จำเป็นสำหรับแอปพลิเคชัน GUI ทั้งหมด)
    app = QApplication(sys.argv)
    # สร้างและแสดงหน้าต่างหลัก
    window = InventoryApp()
    window.show()
    # เริ่มลูปเหตุการณ์และออกจากโปรแกรมเมื่อปิดหน้าต่าง
    sys.exit(app.exec())


# ================================
# start
# ================================
if __name__ == "__main__":
    # เรียกใช้ฟังก์ชัน main() เฉพาะเมื่อไฟล์นี้ถูกเรียกใช้โดยตรง
    main()