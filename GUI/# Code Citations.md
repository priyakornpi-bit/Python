# Code Citations

## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```


## License: unknown
https://github.com/LarryCCLai/TankWar/blob/bc25d7a1972948c3d0c890a291b31741cf9020c8/WorkWidgets/PlayerWidget.py

```
# ทำให้เครื่องคิดเลขทำงานได้

ฉันจะอธิบายวิธีการเชื่อมต่อปุ่มกับการทำงานจริง:

````python
# filepath: /Users/tonton210/Python/GUI/Grid.py
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        # ===== Display =====
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(80)
        self.display.setStyleSheet("font-size: 36px;")

        layout.addWidget(self.display, 0, 0, 2, 4)

        # ===== Row 2 =====
        self.create_button("⌫", 2, 0, layout, self.on_backspace)
        self.create_button("AC", 2, 1, layout, self.on_clear)
        self.create_button("%", 2, 2, layout, lambda: self.on_operator("%"))
        self.create_button("÷", 2, 3, layout, lambda: self.on_operator("÷"))

        # ===== Row 3 =====
        self.create_button("7", 3, 0, layout, lambda: self.on_number("7"))
        self.create_button("8", 3, 1, layout, lambda: self.on_number("8"))
        self.create_button("9", 3, 2, layout, lambda: self.on_number("9"))
        self.create_button("×", 3, 3, layout, lambda: self.on_operator("×"))

        # ===== Row 4 =====
        self.create_button("4", 4, 0, layout, lambda: self.on_number("4"))
        self.create_button("5", 4, 1, layout, lambda: self.on_number("5"))
        self.create_button("6", 4, 2, layout, lambda: self.on_number("6"))
        self.create_button("−", 4, 3, layout, lambda: self.on_operator("−"))

        # ===== Row 5 =====
        self.create_button("1", 5, 0, layout, lambda: self.on_number("1"))
        self.create_button("2", 5, 1, layout, lambda: self.on_number("2"))
        self.create_button("3", 5, 2, layout, lambda: self.on_number("3"))
        self.create_button("+", 5, 3, layout, lambda: self.on_operator("+"))

        # ===== Row 6 =====
        zero_btn = QPushButton("0")
        layout.addWidget(zero_btn, 6, 0, 1, 2)
        zero_btn.clicked.connect(lambda: self.on_number("0"))
        
        self.create_button(".", 6, 2, layout, self.on_decimal)
        self.create_button("=", 6, 3, layout, self.on_equals)

        # ===== Stretch =====
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)

        
```

