import sys
# ใช้สำหรับจัดการระบบของ Python เช่น การออกจากโปรแกรม

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit,
    QRadioButton, QButtonGroup,
    QComboBox, QTextEdit,
    QCheckBox, QPushButton,
    QDateEdit
)
from PyQt6.QtCore import QDate, Qt, QLocale
# QDate   : ใช้กำหนดวันที่
# Qt      : ใช้จัดตำแหน่ง (Alignment)
# QLocale : ใช้กำหนดรูปแบบภาษา / วันที่


class StudentRegistrationForm(QMainWindow):
    """หน้าต่างฟอร์มสมัครเรียน"""

    def __init__(self):
        super().__init__()

        # ==================================================
        # ตั้งค่าหน้าต่างหลัก
        # ==================================================
        self.setWindowTitle("Student Registration")
        self.resize(400, 600)

        # ==================================================
        # Central Widget และ Layout หลัก
        # ==================================================
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # ==================================================
        # หัวข้อฟอร์ม
        # ==================================================
        title_label = QLabel("Student Registration Form")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        main_layout.addWidget(title_label)
        main_layout.addSpacing(25)

        # ==================================================
        # Full Name
        # ==================================================
        name_label = QLabel("Full Name")
        self.name_edit = QLineEdit()

        main_layout.addWidget(name_label)
        main_layout.addWidget(self.name_edit)
        main_layout.addSpacing(15)

        # ==================================================
        # Email
        # ==================================================
        email_label = QLabel("Email")
        self.email_edit = QLineEdit()

        main_layout.addWidget(email_label)
        main_layout.addWidget(self.email_edit)
        main_layout.addSpacing(15)

        # ==================================================
        # Phone
        # ==================================================
        phone_label = QLabel("Phone")
        self.phone_edit = QLineEdit()

        main_layout.addWidget(phone_label)
        main_layout.addWidget(self.phone_edit)
        main_layout.addSpacing(15)

        # ==================================================
        # Gender (Radio Button)
        # ==================================================
        gender_label = QLabel("Gender")
        main_layout.addWidget(gender_label)

        self.gender_group = QButtonGroup(self)
        gender_layout = QHBoxLayout()

        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        nonbinary_radio = QRadioButton("Non-binary")
        prefer_not_radio = QRadioButton("Prefer not to say")

        self.gender_group.addButton(male_radio)
        self.gender_group.addButton(female_radio)
        self.gender_group.addButton(nonbinary_radio)
        self.gender_group.addButton(prefer_not_radio)

        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)
        gender_layout.addWidget(nonbinary_radio)
        gender_layout.addWidget(prefer_not_radio)

        main_layout.addLayout(gender_layout)
        main_layout.addSpacing(20)

        # ==================================================
        # Date of Birth
        # ==================================================
        dob_label = QLabel("Date of Birth")
        main_layout.addWidget(dob_label)

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd/MM/yyyy")
        # QDate(year, month, day)
        self.date_edit.setDate(QDate(2000, 2, 19))
        # PyQt6 uses enum members namespaced under QLocale.Language and QLocale.Country
        self.date_edit.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))
        self.date_edit.setMaximumWidth(200)

        main_layout.addWidget(self.date_edit)
        main_layout.addSpacing(20)

        # ==================================================
        # Program
        # ==================================================
        program_label = QLabel("Program")
        main_layout.addWidget(program_label)

        self.program_combo = QComboBox()
        self.program_combo.setPlaceholderText("Select your program")
        self.program_combo.addItems([
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electrical Engineering",
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

        main_layout.addWidget(self.program_combo)
        main_layout.addSpacing(20)

        # ==================================================
        # About Yourself
        # ==================================================
        about_label = QLabel("Tell us a little bit about yourself:")
        main_layout.addWidget(about_label)

        self.about_text = QTextEdit()
        self.about_text.setMaximumHeight(100)

        main_layout.addWidget(self.about_text)
        main_layout.addSpacing(10)

        # ==================================================
        # Accept Terms
        # ==================================================
        self.terms_checkbox = QCheckBox("I accept the terms and conditions")
        main_layout.addWidget(self.terms_checkbox)
        main_layout.addSpacing(20)

        # ==================================================
        # Submit Button
        # ==================================================
        submit_button = QPushButton("Submit Registration")
        main_layout.addWidget(submit_button)

        main_layout.addStretch()


# ======================================================
# ส่วนเริ่มต้นโปรแกรม
# ======================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentRegistrationForm()
    window.show()
    sys.exit(app.exec())
