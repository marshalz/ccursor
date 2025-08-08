#!/usr/bin/env python3
"""
Launcher script for GinRummy Score Tracker
Automatically tries PyQt5 first, then PyQt6 if needed
"""

import sys
import subprocess
import os

def try_pyqt5():
    """Try to run the PyQt5 version"""
    try:
        print("Attempting to run PyQt5 version...")
        result = subprocess.run([sys.executable, "gin_rummy_tracker_pyqt5.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("PyQt5 version ran successfully!")
            return True
        else:
            print(f"PyQt5 version failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error running PyQt5 version: {e}")
        return False

def try_pyqt6():
    """Try to run the PyQt6 version"""
    try:
        print("Attempting to run PyQt6 version...")
        result = subprocess.run([sys.executable, "gin_rummy_tracker.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("PyQt6 version ran successfully!")
            return True
        else:
            print(f"PyQt6 version failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error running PyQt6 version: {e}")
        return False

def main():
    print("=" * 50)
    print("GinRummy Score Tracker Launcher")
    print("=" * 50)
    
    # Check if files exist
    pyqt5_exists = os.path.exists("gin_rummy_tracker_pyqt5.py")
    pyqt6_exists = os.path.exists("gin_rummy_tracker.py")
    
    if not pyqt5_exists and not pyqt6_exists:
        print("Error: No application files found!")
        print("Please make sure gin_rummy_tracker_pyqt5.py or gin_rummy_tracker.py exists.")
        return
    
    # Try PyQt5 first (better macOS compatibility)
    if pyqt5_exists:
        if try_pyqt5():
            return
    
    # Try PyQt6 as fallback
    if pyqt6_exists:
        if try_pyqt6():
            return
    
    print("\nBoth versions failed to run.")
    print("Please check your PyQt installation:")
    print("  pip install PyQt5")
    print("  pip install PyQt6")

if __name__ == "__main__":
    main() 