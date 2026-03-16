import sys
import json
import os
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QComboBox,
                               QHeaderView, QMessageBox, QFrame, QGroupBox, QDateEdit,
                               QDialog, QCheckBox, QSpinBox, QDoubleSpinBox)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont

class UserManager:
    """
    คลาสจัดการข้อมูลผู้ใช้
    ฟีเจอร์:
    - บันทึกและโหลดข้อมูล Login (users.json)
    - บันทึกและโหลดข้อมูล Profile (profiles.json)
    - ตรวจสอบการลงทะเบียนและเข้าสู่ระบบ
    - จัดการข้อมูล Profile ของผู้ใช้
    """
    def __init__(self):
        self.users_file = Path("users.json")
        self.profiles_file = Path("profiles.json")
        self.load_users()
        self.load_profiles()

    def load_users(self):
        if self.users_file.exists():
            with open(self.users_file, 'r', encoding='utf-8') as f:
                self.users = json.load(f)
        else:
            self.users = {}
            self.save_users()

    def save_users(self):
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)

    def load_profiles(self):
        # โหลดข้อมูล profile ของผู้ใช้ทั้งหมด
        if self.profiles_file.exists():
            with open(self.profiles_file, 'r', encoding='utf-8') as f:
                self.profiles = json.load(f)
        else:
            self.profiles = {}
            self.save_profiles()

    def save_profiles(self):
        # บันทึกข้อมูล profile ลงไฟล์
        with open(self.profiles_file, 'w', encoding='utf-8') as f:
            json.dump(self.profiles, f, ensure_ascii=False, indent=2)

    def register_user(self, username, password):
        if username in self.users:
            return False, "Username already exists!"
        if len(username) < 3:
            return False, "Username must be at least 3 characters!"
        if len(password) < 4:
            return False, "Password must be at least 4 characters!"
        
        self.users[username] = password
        self.save_users()
        return True, "Registration successful!"

    def login_user(self, username, password):
        if username not in self.users:
            return False, "Username not found!"
        if self.users[username] != password:
            return False, "Incorrect password!"
        return True, "Login successful!"

    def has_profile(self, username):
        # ตรวจสอบว่าผู้ใช้มี profile แล้วหรือไม่
        return username in self.profiles

    def save_user_profile(self, username, profile_data):
        # บันทึกข้อมูล profile ของผู้ใช้
        self.profiles[username] = profile_data
        self.save_profiles()

    def get_user_profile(self, username):
        # ดึงข้อมูล profile ของผู้ใช้
        return self.profiles.get(username, None)

class LoginWindow(QDialog):
    """
    หน้า Login/Register
    มีฟีเจอร์:
    - เข้าสู่ระบบด้วยชื่อผู้ใช้และรหัสผ่าน
    - สมัครสมาชิกใหม่
    - สลับระหว่างโหมด Login และ Register
    """
    def __init__(self, user_manager):
        super().__init__()
        self.user_manager = user_manager
        self.current_user = None
        self.is_register_mode = False
        
        self.setWindowTitle("Calorie Calculator - Login")
        self.setGeometry(400, 300, 400, 300)
        
        self.setStyleSheet("""
            QDialog { background-color: #f0f8ff; }
            QLabel { color: #2f3640; font-size: 12px; }
            QLineEdit { 
                padding: 10px; 
                border: 2px solid #E0E0E0;
                border-radius: 6px; 
                background-color: #FFFACD;
                color: #1a1a1a;
                font-size: 13px;
                font-weight: 500;
            }
            QLineEdit:focus {
                border: 2px solid #2196F3;
                background-color: #FFFEF5;
            }
            QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; font-weight: bold; }
            QPushButton:hover { background-color: #45a049; }
            QPushButton#toggleBtn { background-color: #2196F3; }
            QPushButton#toggleBtn:hover { background-color: #0b7dda; }
        """)
        
        layout = QVBoxLayout()
        
        self.lbl_title = QLabel("Login to Calorie Calculator")
        self.lbl_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2196F3;")
        layout.addWidget(self.lbl_title)
        
        layout.addWidget(QLabel("Username:"))
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Enter username")
        layout.addWidget(self.input_username)
        
        layout.addWidget(QLabel("Password:"))
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Enter password")
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)
        
        # Button layout
        btn_layout = QHBoxLayout()
        
        self.btn_submit = QPushButton("Login")
        self.btn_submit.clicked.connect(self.handle_login)
        btn_layout.addWidget(self.btn_submit)
        
        self.btn_toggle = QPushButton("Register")
        self.btn_toggle.setObjectName("toggleBtn")
        self.btn_toggle.clicked.connect(self.toggle_mode)
        btn_layout.addWidget(self.btn_toggle)
        
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)

    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        
        if self.is_register_mode:
            success, message = self.user_manager.register_user(username, password)
            if success:
                QMessageBox.information(self, "Success", message)
                self.input_username.clear()
                self.input_password.clear()
                self.toggle_mode()
            else:
                QMessageBox.warning(self, "Error", message)
        else:
            success, message = self.user_manager.login_user(username, password)
            if success:
                self.current_user = username
                self.accept()
            else:
                QMessageBox.warning(self, "Error", message)

    def toggle_mode(self):
        self.is_register_mode = not self.is_register_mode
        if self.is_register_mode:
            self.lbl_title.setText("Register New Account")
            self.btn_submit.setText("Register")
            self.btn_toggle.setText("Back to Login")
        else:
            self.lbl_title.setText("Login to Calorie Calculator")
            self.btn_submit.setText("Login")
            self.btn_toggle.setText("Register")
        self.input_username.clear()
        self.input_password.clear()

class ProfileWindow(QDialog):
    """
    หน้าสร้าง/แก้ไข Profile
    รับข้อมูล:
    - ชื่อเต็ม (Full Name)
    - อีเมล (Email)
    - อายุ (Age)
    - ส่วนสูง (Height in cm)
    - น้ำหนักปัจจุบัน (Weight in kg)
    - เพศ (Gender: Male, Female, Other)
    - กรุ๊ปเลือด (Blood Type: O+, O-, A+, A-, B+, B-, AB+, AB-)
    - น้ำหนักเป้าหมาย (Target Weight in kg)
    
    Input สีขาว (#FFFFFF) ขอบสีฟ้า (#2196F3) เปลี่ยนขอบเป็นแดง (#FF6B6B) เมื่อ Focus
    พื้นหลังขาว: #f0f8ff
    """
    def __init__(self, user_manager, username):
        super().__init__()
        self.user_manager = user_manager
        self.username = username
        self.profile_data = None
        
        self.setWindowTitle(f"User Profile - {username}")
        self.setGeometry(350, 250, 500, 650)
        
        # ======== สี input ที่ตัดกับพื้นหลัง: ขาว(#FFFFFF) ขอบสีฟ้า(#2196F3) ========
        # ======== Focus: ขอบแดง(#FF6B6B) พื้นหลังเหลือง(#FFF9E6) ========
        self.setStyleSheet("""
            QDialog { background-color: #f0f8ff; }
            QLabel { color: #2f3640; font-size: 12px; font-weight: bold; }
            QLineEdit { 
                padding: 10px; 
                border: 2px solid #2196F3;
                border-radius: 6px; 
                background-color: #FFFFFF;
                color: #1a1a1a;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #FF6B6B;
                background-color: #FFF9E6;
            }
            QComboBox {
                padding: 8px;
                border: 2px solid #2196F3;
                border-radius: 6px;
                background-color: #FFFFFF;
                color: #1a1a1a;
            }
            QSpinBox, QDoubleSpinBox {
                padding: 8px;
                border: 2px solid #2196F3;
                border-radius: 6px;
                background-color: #FFFFFF;
                color: #1a1a1a;
            }
            QPushButton { background-color: #4CAF50; color: white; padding: 12px; border-radius: 5px; font-weight: bold; }
            QPushButton:hover { background-color: #45a049; }
            QGroupBox { font-weight: bold; border: 2px solid #E0E0E0; border-radius: 5px; margin-top: 10px; color: #2f3640; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; }
        """)
        
        layout = QVBoxLayout()
        
        # ====== ส่วนหัวข้อ ======
        title_label = QLabel("Create Your Profile")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2196F3; margin-bottom: 15px;")
        layout.addWidget(title_label)
        
        # ====== ข้อมูลส่วนตัว ======
        personal_group = QGroupBox("Personal Information")
        personal_layout = QVBoxLayout()
        
        # ชื่อเต็ม
        personal_layout.addWidget(QLabel("Full Name:"))
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Enter your full name")
        personal_layout.addWidget(self.input_name)
        
        # อีเมล
        personal_layout.addWidget(QLabel("Email:"))
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Enter your email (example@gmail.com)")
        personal_layout.addWidget(self.input_email)
        
        personal_group.setLayout(personal_layout)
        layout.addWidget(personal_group)
        
        # ====== ข้อมูลสุขภาพ ======
        health_group = QGroupBox("Health Information")
        health_layout = QVBoxLayout()
        
        # อายุ
        health_layout.addWidget(QLabel("Age (years):"))
        age_layout = QHBoxLayout()
        self.spin_age = QSpinBox()
        self.spin_age.setRange(10, 120)
        self.spin_age.setValue(25)
        age_layout.addWidget(self.spin_age)
        age_layout.addStretch()
        health_layout.addLayout(age_layout)
        
        # ส่วนสูง
        health_layout.addWidget(QLabel("Height (cm):"))
        height_layout = QHBoxLayout()
        self.spin_height = QDoubleSpinBox()
        self.spin_height.setRange(100, 250)
        self.spin_height.setValue(170)
        self.spin_height.setSingleStep(1)
        height_layout.addWidget(self.spin_height)
        height_layout.addStretch()
        health_layout.addLayout(height_layout)
        
        # น้ำหนัก
        health_layout.addWidget(QLabel("Weight (kg):"))
        weight_layout = QHBoxLayout()
        self.spin_weight = QDoubleSpinBox()
        self.spin_weight.setRange(20, 200)
        self.spin_weight.setValue(70)
        self.spin_weight.setSingleStep(0.1)
        weight_layout.addWidget(self.spin_weight)
        weight_layout.addStretch()
        health_layout.addLayout(weight_layout)
        
        # เพศ
        health_layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()
        self.combo_gender = QComboBox()
        self.combo_gender.addItems(["Male", "Female", "Other"])
        gender_layout.addWidget(self.combo_gender)
        gender_layout.addStretch()
        health_layout.addLayout(gender_layout)
        
        # กรุ๊ปเลือด
        health_layout.addWidget(QLabel("Blood Type:"))
        blood_layout = QHBoxLayout()
        self.combo_blood = QComboBox()
        self.combo_blood.addItems(["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
        blood_layout.addWidget(self.combo_blood)
        blood_layout.addStretch()
        health_layout.addLayout(blood_layout)
        
        # น้ำหนักเป้าหมาย
        health_layout.addWidget(QLabel("Target Weight (kg):"))
        target_weight_layout = QHBoxLayout()
        self.spin_target_weight = QDoubleSpinBox()
        self.spin_target_weight.setRange(20, 200)
        self.spin_target_weight.setValue(65)
        self.spin_target_weight.setSingleStep(0.1)
        target_weight_layout.addWidget(self.spin_target_weight)
        target_weight_layout.addStretch()
        health_layout.addLayout(target_weight_layout)
        
        health_group.setLayout(health_layout)
        layout.addWidget(health_group)
        
        # ====== ปุ่ม Submit ======
        self.btn_submit = QPushButton("Save Profile")
        self.btn_submit.setMinimumHeight(40)
        self.btn_submit.clicked.connect(self.save_profile)
        layout.addWidget(self.btn_submit)
        
        layout.addStretch()
        self.setLayout(layout)
        
        # โหลดข้อมูล profile ถ้ามี
        self.load_existing_profile()

    def load_existing_profile(self):
        # ====== โหลดข้อมูล profile ที่มีอยู่ (ถ้ามี) ======
        profile = self.user_manager.get_user_profile(self.username)
        if profile:
            self.input_name.setText(profile.get("name", ""))
            self.input_email.setText(profile.get("email", ""))
            self.spin_age.setValue(profile.get("age", 25))
            self.spin_height.setValue(profile.get("height", 170))
            self.spin_weight.setValue(profile.get("weight", 70))
            self.combo_gender.setCurrentText(profile.get("gender", "Male"))
            self.combo_blood.setCurrentText(profile.get("blood_type", "O+"))
            self.spin_target_weight.setValue(profile.get("target_weight", 65))

    def save_profile(self):
        # ====== ตรวจสอบว่ากรอกชื่อหรือไม่ ======
        if not self.input_name.text().strip():
            QMessageBox.warning(self, "Error", "Please enter your full name!")
            return
        
        # ====== ตรวจสอบว่ากรอกอีเมลหรือไม่ ======
        if not self.input_email.text().strip():
            QMessageBox.warning(self, "Error", "Please enter your email!")
            return
        
        # ====== ตรวจสอบรูปแบบอีเมล ======
        if "@" not in self.input_email.text():
            QMessageBox.warning(self, "Error", "Please enter a valid email!")
            return
        
        # ====== สร้าง Dictionary เก็บข้อมูล Profile ======
        profile_data = {
            "name": self.input_name.text(),
            "email": self.input_email.text(),
            "age": self.spin_age.value(),
            "height": self.spin_height.value(),
            "weight": self.spin_weight.value(),
            "gender": self.combo_gender.currentText(),
            "blood_type": self.combo_blood.currentText(),
            "target_weight": self.spin_target_weight.value()
        }
        
        # ====== บันทึก Profile ลงไฟล์ ======
        self.user_manager.save_user_profile(self.username, profile_data)
        self.profile_data = profile_data
        
        QMessageBox.information(self, "Success", "Profile saved successfully!")
        self.accept()

class FoodItem:
    """
    คลาสสำหรับเก็บข้อมูลอาหารแต่ละรายการ
    - date: วันที่รับประทาน
    - name: ชื่ออาหาร
    - calories_per_100g: แคลอรี่ต่อ 100 กรัม
    - amount: ปริมาณที่รับประทาน (กรัม)
    - total_calories: แคลอรี่รวม = (amount / 100) * calories_per_100g
    """
    def __init__(self, date, name, calories_per_100g, amount):
        self.date = date
        self.name = name
        self.calories_per_100g = float(calories_per_100g)
        self.amount = float(amount)  # กรัม
        self.total_calories = (self.amount / 100) * self.calories_per_100g

class CalorieCalculator(QMainWindow):
    """
    แอปพลิเคชันหลักสำหรับติดตามแคลอรี่
    มีฟีเจอร์:
    - เพิ่มและบันทึกข้อมูลอาหาร
    - แสดงสรุปแคลอรี่ของวันและรวมทั้งหมด
    - ลบข้อมูลอาหารที่ไม่ต้องการ
    - Logout
    """
    def __init__(self, username, user_manager):
        super().__init__()
        # ====== บันทึกชื่อผู้ใช้ ======
        self.username = username
        # ====== เก็บ user manager เพื่อใช้จัดการข้อมูล ======
        self.user_manager = user_manager
        # ====== โหลด profile data ของผู้ใช้ ======
        self.user_profile = user_manager.get_user_profile(username)
        # ====== list สำหรับเก็บข้อมูลอาหาร ======
        self.food_items = []
        self.setWindowTitle(f"Calorie Calculator - {username}")
        self.setGeometry(100, 100, 600, 600)

        # Style
        self.setStyleSheet("""
            QMainWindow { background-color: #f0f8ff; color: #000000; }
            QLabel { font-size: 14px; color: #2f3640; }
            QLineEdit, QComboBox, QDateEdit { padding: 8px; border: 1px solid #dcdde1; border-radius: 5px; background-color: white; color: black; }
            QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; font-weight: bold; }
            QPushButton:hover { background-color: #45a049; }
            QPushButton#deleteBtn { background-color: #f44336; }
            QPushButton#deleteBtn:hover { background-color: #da190b; }
            QTableWidget { border: 1px solid #dcdde1; gridline-color: #ecf0f1; background-color: white; color: black; }
            QHeaderView::section { background-color: #2196F3; color: white; padding: 5px; }
            QGroupBox { font-weight: bold; border: 1px solid #dcdde1; border-radius: 5px; margin-top: 10px; color: black; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px; color: black; }
        """)

        # Main Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Total Calories Display
        self.create_total_display()

        # Input Form
        self.create_input_form()

        # Food List Table
        self.create_food_table()

        # Load initial data (empty)
        self.update_display()

    def create_total_display(self):
        # ====== Group น้ำหนัก/แคลอรี่ ======
        group = QGroupBox("Calories Summary")
        layout = QVBoxLayout()

        # ====== แถวแสดงข้อมูลผู้ใช้ และปุ่ม Edit Profile, Logout ======
        user_layout = QHBoxLayout()
        self.lbl_user = QLabel(f"User: {self.username}")
        self.lbl_user.setStyleSheet("font-size: 12px; color: #555;")
        self.btn_edit_profile = QPushButton("Edit Profile")
        self.btn_edit_profile.setMaximumWidth(120)
        self.btn_edit_profile.clicked.connect(self.edit_profile)
        self.btn_logout = QPushButton("Logout")
        self.btn_logout.setMaximumWidth(100)
        self.btn_logout.clicked.connect(self.logout)
        user_layout.addWidget(self.lbl_user)
        user_layout.addStretch()
        user_layout.addWidget(self.btn_edit_profile)
        user_layout.addWidget(self.btn_logout)
        layout.addLayout(user_layout)

        # ====== แสดงแคลอรี่วันนี้ ======
        self.lbl_today = QLabel("Today: 0 kcal")
        self.lbl_today.setStyleSheet("font-size: 16px; font-weight: bold; color: #FF9800;")
        
        # ====== แสดงแคลอรี่รวมทั้งหมด ======
        self.lbl_total = QLabel("Total All: 0 kcal")
        self.lbl_total.setStyleSheet("font-size: 18px; font-weight: bold; color: #2196F3;")
        
        # ====== แสดงแคลอรี่เป้าหมายต่อวันเพื่อบรรลุน้ำหนักเป้าหมาย ======
        self.lbl_daily_target = QLabel("Daily Target: 0 kcal")
        self.lbl_daily_target.setStyleSheet("font-size: 14px; font-weight: bold; color: #4CAF50;")
        
        # ====== แสดงแคลอรี่ที่เหลือสำหรับวันนี้ ======
        self.lbl_remaining = QLabel("Remaining: 0 kcal")
        self.lbl_remaining.setStyleSheet("font-size: 14px; font-weight: bold; color: #9C27B0;")
        
        layout.addWidget(self.lbl_today)
        layout.addWidget(self.lbl_total)
        layout.addWidget(self.lbl_daily_target)
        layout.addWidget(self.lbl_remaining)

        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def create_input_form(self):
        # ====== Group สำหรับเพิ่มอาหาร ======
        group = QGroupBox("Add Food")
        layout = QVBoxLayout()

        # ====== วันที่ - ใช้ QDateEdit สำหรับเลือกวันที่ ======
        layout.addWidget(QLabel("Date:"))
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        layout.addWidget(self.date_edit)

        # ====== ชื่ออาหาร - กรอกชื่อของอาหารที่ต้องการเพิ่ม ======
        layout.addWidget(QLabel("Food Name:"))
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("e.g. Apple")
        layout.addWidget(self.input_name)

        # ====== แคลอรี่ต่อ 100g - gกรอกค่าแคลอรี่ของอาหารต่อ 100 กรัม ======
        layout.addWidget(QLabel("Calories per 100g:"))
        self.input_calories = QLineEdit()
        self.input_calories.setPlaceholderText("e.g. 52")
        layout.addWidget(self.input_calories)

        # ====== ปริมาณ (กรัม) - จำนวนกรัมของอาหารที่รับประทาน ======
        layout.addWidget(QLabel("Amount (grams):"))
        self.input_amount = QLineEdit()
        self.input_amount.setPlaceholderText("e.g. 100")
        layout.addWidget(self.input_amount)

        # ====== ปุ่มเพิ่มอาหาร ======
        self.btn_add = QPushButton("Add Food")
        self.btn_add.clicked.connect(self.add_food)
        layout.addWidget(self.btn_add)

        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def create_food_table(self):
        # ====== Group ตาราแสดงรายการอาหาร ======
        group = QGroupBox("Food List")
        layout = QVBoxLayout()

        # ====== สร้าง Table Widget ======
        self.table = QTableWidget()
        # ====== จำนวนคอลัมน์: วันที่, ชื่ออาหาร, แคลอรี่/100g, ปริมาณ(g), รวมแคลอรี่ ======
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Date", "Food", "Cal/100g", "Amount (g)", "Total Cal"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # ====== ปุ่มลบแถวที่เลือก ======
        self.btn_delete = QPushButton("Delete Selected")
        self.btn_delete.setObjectName("deleteBtn")
        self.btn_delete.clicked.connect(self.delete_food)

        layout.addWidget(self.table)
        layout.addWidget(self.btn_delete)
        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def add_food(self):
        try:
            # ====== ดึงข้อมูลจาก input fields ======
            date = self.date_edit.date().toString("yyyy-MM-dd")
            name = self.input_name.text()
            calories_text = self.input_calories.text()
            amount_text = self.input_amount.text()

            # ====== ตรวจสอบข้อมูลไม่ว่าง ======
            if not name or not calories_text or not amount_text:
                QMessageBox.warning(self, "Error", "Please fill in all fields!")
                return

            try:
                # ====== แปลงค่าเป็นตัวเลข ======
                calories_per_100g = float(calories_text)
                amount = float(amount_text)
            except ValueError:
                QMessageBox.warning(self, "Error", "Calories and Amount must be numbers!")
                return

            # ====== ตรวจสอบค่าที่ป้อนเข้า ======
            if calories_per_100g < 0 or amount <= 0:
                QMessageBox.warning(self, "Error", "Calories must be non-negative and Amount must be positive!")
                return

            # ====== สร้าง FoodItem object และเพิ่มลงใน list ======
            food_item = FoodItem(date, name, calories_per_100g, amount)
            self.food_items.append(food_item)

            # ====== ล้าง input fields ======
            self.input_name.clear()
            self.input_calories.clear()
            self.input_amount.clear()

            # ====== อัปเดตการแสดงผลตาราและสรุปแคลอรี่ ======
            self.update_display()

            QMessageBox.information(self, "Success", "Food added successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_food(self):
        # ====== ดึงแถวที่เลือก ======
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a row to delete.")
            return

        # ====== ยืนยันการลบ ======
        confirm = QMessageBox.question(self, "Confirm", "Are you sure you want to delete this food?",
                                       QMessageBox.Yes | QMessageBox.No)

        # ====== ลบข้อมูลจาก list และอัปเดตตารา ======
        if confirm == QMessageBox.Yes:
            del self.food_items[selected_row]
            self.update_display()

    def update_display(self):
        # ====== เรียงลำดับข้อมูลตามวันที่ (ล่าสุดมาก่อน) ======
        self.food_items.sort(key=lambda x: x.date, reverse=True)

        # ====== ล้างตารา ======
        self.table.setRowCount(0)
        today = QDate.currentDate().toString("yyyy-MM-dd")
        today_calories = 0
        total_calories = 0

        # ====== วนลูปเพิ่มข้อมูลลงตารา ======
        for item in self.food_items:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            # ====== เพิ่มข้อมูลแต่ละคอลัมน์ ======
            self.table.setItem(row_position, 0, QTableWidgetItem(item.date))
            self.table.setItem(row_position, 1, QTableWidgetItem(item.name))
            self.table.setItem(row_position, 2, QTableWidgetItem(f"{item.calories_per_100g:.1f}"))
            self.table.setItem(row_position, 3, QTableWidgetItem(f"{item.amount:.1f}"))
            self.table.setItem(row_position, 4, QTableWidgetItem(f"{item.total_calories:.1f}"))

            # ====== คำนวณแคลอรี่รวม ======
            total_calories += item.total_calories
            # ====== คำนวณแคลอรี่วันนี้ ======
            if item.date == today:
                today_calories += item.total_calories

        # ====== คำนวณแคลอรี่เป้าหมายต่อวัน ======
        daily_target = self.calculate_daily_target()
        remaining_calories = daily_target - today_calories
        
        # ====== อัปเดตป้ายแสดงแคลอรี่ ======
        self.lbl_today.setText(f"Today: {today_calories:.1f} kcal")
        self.lbl_total.setText(f"Total All: {total_calories:.1f} kcal")
        self.lbl_daily_target.setText(f"Daily Target: {daily_target:.1f} kcal")
        
        # ====== แสดงแคลอรี่ที่เหลือพร้อมสี ======
        if remaining_calories >= 0:
            self.lbl_remaining.setText(f"Remaining: {remaining_calories:.1f} kcal")
            self.lbl_remaining.setStyleSheet("font-size: 14px; font-weight: bold; color: #4CAF50;")
        else:
            self.lbl_remaining.setText(f"Over: {abs(remaining_calories):.1f} kcal")
            self.lbl_remaining.setStyleSheet("font-size: 14px; font-weight: bold; color: #FF5252;")

        # ====== ยืนยันการออกจากระบบข ======
        reply = QMessageBox.question(self, "Logout", "Are you sure you want to logout?",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

    def calculate_daily_target(self):
        """
        ====== คำนวณแคลอรี่เป้าหมายต่อวันเพื่อบรรลุน้ำหนักเป้าหมาย ======
        ใช้สูตร Harris-Benedict เพื่อคำนวณ Basal Metabolic Rate (BMR)
        จากนั้นคูณด้วย activity level (1.2) เพื่อได้ TDEE
        สำหรับการลดน้ำหนัก ลด 500 kcal/วัน = 0.5 kg/สัปดาห์
        """
        if not self.user_profile:
            return 2000  # ค่าเริ่มต้น
        
        weight = self.user_profile.get("weight", 70)
        height = self.user_profile.get("height", 170)
        age = self.user_profile.get("age", 25)
        gender = self.user_profile.get("gender", "Male")
        target_weight = self.user_profile.get("target_weight", 65)
        
        # ====== คำนวณ BMR ด้วย Harris-Benedict ======
        if gender == "Male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        
        # ====== TDEE = BMR * Activity Level (1.2 = sedentary) ======
        tdee = bmr * 1.2
        
        # ====== สำหรับลดน้ำหนัก: ลด 500 kcal/วัน ======
        if weight > target_weight:
            daily_target = tdee - 500
        else:
            daily_target = tdee
        
        return max(daily_target, 1200)  # ต่ำสุด 1200 kcal/วัน

    def edit_profile(self):
        """
        ====== เปิดหน้า Profile เพื่อแก้ไขข้อมูล ======
        """
        profile_window = ProfileWindow(self.user_manager, self.username)
        if profile_window.exec() == QDialog.Accepted:
            # ====== โหลด profile ที่อัปเดตใหม่ ======
            self.user_profile = self.user_manager.get_user_profile(self.username)
            # ====== อัปเดตการแสดงผลเพื่อให้เห็นแคลอรี่เป้าหมายใหม่ ======
            self.update_display()
            QMessageBox.information(self, "Success", "Profile updated!")

    def logout(self):
        # ====== ยืนยันการออกจากระบบข ======
        reply = QMessageBox.question(self, "Logout", "Are you sure you want to logout?",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    # ====== สร้าง QApplication (แอปพลิเคชัน Qt) ======
    app = QApplication(sys.argv)
    # ====== ตั้งค่าฟอนต์เริ่มต้นของแอปพลิเคชัน ======
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # ====== โหลด User Manager เพื่อจัดการข้อมูลผู้ใช้ ======
    user_manager = UserManager()
    # ====== แสดงหน้า Login ======
    login_window = LoginWindow(user_manager)
    
    # ====== ตรวจสอบว่า User กด OK ในหน้า Login หรือไม่ ======
    if login_window.exec() == QDialog.Accepted:
        username = login_window.current_user
        
        # ====== ตรวจสอบว่า User มี Profile แล้วหรือไม่ ======
        # ====== ถ้ายังไม่มี ให้แสดงหน้า Profile เพื่อให้กรอกข้อมูล ======
        if not user_manager.has_profile(username):
            profile_window = ProfileWindow(user_manager, username)
            if profile_window.exec() != QDialog.Accepted:
                sys.exit()
        
        # ====== หลังจาก Login และ Profile สำเร็จ แสดงแอปพลิเคชันหลัก ======
        window = CalorieCalculator(username, user_manager)
        window.show()
        # ====== รัน event loop ======
        sys.exit(app.exec())
    else:
        # ====== ถ้า User ปิดหน้า Login ให้ปิดแอปพลิเคชัน ======
        sys.exit()