#!/usr/bin/env python3
"""
Test script to verify input field reset behavior
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class TestInputReset(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Input Reset Test")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        
        # Input fields
        input_layout = QHBoxLayout()
        
        self.zayaka_entry = QLineEdit("0")
        self.zayaka_entry.setPlaceholderText("Enter Zayaka's score")
        input_layout.addWidget(self.zayaka_entry)
        
        self.brian_entry = QLineEdit("0")
        self.brian_entry.setPlaceholderText("Enter Brian's score")
        input_layout.addWidget(self.brian_entry)
        
        add_button = QPushButton("Add Scores")
        add_button.clicked.connect(self.add_scores)
        input_layout.addWidget(add_button)
        
        layout.addLayout(input_layout)
        
        # Status label
        self.status_label = QLabel("Enter scores and click 'Add Scores' to test reset behavior")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
    def add_scores(self):
        """Add scores and reset input fields to 0"""
        try:
            zayaka_score = int(self.zayaka_entry.text()) if self.zayaka_entry.text() else 0
            brian_score = int(self.brian_entry.text()) if self.brian_entry.text() else 0
            
            self.status_label.setText(f"Added scores: Zayaka={zayaka_score}, Brian={brian_score}")
            
            # Reset entry fields to 0
            self.zayaka_entry.setText("0")
            self.brian_entry.setText("0")
            self.zayaka_entry.setFocus()
            
        except ValueError:
            self.status_label.setText("Error: Please enter valid numbers")

def main():
    app = QApplication(sys.argv)
    window = TestInputReset()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 