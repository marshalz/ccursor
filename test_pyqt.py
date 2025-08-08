#!/usr/bin/env python3
"""
Simple PyQt6 test to verify the installation works
"""

import sys
import os

# Set environment variables for Qt
if sys.platform == "darwin":
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ''

try:
    from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
    from PyQt6.QtCore import Qt
    
    app = QApplication(sys.argv)
    
    # Create a simple window
    window = QWidget()
    window.setWindowTitle("PyQt6 Test")
    window.setGeometry(100, 100, 300, 200)
    
    layout = QVBoxLayout()
    label = QLabel("PyQt6 is working!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label)
    
    window.setLayout(layout)
    window.show()
    
    print("PyQt6 test window should appear. Close it to continue.")
    sys.exit(app.exec())
    
except Exception as e:
    print(f"Error: {e}")
    print("PyQt6 is not working properly on this system.") 