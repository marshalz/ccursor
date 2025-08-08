#!/usr/bin/env python3
"""
GinRummy Score Tracker - Complete Application
PyQt5 version with database integration
"""

import sys
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QMessageBox, QTabWidget, QFrame)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIntValidator, QFont

class GinRummyTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_database()
        self.init_ui()
        self.load_match_history()
        
    def init_database(self):
        """Initialize database and create tables if needed"""
        self.conn = sqlite3.connect('gin_rummy_history.db')
        self.cursor = self.conn.cursor()
        
        # Create matches table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                zayaka_score INTEGER,
                brian_score INTEGER,
                winner TEXT,
                match_date TEXT,
                game_scores TEXT
            )
        ''')
        self.conn.commit()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("GinRummy Score Tracker")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # Create tabs
        self.create_score_tab()
        self.create_history_tab()
        self.create_stats_tab()
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
    def create_score_tab(self):
        """Create the score entry tab"""
        score_widget = QWidget()
        layout = QVBoxLayout(score_widget)
        
        # Title
        title = QLabel("GinRummy Score Tracker")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Score entry section
        entry_frame = QFrame()
        entry_frame.setFrameStyle(QFrame.Box)
        entry_layout = QVBoxLayout(entry_frame)
        
        entry_title = QLabel("Enter Game Scores")
        entry_title.setFont(QFont("Arial", 12, QFont.Bold))
        entry_layout.addWidget(entry_title)
        
        # Input fields
        input_layout = QHBoxLayout()
        
        # Zayaka's score
        zayaka_layout = QVBoxLayout()
        zayaka_label = QLabel("Zayaka's Score:")
        zayaka_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.zayaka_entry = QLineEdit()
        self.zayaka_entry.setPlaceholderText("Enter score")
        self.zayaka_entry.setValidator(QIntValidator(0, 999))
        self.zayaka_entry.setFont(QFont("Arial", 14, QFont.Bold))
        self.zayaka_entry.textChanged.connect(self.on_zayaka_score_changed)
        zayaka_layout.addWidget(zayaka_label)
        zayaka_layout.addWidget(self.zayaka_entry)
        input_layout.addLayout(zayaka_layout)
        
        # Brian's score
        brian_layout = QVBoxLayout()
        brian_label = QLabel("Brian's Score:")
        brian_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.brian_entry = QLineEdit()
        self.brian_entry.setPlaceholderText("Enter score")
        self.brian_entry.setValidator(QIntValidator(0, 999))
        self.brian_entry.setFont(QFont("Arial", 14, QFont.Bold))
        self.brian_entry.textChanged.connect(self.on_brian_score_changed)
        brian_layout.addWidget(brian_label)
        brian_layout.addWidget(self.brian_entry)
        input_layout.addLayout(brian_layout)
        
        entry_layout.addLayout(input_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Scores")
        self.add_button.clicked.connect(self.add_scores)
        self.add_button.setStyleSheet("QPushButton { padding: 10px; font-size: 12px; }")
        button_layout.addWidget(self.add_button)
        
        self.clear_button = QPushButton("Clear Fields")
        self.clear_button.clicked.connect(self.clear_fields)
        self.clear_button.setStyleSheet("QPushButton { padding: 10px; font-size: 12px; }")
        button_layout.addWidget(self.clear_button)
        
        entry_layout.addLayout(button_layout)
        layout.addWidget(entry_frame)
        
        # Current match scores table
        scores_frame = QFrame()
        scores_frame.setFrameStyle(QFrame.Box)
        scores_layout = QVBoxLayout(scores_frame)
        
        scores_title = QLabel("Current Match Scores")
        scores_title.setFont(QFont("Arial", 12, QFont.Bold))
        scores_layout.addWidget(scores_title)
        
        # Create table for current match scores
        self.current_scores_table = QTableWidget()
        self.current_scores_table.setColumnCount(3)
        self.current_scores_table.setHorizontalHeaderLabels([
            "Game #", "Zayaka", "Brian"
        ])
        
        # Set column widths
        header = self.current_scores_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        
        # Set table properties
        self.current_scores_table.setMaximumHeight(200)
        self.current_scores_table.setAlternatingRowColors(True)
        
        scores_layout.addWidget(self.current_scores_table)
        layout.addWidget(scores_frame)
        
        # Current totals
        totals_frame = QFrame()
        totals_frame.setFrameStyle(QFrame.Box)
        totals_layout = QVBoxLayout(totals_frame)
        
        totals_title = QLabel("Current Match Totals")
        totals_title.setFont(QFont("Arial", 12, QFont.Bold))
        totals_layout.addWidget(totals_title)
        
        self.totals_layout = QHBoxLayout()
        self.zayaka_total_label = QLabel("Zayaka: 0")
        self.zayaka_total_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.brian_total_label = QLabel("Brian: 0")
        self.brian_total_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.totals_layout.addWidget(self.zayaka_total_label)
        self.totals_layout.addWidget(self.brian_total_label)
        totals_layout.addLayout(self.totals_layout)
        
        layout.addWidget(totals_frame)
        
        # Status
        self.status_label = QLabel("Enter scores and click 'Add Scores'")
        self.status_label.setStyleSheet("color: #666; padding: 10px;")
        layout.addWidget(self.status_label)
        
        self.tab_widget.addTab(score_widget, "Score Entry")
        
        # Initialize totals and game scores
        self.zayaka_total = 0
        self.brian_total = 0
        self.game_scores = []
        self.update_current_scores_table()
        
    def create_history_tab(self):
        """Create the match history tab"""
        history_widget = QWidget()
        layout = QVBoxLayout(history_widget)
        
        # Title
        title = QLabel("Match History")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Table
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)
        self.history_table.setHorizontalHeaderLabels([
            "Date", "Zayaka Score", "Brian Score", "Winner", "Game Scores", "ID"
        ])
        
        # Set column widths
        header = self.history_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        
        layout.addWidget(self.history_table)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        refresh_button = QPushButton("Refresh History")
        refresh_button.clicked.connect(self.load_match_history)
        button_layout.addWidget(refresh_button)
        
        clear_history_button = QPushButton("Clear All History")
        clear_history_button.clicked.connect(self.clear_match_history)
        button_layout.addWidget(clear_history_button)
        
        layout.addLayout(button_layout)
        
        self.tab_widget.addTab(history_widget, "Match History")
        
    def create_stats_tab(self):
        """Create the statistics tab"""
        stats_widget = QWidget()
        layout = QVBoxLayout(stats_widget)
        
        # Title
        title = QLabel("GinRummy Statistics")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #2c3e50; margin: 10px;")
        layout.addWidget(title)
        
        # Stats display with better styling
        self.stats_text = QTextEdit()
        self.stats_text.setReadOnly(True)
        self.stats_text.setFont(QFont("Courier New", 10))
        self.stats_text.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Courier New', monospace;
            }
        """)
        layout.addWidget(self.stats_text)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        # Refresh button
        refresh_stats_button = QPushButton("🔄 Refresh Statistics")
        refresh_stats_button.clicked.connect(self.update_statistics)
        refresh_stats_button.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        button_layout.addWidget(refresh_stats_button)
        
        # Clear statistics button
        clear_stats_button = QPushButton("🗑️ Clear All Data")
        clear_stats_button.clicked.connect(self.clear_all_data)
        clear_stats_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        button_layout.addWidget(clear_stats_button)
        
        layout.addLayout(button_layout)
        
        # Status label
        self.stats_status_label = QLabel("Statistics ready - click Refresh to update")
        self.stats_status_label.setStyleSheet("color: #6c757d; padding: 5px;")
        self.stats_status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.stats_status_label)
        
        self.tab_widget.addTab(stats_widget, "Statistics")
        
        # Initialize statistics
        self.update_statistics()
        
    def add_scores(self):
        """Add scores to the current match"""
        try:
            zayaka_text = self.zayaka_entry.text().strip()
            brian_text = self.brian_entry.text().strip()
            
            if not zayaka_text and not brian_text:
                self.status_label.setText("Please enter at least one score")
                return
            
            # Determine scores based on which field has a value
            if zayaka_text:
                zayaka_score = int(zayaka_text)
                brian_score = 0
                self.status_label.setText(f"Added score: Zayaka={zayaka_score}, Brian=0")
            elif brian_text:
                brian_score = int(brian_text)
                zayaka_score = 0
                self.status_label.setText(f"Added score: Zayaka=0, Brian={brian_score}")
            else:
                zayaka_score = 0
                brian_score = 0
            
            # Add to totals
            self.zayaka_total += zayaka_score
            self.brian_total += brian_score
            
            # Store game scores
            game_score = f"Zayaka:{zayaka_score}, Brian:{brian_score}"
            self.game_scores.append(game_score)
            
            # Update display
            self.zayaka_total_label.setText(f"Zayaka: {self.zayaka_total}")
            self.brian_total_label.setText(f"Brian: {self.brian_total}")
            
            # Update the current scores table
            self.update_current_scores_table()
            
            # Clear input fields and re-enable them
            self.zayaka_entry.clear()
            self.brian_entry.clear()
            self.zayaka_entry.setEnabled(True)
            self.brian_entry.setEnabled(True)
            self.zayaka_entry.setPlaceholderText("Enter score")
            self.brian_entry.setPlaceholderText("Enter score")
            self.zayaka_entry.setFocus()
            
            # Check for winner
            if self.zayaka_total >= 100 or self.brian_total >= 100:
                self.end_match()
                
        except ValueError:
            self.status_label.setText("Error: Please enter valid numbers")
            
    def end_match(self):
        """End the current match and save to database"""
        winner = "Zayaka" if self.zayaka_total >= 100 else "Brian"
        
        # Save to database
        game_scores_str = "; ".join(self.game_scores)
        self.cursor.execute('''
            INSERT INTO matches (zayaka_score, brian_score, winner, match_date, game_scores)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.zayaka_total, self.brian_total, winner, 
              datetime.now().strftime("%Y-%m-%d %H:%M:%S"), game_scores_str))
        self.conn.commit()
        
        # Show winner message
        QMessageBox.information(self, "Match Complete!", 
                              f"Winner: {winner}\n"
                              f"Final Scores:\n"
                              f"Zayaka: {self.zayaka_total}\n"
                              f"Brian: {self.brian_total}")
        
        # Reset for new match
        self.reset_match()
        
    def reset_match(self):
        """Reset the current match"""
        self.zayaka_total = 0
        self.brian_total = 0
        self.game_scores = []
        self.zayaka_total_label.setText("Zayaka: 0")
        self.brian_total_label.setText("Brian: 0")
        self.status_label.setText("New match started - enter scores")
        self.update_current_scores_table()
        
        # Re-enable both entry fields
        self.zayaka_entry.setEnabled(True)
        self.brian_entry.setEnabled(True)
        self.zayaka_entry.setPlaceholderText("Enter score")
        self.brian_entry.setPlaceholderText("Enter score")
        
    def clear_fields(self):
        """Clear the input fields"""
        self.zayaka_entry.clear()
        self.brian_entry.clear()
        self.zayaka_entry.setEnabled(True)
        self.brian_entry.setEnabled(True)
        self.zayaka_entry.setPlaceholderText("Enter score")
        self.brian_entry.setPlaceholderText("Enter score")
        self.zayaka_entry.setFocus()
        self.status_label.setText("Fields cleared")
        
    def load_match_history(self):
        """Load match history into the table"""
        self.cursor.execute('SELECT * FROM matches ORDER BY match_date DESC')
        matches = self.cursor.fetchall()
        
        self.history_table.setRowCount(len(matches))
        
        for row, match in enumerate(matches):
            for col, value in enumerate(match):
                item = QTableWidgetItem(str(value))
                self.history_table.setItem(row, col, item)
                
    def clear_match_history(self):
        """Clear all match history"""
        reply = QMessageBox.question(self, "Clear History", 
                                   "Are you sure you want to clear all match history?",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.cursor.execute('DELETE FROM matches')
            self.conn.commit()
            self.load_match_history()
            self.update_statistics()
            
    def update_statistics(self):
        """Update the statistics display with comprehensive stats"""
        # Basic match statistics
        self.cursor.execute('SELECT COUNT(*) FROM matches')
        total_matches = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT COUNT(*) FROM matches WHERE winner = "Zayaka"')
        zayaka_wins = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT COUNT(*) FROM matches WHERE winner = "Brian"')
        brian_wins = self.cursor.fetchone()[0]
        
        # Average scores per match
        self.cursor.execute('SELECT AVG(zayaka_score), AVG(brian_score) FROM matches')
        avg_scores = self.cursor.fetchone()
        avg_zayaka_match = avg_scores[0] if avg_scores[0] else 0
        avg_brian_match = avg_scores[1] if avg_scores[1] else 0
        
        # Get all game scores for hand-level analysis
        self.cursor.execute('SELECT game_scores FROM matches')
        all_game_scores = self.cursor.fetchall()
        
        # Parse individual hand scores
        zayaka_hands = []
        brian_hands = []
        total_hands = 0
        
        for match_scores in all_game_scores:
            if match_scores[0]:  # game_scores column
                game_list = match_scores[0].split('; ')
                for game in game_list:
                    if "Zayaka:" in game and "Brian:" in game:
                        try:
                            zayaka_part = game.split("Brian:")[0].replace("Zayaka:", "").strip()
                            brian_part = game.split("Brian:")[1].strip()
                            
                            zayaka_score = int(zayaka_part) if zayaka_part else 0
                            brian_score = int(brian_part) if brian_part else 0
                            
                            zayaka_hands.append(zayaka_score)
                            brian_hands.append(brian_score)
                            total_hands += 1
                        except ValueError:
                            continue
        
        # Calculate hand-level statistics
        avg_zayaka_hand = sum(zayaka_hands) / len(zayaka_hands) if zayaka_hands else 0
        avg_brian_hand = sum(brian_hands) / len(brian_hands) if brian_hands else 0
        
        # Calculate additional statistics
        max_zayaka_hand = max(zayaka_hands) if zayaka_hands else 0
        max_brian_hand = max(brian_hands) if brian_hands else 0
        min_zayaka_hand = min(zayaka_hands) if zayaka_hands else 0
        min_brian_hand = min(brian_hands) if brian_hands else 0
        
        # Calculate win streaks
        self.cursor.execute('SELECT winner FROM matches ORDER BY match_date')
        winners = [row[0] for row in self.cursor.fetchall()]
        
        zayaka_streak = 0
        brian_streak = 0
        current_zayaka_streak = 0
        current_brian_streak = 0
        
        for winner in winners:
            if winner == "Zayaka":
                current_zayaka_streak += 1
                current_brian_streak = 0
                zayaka_streak = max(zayaka_streak, current_zayaka_streak)
            else:
                current_brian_streak += 1
                current_zayaka_streak = 0
                brian_streak = max(brian_streak, current_brian_streak)
        
        # Calculate match duration statistics (games per match)
        self.cursor.execute('SELECT game_scores FROM matches')
        match_games = []
        for match in self.cursor.fetchall():
            if match[0]:
                games_in_match = len(match[0].split('; '))
                match_games.append(games_in_match)
        
        avg_games_per_match = sum(match_games) / len(match_games) if match_games else 0
        max_games_per_match = max(match_games) if match_games else 0
        min_games_per_match = min(match_games) if match_games else 0
        
        # Calculate scoring efficiency (hands with non-zero scores)
        zayaka_non_zero = sum(1 for score in zayaka_hands if score > 0)
        brian_non_zero = sum(1 for score in brian_hands if score > 0)
        
        zayaka_efficiency = (zayaka_non_zero / len(zayaka_hands) * 100) if zayaka_hands else 0
        brian_efficiency = (brian_non_zero / len(brian_hands) * 100) if brian_hands else 0
        
        # Calculate win percentages
        zayaka_win_pct = (zayaka_wins / total_matches * 100) if total_matches > 0 else 0
        brian_win_pct = (brian_wins / total_matches * 100) if total_matches > 0 else 0
        
        # Format statistics text
        stats_text = f"""
GinRummy Statistics
==================

MATCH STATISTICS
----------------
Total Matches: {total_matches}
Average Games per Match: {avg_games_per_match:.1f}
Longest Match: {max_games_per_match} games
Shortest Match: {min_games_per_match} games

WIN STATISTICS
--------------
Zayaka Wins: {zayaka_wins} ({zayaka_win_pct:.1f}%)
Brian Wins: {brian_wins} ({brian_win_pct:.1f}%)

Win Streaks:
- Zayaka: {zayaka_streak} consecutive wins
- Brian: {brian_streak} consecutive wins

MATCH AVERAGES
--------------
Zayaka Average per Match: {avg_zayaka_match:.1f} points
Brian Average per Match: {avg_brian_match:.1f} points

HAND STATISTICS
---------------
Total Hands Played: {total_hands}

Average Score per Hand:
- Zayaka: {avg_zayaka_hand:.1f} points
- Brian: {avg_brian_hand:.1f} points

Hand Score Ranges:
- Zayaka: {min_zayaka_hand} - {max_zayaka_hand} points
- Brian: {min_brian_hand} - {max_brian_hand} points

Scoring Efficiency (Non-Zero Hands):
- Zayaka: {zayaka_efficiency:.1f}% ({zayaka_non_zero}/{len(zayaka_hands)} hands)
- Brian: {brian_efficiency:.1f}% ({brian_non_zero}/{len(brian_hands)} hands)

PERFORMANCE METRICS
------------------
Most Consistent Player: {"Zayaka" if abs(avg_zayaka_hand - avg_brian_hand) < 2 else "Brian"}
Highest Single Hand: {"Zayaka" if max_zayaka_hand > max_brian_hand else "Brian"} ({max(max_zayaka_hand, max_brian_hand)} points)
Most Efficient Scorer: {"Zayaka" if zayaka_efficiency > brian_efficiency else "Brian"} ({max(zayaka_efficiency, brian_efficiency):.1f}%)

Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        """
        
        self.stats_text.setText(stats_text)
        
        # Update status label
        if hasattr(self, 'stats_status_label'):
            if total_matches > 0:
                self.stats_status_label.setText(f"Statistics updated - {total_matches} matches, {total_hands} hands analyzed")
            else:
                self.stats_status_label.setText("No match data available - play some games to see statistics")
        
    def on_zayaka_score_changed(self, text):
        """Handle Zayaka score entry changes - block Brian's entry if Zayaka has a score"""
        if text.strip():
            self.brian_entry.setEnabled(False)
            self.brian_entry.setPlaceholderText("Blocked - Zayaka has score")
            self.brian_entry.clear()
        else:
            self.brian_entry.setEnabled(True)
            self.brian_entry.setPlaceholderText("Enter score")
    
    def on_brian_score_changed(self, text):
        """Handle Brian score entry changes - block Zayaka's entry if Brian has a score"""
        if text.strip():
            self.zayaka_entry.setEnabled(False)
            self.zayaka_entry.setPlaceholderText("Blocked - Brian has score")
            self.zayaka_entry.clear()
        else:
            self.zayaka_entry.setEnabled(True)
            self.zayaka_entry.setPlaceholderText("Enter score")
    
    def update_current_scores_table(self):
        """Update the current match scores table"""
        self.current_scores_table.setRowCount(len(self.game_scores))
        
        for row, game_score in enumerate(self.game_scores):
            # Parse the game score string
            if "Zayaka:" in game_score and "Brian:" in game_score:
                zayaka_part = game_score.split("Brian:")[0].replace("Zayaka:", "").strip()
                brian_part = game_score.split("Brian:")[1].strip()
                
                zayaka_score = zayaka_part if zayaka_part else "0"
                brian_score = brian_part if brian_part else "0"
            else:
                zayaka_score = "0"
                brian_score = "0"
            
            # Add game number
            game_num_item = QTableWidgetItem(f"Game {row + 1}")
            game_num_item.setTextAlignment(Qt.AlignCenter)
            self.current_scores_table.setItem(row, 0, game_num_item)
            
            # Add Zayaka score
            zayaka_item = QTableWidgetItem(zayaka_score)
            zayaka_item.setTextAlignment(Qt.AlignCenter)
            zayaka_item.setFont(QFont("Arial", 12, QFont.Bold))
            self.current_scores_table.setItem(row, 1, zayaka_item)
            
            # Add Brian score
            brian_item = QTableWidgetItem(brian_score)
            brian_item.setTextAlignment(Qt.AlignCenter)
            brian_item.setFont(QFont("Arial", 12, QFont.Bold))
            self.current_scores_table.setItem(row, 2, brian_item)
        
        # Add totals row if there are games
        if self.game_scores:
            self.current_scores_table.setRowCount(len(self.game_scores) + 1)
            
            # Totals row
            totals_row = len(self.game_scores)
            
            # Game number for totals
            totals_num_item = QTableWidgetItem("TOTALS")
            totals_num_item.setTextAlignment(Qt.AlignCenter)
            totals_num_item.setFont(QFont("Arial", 16, QFont.Bold))  # 30% bigger (12 * 1.3 ≈ 16)
            totals_num_item.setForeground(Qt.red)
            self.current_scores_table.setItem(totals_row, 0, totals_num_item)
            
            # Zayaka total
            zayaka_total_item = QTableWidgetItem(str(self.zayaka_total))
            zayaka_total_item.setTextAlignment(Qt.AlignCenter)
            zayaka_total_item.setFont(QFont("Arial", 16, QFont.Bold))  # 30% bigger (12 * 1.3 ≈ 16)
            zayaka_total_item.setForeground(Qt.red)
            zayaka_total_item.setBackground(self.current_scores_table.palette().alternateBase())
            self.current_scores_table.setItem(totals_row, 1, zayaka_total_item)
            
            # Brian total
            brian_total_item = QTableWidgetItem(str(self.brian_total))
            brian_total_item.setTextAlignment(Qt.AlignCenter)
            brian_total_item.setFont(QFont("Arial", 16, QFont.Bold))  # 30% bigger (12 * 1.3 ≈ 16)
            brian_total_item.setForeground(Qt.red)
            brian_total_item.setBackground(self.current_scores_table.palette().alternateBase())
            self.current_scores_table.setItem(totals_row, 2, brian_total_item)
        
    def clear_all_data(self):
        """Clear all match history and statistics"""
        reply = QMessageBox.question(self, "Clear All Data", 
                                   "Are you sure you want to clear all match history and statistics?",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.cursor.execute('DELETE FROM matches')
            self.conn.commit()
            self.load_match_history()
            self.update_statistics()
            self.stats_status_label.setText("All data cleared - click Refresh to update")
            self.stats_text.clear()
            QMessageBox.information(self, "Data Cleared", "All match history and statistics have been cleared.")
            
    def closeEvent(self, event):
        """Handle application close"""
        self.conn.close()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = GinRummyTracker()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
