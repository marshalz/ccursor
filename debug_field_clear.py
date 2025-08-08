#!/usr/bin/env python3
"""
Debug script to test field clearing behavior
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

class DebugFieldClear(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Debug Field Clearing")
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        
        # Input fields
        input_layout = QHBoxLayout()
        
        self.zayaka_entry = QLineEdit()
        self.zayaka_entry.setPlaceholderText("Enter Zayaka's score")
        self.zayaka_entry.setValidator(QIntValidator(0, 999))
        input_layout.addWidget(self.zayaka_entry)
        
        self.brian_entry = QLineEdit()
        self.brian_entry.setPlaceholderText("Enter Brian's score")
        self.brian_entry.setValidator(QIntValidator(0, 999))
        input_layout.addWidget(self.brian_entry)
        
        add_button = QPushButton("Add Scores")
        add_button.clicked.connect(self.add_scores)
        input_layout.addWidget(add_button)
        
        layout.addLayout(input_layout)
        
        # Debug output
        self.debug_output = QTextEdit()
        self.debug_output.setMaximumHeight(200)
        self.debug_output.setPlaceholderText("Debug output will appear here...")
        layout.addWidget(self.debug_output)
        
        # Status
        self.status_label = QLabel("Enter scores and click 'Add Scores' to test clearing")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
        # Log initial state
        self.log_debug("Initial state:")
        self.log_field_states()
        
    def log_debug(self, message):
        """Add message to debug output"""
        self.debug_output.append(message)
        
    def log_field_states(self):
        """Log the current state of input fields"""
        zayaka_text = self.zayaka_entry.text()
        brian_text = self.brian_entry.text()
        zayaka_len = len(zayaka_text)
        brian_len = len(brian_text)
        
        self.log_debug(f"  Zayaka field: text='{zayaka_text}' (length={zayaka_len})")
        self.log_debug(f"  Brian field: text='{brian_text}' (length={brian_len})")
        self.log_debug("")
        
    def add_scores(self):
        """Add scores and clear fields"""
        self.log_debug("=== ADDING SCORES ===")
        self.log_debug("Before processing:")
        self.log_field_states()
        
        try:
            zayaka_text = self.zayaka_entry.text()
            brian_text = self.brian_entry.text()
            
            zayaka_score = int(zayaka_text) if zayaka_text else 0
            brian_score = int(brian_text) if brian_text else 0
            
            self.log_debug(f"Processing scores: Zayaka={zayaka_score}, Brian={brian_score}")
            
            # Clear entry fields completely
            self.log_debug("Clearing fields...")
            self.zayaka_entry.clear()
            self.brian_entry.clear()
            self.zayaka_entry.setFocus()
            
            self.log_debug("After clearing:")
            self.log_field_states()
            
            self.status_label.setText(f"Added scores: Zayaka={zayaka_score}, Brian={brian_score}")
            
        except ValueError as e:
            self.log_debug(f"Error: {e}")
            self.status_label.setText("Error: Please enter valid numbers")

def main():
    app = QApplication(sys.argv)
    window = DebugFieldClear()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 