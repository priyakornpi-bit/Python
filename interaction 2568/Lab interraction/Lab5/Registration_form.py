import sys
# ใช้สำหรับจัดการระบบของ Python เช่น การออกจากโปรแกรม

from PySide6.QtCore import QDate, Qt
# QDate : ใช้จัดการข้อมูลวันที่ (ปี / เดือน / วัน)
# Qt    : ใช้สำหรับจัดตำแหน่ง (Alignment) เช่น จัดข้อความกึ่งกลาง

from PySide6.QtWidgets import (
    QApplication,      # ตัวจัดการแอปพลิเคชัน Qt (จำเป็นต้องมีทุกโปรแกรม GUI)
    QWidget,           # หน้าต่างหลักของโปรแกรม
    QVBoxLayout,       # layout สำหรับจัดวาง widget ในแนวตั้ง (Vertical)
    QHBoxLayout,       # layout สำหรับจัดวาง widget ในแนวนอน (Horizontal)
    QLabel,            # ใช้แสดงข้อความ เช่น ชื่อช่องกรอก
    QLineEdit,         # ช่องกรอกข้อความบรรทัดเดียว (ชื่อ, email, phone)
    QRadioButton,      # ปุ่มตัวเลือกแบบเลือกได้
    QButtonGroup,      # จัดกลุ่ม radio button ให้เลือกได้เพียง 1 ตัว
    QDateEdit,         # ช่องเลือกวันที่ พร้อมปฏิทิน
    QComboBox,         # กล่องตัวเลือกแบบ dropdown
    QTextEdit,         # ช่องกรอกข้อความหลายบรรทัด
    QPushButton        # ปุ่มกด
)


class RegistrationForm(QWidget):
    """หน้าต่างฟอร์มสมัครเรียน"""

    def __init__(self):
        super().__init__()
        # เรียก constructor ของ QWidget

        # ==================================================
        # ตั้งค่าหน้าต่างหลัก
        # ==================================================
        self.setWindowTitle("Registration Form")
        self.resize(400, 600)

        # ==================================================
        # สร้าง Layout หลัก (แนวตั้ง)
        # ==================================================
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # ==================================================
        # หัวข้อฟอร์ม
        # ==================================================
        title_label = QLabel("Student Registration Form")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        main_layout.addWidget(title_label)
        main_layout.addSpacing(25)

        # ==================================================
        # Full Name
        # ==================================================
        name_label = QLabel("Full Name")
        name_edit = QLineEdit()

        main_layout.addWidget(name_label)
        main_layout.addWidget(name_edit)
        main_layout.addSpacing(15)

        # ==================================================
        # Email
        # ==================================================
        email_label = QLabel("Email")
        email_edit = QLineEdit()

        main_layout.addWidget(email_label)
        main_layout.addWidget(email_edit)
        main_layout.addSpacing(15)

        # ==================================================
        # Phone
        # ==================================================
        phone_label = QLabel("Phone")
        phone_edit = QLineEdit()

        main_layout.addWidget(phone_label)
        main_layout.addWidget(phone_edit)
        main_layout.addSpacing(15)

        # ==================================================
        # Gender (Radio Button)
        # ==================================================
        gender_label = QLabel("Gender")
        main_layout.addWidget(gender_label)

        gender_group = QButtonGroup(self)
        gender_layout = QHBoxLayout()

        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        non_binary_radio = QRadioButton("Non-binary")
        prefer_not_radio = QRadioButton("Prefer not to say")

        gender_group.addButton(male_radio)
        gender_group.addButton(female_radio)
        gender_group.addButton(non_binary_radio)
        gender_group.addButton(prefer_not_radio)

        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)
        gender_layout.addWidget(non_binary_radio)
        gender_layout.addWidget(prefer_not_radio)

        main_layout.addLayout(gender_layout)
        main_layout.addSpacing(20)

        # ==================================================
        # Date of Birth
        # ==================================================
        dob_label = QLabel("Date of Birth M/dd/yy")
        main_layout.addWidget(dob_label)

        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDisplayFormat("M/dd/yy")
        date_edit.setDate(QDate(2000, 1, 1))

        main_layout.addWidget(date_edit)
        main_layout.addSpacing(20)

        # ==================================================
        # Program
        # ==================================================
        program_label = QLabel("Program")
        main_layout.addWidget(program_label)

        program_combo = QComboBox()
        program_combo.addItems([
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electical Engineering",
            "Semiconductor Engineering",
            "Mechanical Engineering",
            "Industrial Engineering",
            "Logistic Engineering",
            "Power Engineering",
            "Electronic Engineering",
            "Telecommunication Engineering",
            "Agricultural Engineering",
            "Civil Engineering",
            "ARIS"
        ])

        main_layout.addWidget(program_combo)
        main_layout.addSpacing(20)

        # ==================================================
        # About Yourself / Address
        # ==================================================
        st_inf0_label = QLabel("Tell us a little bit about yourself:")
        main_layout.addWidget(st_inf0_label)

        st_info = QTextEdit()
        st_info.setMaximumHeight(100)

        main_layout.addWidget(st_info)
        main_layout.addSpacing(10)

        # ==================================================
        # Accept Terms
        # ==================================================
        accept_layout = QHBoxLayout()
        accept_radio = QRadioButton("I accept the terms and conditions")

        accept_layout.addWidget(accept_radio)
        main_layout.addLayout(accept_layout)
        main_layout.addSpacing(15)

        # ==================================================
        # Submit Button
        # ==================================================
        register_btn = QPushButton("Submit Register")
        main_layout.addWidget(register_btn)

        # ดัน widget ทั้งหมดขึ้นด้านบน
        main_layout.addStretch()


# ======================================================
# ส่วนเริ่มต้นการทำงานของโปรแกรม
# ======================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())

"""
Program: Student Registration Form (PySide6)

Description:
โปรแกรมนี้เป็นการสร้างฟอร์มสมัครเรียนด้วย PySide6 โดยใช้แนวคิดของ
Widget และ Layout ในการออกแบบส่วนติดต่อผู้ใช้ (GUI)

โครงสร้างหลักของโปรแกรม:
- ใช้ QApplication เป็นตัวจัดการแอปพลิเคชัน GUI
- สร้างหน้าต่างหลักด้วย QWidget
- ใช้ QVBoxLayout เป็น layout หลักในการจัดเรียง widget จากบนลงล่าง
- ใช้ QHBoxLayout สำหรับจัดวาง widget ในแนวนอน เช่น Radio Button

องค์ประกอบภายในฟอร์ม:
1. QLabel
   ใช้แสดงข้อความ เช่น ชื่อฟอร์ม และชื่อช่องกรอกข้อมูล

2. QLineEdit
   ใช้สำหรับกรอกข้อมูลแบบบรรทัดเดียว เช่น Full Name, Email และ Phone

3. QRadioButton และ QButtonGroup
   ใช้สำหรับเลือกเพศ (Gender) โดย QButtonGroup
   ทำหน้าที่ควบคุมให้เลือกได้เพียง 1 ตัวเลือกเท่านั้น

4. QDateEdit
   ใช้สำหรับเลือกวันเกิด (Date of Birth)
   ตั้งค่าให้แสดงปฏิทินแบบ popup และกำหนดค่าเริ่มต้นเป็น
   January 1, 2000

5. QComboBox
   ใช้สำหรับเลือกสาขาวิชา (Program) จากรายการที่กำหนดไว้ล่วงหน้า

6. QTextEdit
   ใช้สำหรับกรอกข้อมูลหลายบรรทัด เช่น แนะนำตัวเอง
   โดยจำกัดความสูงของช่องกรอกไว้ไม่เกิน 100 pixel

7. QRadioButton (Accept Terms)
   ใช้ให้ผู้ใช้ยืนยันการยอมรับเงื่อนไขและข้อตกลง

8. QPushButton
   ใช้เป็นปุ่ม Submit Register สำหรับส่งข้อมูล (ยังไม่เชื่อม signal ตามโจทย์)

คุณสมบัติของโปรแกรม:
- ขนาดหน้าต่าง 400 x 600 pixel
- มีการจัด spacing ระหว่าง widget แบบไม่เท่ากัน
- ใช้ layout เพื่อให้ UI เป็นระเบียบและปรับขนาดอัตโนมัติ
- ยังไม่มีการเชื่อม signal หรือ logic การทำงานของปุ่ม

"""
