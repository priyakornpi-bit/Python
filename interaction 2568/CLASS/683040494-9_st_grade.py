"""
Priyakorn Pichitmarn
683040494-9
"""
import sys
import csv
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QFileDialog, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt


class StudentManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Score Manager")
        self.resize(700, 500)
        self.current_path = None

        # ── Central widget & layout ──────────────────
        widget = QWidget()
        main_layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

        # ── Toolbar: Load / Save buttons ─────────────
        toolbar = QHBoxLayout()
        self.btn_load = QPushButton("Load CSV")
        self.btn_save = QPushButton("Save CSV")
        self.lbl_file = QLabel("No file loaded")
        self.btn_save.setEnabled(False)

        toolbar.addWidget(self.btn_load)
        toolbar.addWidget(self.btn_save)
        toolbar.addWidget(self.lbl_file)
        toolbar.addStretch()

        # ── Table ─────────────────────────────────────
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Score", "Grade"])
        self.table.horizontalHeader().setStretchLastSection(True)

        # ── Add new student row ───────────────────────
        add_layout = QHBoxLayout()
        self.input_name  = QLineEdit()
        self.input_score = QLineEdit()
        self.input_grade = QLineEdit()
        self.input_name.setPlaceholderText("Name")
        self.input_score.setPlaceholderText("Score")
        self.input_grade.setPlaceholderText("Grade")
        self.btn_add = QPushButton("Add Row")

        add_layout.addWidget(self.input_name)
        add_layout.addWidget(self.input_score)
        add_layout.addWidget(self.input_grade)
        add_layout.addWidget(self.btn_add)

        # ── Status bar ────────────────────────────────
        self.statusBar().showMessage("Ready")

        # ── Assemble layout ───────────────────────────
        main_layout.addLayout(toolbar)
        main_layout.addWidget(self.table)
        main_layout.addLayout(add_layout)

        # ── Connect signals ───────────────────────────
        self.btn_load.clicked.connect(self.load_file)
        self.btn_save.clicked.connect(self.save_file)
        self.btn_add.clicked.connect(self.add_row)

    # Load data from CSV and populate the table.
    def load_file(self):
        # Ask user to choose the CSV file to load.
        dbfilename, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*)"
        )
        if not dbfilename:
            return

        # Read each row from CSV and append it into the table widget.
        with open(dbfilename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for k in row:  # for each key in dict
                    print(f"  {k}: {row[k]}")
                name = row['name']
                score = row['score']
                grade = row['grade']
                r = self.table.rowCount()
                self.table.insertRow(r)
                self.table.setItem(r, 0, QTableWidgetItem(name))
                self.table.setItem(r, 1, QTableWidgetItem(score))
                self.table.setItem(r, 2, QTableWidgetItem(grade))

    # Save all table rows to a CSV file.
    def save_file(self):
        pass

    # ──────────────────────────────────────────────────
    # Read the three input fields,
    #      and add a new row to self.table
    # ──────────────────────────────────────────────────
    def add_row(self):
        # Get user input and trim spaces to avoid accidental empty values.
        name  = self.input_name.text().strip()
        score = self.input_score.text().strip()
        grade = self.input_grade.text().strip()

        if not name or not score or not grade:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields")
            return

        # Insert a new table row with the entered student data.
        r = self.table.rowCount()
        self.table.insertRow(r)
        self.table.setItem(r, 0, QTableWidgetItem(name))
        self.table.setItem(r, 1, QTableWidgetItem(score))
        self.table.setItem(r, 2, QTableWidgetItem(grade))

        self.input_name.clear()
        self.input_score.clear()
        self.input_grade.clear()

        self.statusBar().showMessage(f"Added {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StudentManager()
    win.show()
    sys.exit(app.exec())