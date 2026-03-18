import sys 
from PySide6.QtWidgets import (QApplication,
QMainWindow,
QWidget,
QVBoxLayout,
QHBoxLayout,
QLabel,
QLineEdit,
QPushButton,
QRadioButton,
QComboBox,
QDateEdit,
QTextEdit,
QCheckBox,
QButtonGroup
)
from PySide6.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.resize(420,260)
        self.setWindowTitle("Login - Pyside6")

         # กล่องหลัก
        central = QWidget()
        self.setCentralWidget(central)

        #layou แนวตั้ง 
        layout = QVBoxLayout()
        central.setLayout(layout)

        #widgets
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        Login = QLabel("login ")
        Login.setAlignment(Qt.AlignLeft)


        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        #ใส่ลง layout
        
        layout.addWidget(Login)
        layout.addWidget(self.email_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        


        











if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


