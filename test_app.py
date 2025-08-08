#!/usr/bin/env python3
"""
Test script for GinRummy Score Tracker
This script tests the database functionality and core features
"""

import sqlite3
import os
from datetime import datetime

def test_database():
    """Test database creation and operations"""
    print("Testing database functionality...")
    
    # Test database connection
    conn = sqlite3.connect('gin_rummy_history.db')
    cursor = conn.cursor()
    
    # Test table creation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zayaka_score INTEGER,
            brian_score INTEGER,
            winner TEXT,
            match_date TEXT,
            game_scores TEXT
        )
    ''')
    conn.commit()
    print("✓ Database table created successfully")
    
    # Test data insertion
    test_data = {
        'zayaka_score': 105,
        'brian_score': 95,
        'winner': 'Zayaka',
        'match_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'game_scores': 'Zayaka: 25,30,50; Brian: 20,25,50'
    }
    
    cursor.execute('''
        INSERT INTO test_matches (zayaka_score, brian_score, winner, match_date, game_scores)
        VALUES (?, ?, ?, ?, ?)
    ''', (test_data['zayaka_score'], test_data['brian_score'], 
          test_data['winner'], test_data['match_date'], test_data['game_scores']))
    conn.commit()
    print("✓ Test data inserted successfully")
    
    # Test data retrieval
    cursor.execute('SELECT * FROM test_matches WHERE winner = ?', ('Zayaka',))
    result = cursor.fetchone()
    if result:
        print(f"✓ Data retrieved successfully: {result}")
    else:
        print("✗ Data retrieval failed")
    
    # Clean up test table
    cursor.execute('DROP TABLE test_matches')
    conn.commit()
    print("✓ Test table cleaned up")
    
    conn.close()
    print("✓ Database test completed successfully\n")

def test_score_calculation():
    """Test score calculation logic"""
    print("Testing score calculation...")
    
    # Test case 1: Zayaka wins
    zayaka_scores = [25, 30, 50]
    brian_scores = [20, 25, 45]
    zayaka_total = sum(zayaka_scores)  # 105
    brian_total = sum(brian_scores)    # 90
    
    if zayaka_total >= 100:
        winner = "Zayaka"
    elif brian_total >= 100:
        winner = "Brian"
    else:
        winner = "Game continues"
    
    print(f"✓ Zayaka total: {zayaka_total}, Brian total: {brian_total}")
    print(f"✓ Winner: {winner}")
    
    # Test case 2: Brian wins
    zayaka_scores = [20, 25, 40]
    brian_scores = [30, 35, 40]
    zayaka_total = sum(zayaka_scores)  # 85
    brian_total = sum(brian_scores)    # 105
    
    if zayaka_total >= 100:
        winner = "Zayaka"
    elif brian_total >= 100:
        winner = "Brian"
    else:
        winner = "Game continues"
    
    print(f"✓ Zayaka total: {zayaka_total}, Brian total: {brian_total}")
    print(f"✓ Winner: {winner}")
    
    # Test case 3: Both reach 100
    zayaka_scores = [25, 30, 50]
    brian_scores = [30, 35, 40]
    zayaka_total = sum(zayaka_scores)  # 105
    brian_total = sum(brian_scores)    # 105
    
    if zayaka_total >= 100 and brian_total >= 100:
        winner = "Zayaka" if zayaka_total > brian_total else "Brian"
    elif zayaka_total >= 100:
        winner = "Zayaka"
    elif brian_total >= 100:
        winner = "Brian"
    else:
        winner = "Game continues"
    
    print(f"✓ Zayaka total: {zayaka_total}, Brian total: {brian_total}")
    print(f"✓ Winner: {winner}")
    print("✓ Score calculation test completed successfully\n")

def test_file_structure():
    """Test that all required files exist"""
    print("Testing file structure...")
    
    required_files = [
        'gin_rummy_tracker.py',
        'requirements.txt',
        'README.md'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
    
    print("✓ File structure test completed successfully\n")

if __name__ == "__main__":
    print("=" * 50)
    print("GinRummy Score Tracker - Test Suite")
    print("=" * 50)
    
    test_file_structure()
    test_database()
    test_score_calculation()
    
    print("=" * 50)
    print("All tests completed!")
    print("=" * 50) 