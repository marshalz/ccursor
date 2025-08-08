#!/usr/bin/env python3
"""
Test script to verify integer-only validation and empty field reset
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

class TestInputValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Input Validation Test")
        self.setGeometry(100, 100, 500, 300)
        
        layout = QVBoxLayout()
        
        # Instructions
        instructions = QLabel("Test integer-only validation and empty field reset:")
        instructions.setStyleSheet("font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(instructions)
        
        # Input fields
        input_layout = QHBoxLayout()
        
        self.zayaka_entry = QLineEdit()
        self.zayaka_entry.setPlaceholderText("Enter Zayaka's score (integers only)")
        self.zayaka_entry.setValidator(QIntValidator(0, 999))  # Only allow integers 0-999
        input_layout.addWidget(self.zayaka_entry)
        
        self.brian_entry = QLineEdit()
        self.brian_entry.setPlaceholderText("Enter Brian's score (integers only)")
        self.brian_entry.setValidator(QIntValidator(0, 999))  # Only allow integers 0-999
        input_layout.addWidget(self.brian_entry)
        
        add_button = QPushButton("Add Scores")
        add_button.clicked.connect(self.add_scores)
        input_layout.addWidget(add_button)
        
        layout.addLayout(input_layout)
        
        # Status label
        self.status_label = QLabel("Try entering non-integers (letters, symbols) - they should be blocked")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("color: #666; margin: 10px 0;")
        layout.addWidget(self.status_label)
        
        # Test results
        self.results_label = QLabel("Results will appear here")
        self.results_label.setWordWrap(True)
        self.results_label.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.results_label)
        
        self.setLayout(layout)
        
    def add_scores(self):
        """Add scores and clear input fields completely"""
        try:
            zayaka_text = self.zayaka_entry.text()
            brian_text = self.brian_entry.text()
            
            zayaka_score = int(zayaka_text) if zayaka_text else 0
            brian_score = int(brian_text) if brian_text else 0
            
            result_text = f"Added scores: Zayaka={zayaka_score}, Brian={brian_score}\n"
            result_text += f"Input field contents before clear: Zayaka='{zayaka_text}', Brian='{brian_text}'\n"
            
            # Clear entry fields completely
            self.zayaka_entry.clear()
            self.brian_entry.clear()
            self.zayaka_entry.setFocus()
            
            result_text += f"Input field contents after clear: Zayaka='{self.zayaka_entry.text()}', Brian='{self.brian_entry.text()}'"
            
            self.results_label.setText(result_text)
            
        except ValueError:
            self.results_label.setText("Error: Please enter valid numbers")

def main():
    app = QApplication(sys.argv)
    window = TestInputValidation()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 