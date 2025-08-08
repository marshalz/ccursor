# GinRummy Score Tracker - iOS App

A native iOS application for tracking GinRummy scores between Zayaka and Brian, built with SwiftUI.

## Features

- **Score Entry**: Enter individual game scores with large, bold fonts for easy visibility
- **Match Tracking**: Automatically tracks current match totals and determines winners
- **Match History**: View all completed matches with detailed information
- **Statistics**: Comprehensive statistics including win rates and average scores
- **Data Persistence**: All data is saved locally using UserDefaults

## Requirements

- iOS 17.0 or later
- Xcode 15.0 or later
- Swift 5.0

## Installation

1. Open the `GinRummyTracker.xcodeproj` file in Xcode
2. Select your target device or simulator
3. Build and run the project (⌘+R)

## Usage

### Score Entry
- Enter Zayaka's and Brian's scores for each game
- Tap "Add Scores" to record the scores
- The app automatically tracks running totals
- When either player reaches 100 points, the match ends

### History
- View all completed matches
- See final scores, winners, and game details
- Clear all history if needed

### Statistics
- View total matches played
- See win rates for each player
- Check average scores
- Statistics update automatically as you play

## App Structure

- `GinRummyTrackerApp.swift`: Main app entry point
- `ContentView.swift`: Tab navigation container
- `ScoreEntryView.swift`: Score input interface with large, bold fonts
- `HistoryView.swift`: Match history display
- `StatsView.swift`: Statistics and analytics
- `MatchModel.swift`: Data models and business logic

## Design Features

- **Large, Bold Fonts**: Score displays use 36pt bold fonts for easy reading
- **Color Coding**: Zayaka (blue) and Brian (green) for easy identification
- **Modern UI**: Clean, iOS-native design with proper spacing and typography
- **Responsive**: Works on both iPhone and iPad
- **Accessibility**: Proper contrast and readable fonts

## Data Storage

The app uses UserDefaults to persist match data locally. All data is stored on the device and can be cleared through the app interface.

## Development

This app is built using:
- SwiftUI for the user interface
- MVVM architecture pattern
- UserDefaults for data persistence
- Swift 5.0 language features

## Screenshots

The app includes three main tabs:
1. **Score Entry**: Large input fields and current totals display
2. **History**: List of all completed matches
3. **Statistics**: Charts and analytics of match data

## License

This project is for personal use and educational purposes.
