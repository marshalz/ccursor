# How to Open GinRummyTracker in Xcode

## Option 1: Open as Swift Package (Recommended)

1. **Open Xcode**
2. **File → Open...** (or press ⌘+O)
3. **Navigate to**: `/Users/briangreen/ff2/GinRummyTracker/`
4. **Select**: `Package.swift`
5. **Click**: "Open"

This will open the project as a Swift Package, which is more reliable than the Xcode project file.

## Option 2: Create New Xcode Project

If the above doesn't work, create a new iOS project:

1. **Open Xcode**
2. **File → New → Project**
3. **Choose**: iOS → App
4. **Product Name**: GinRummyTracker
5. **Interface**: SwiftUI
6. **Language**: Swift
7. **Save to**: `/Users/briangreen/ff2/GinRummyTracker/`
8. **Replace** the generated files with our custom files:
   - `GinRummyTrackerApp.swift`
   - `ContentView.swift`
   - `ScoreEntryView.swift`
   - `HistoryView.swift`
   - `StatsView.swift`
   - `MatchModel.swift`
   - `DatabaseManager.swift`

## Option 3: Open Individual Files

You can also open individual Swift files in Xcode:

1. **Open Xcode**
2. **File → Open...**
3. **Navigate to**: `/Users/briangreen/ff2/GinRummyTracker/GinRummyTracker/`
4. **Select any Swift file** (e.g., `GinRummyTrackerApp.swift`)
5. **Click**: "Open"

## Project Structure

```
GinRummyTracker/
├── Package.swift                    ← Swift Package manifest
├── GinRummyTracker.xcodeproj/      ← Xcode project (may not work)
├── GinRummyTracker/                ← Source code
│   ├── GinRummyTrackerApp.swift    ← Main app entry point
│   ├── ContentView.swift           ← Tab navigation
│   ├── ScoreEntryView.swift        ← Score input with large fonts
│   ├── HistoryView.swift           ← Match history
│   ├── StatsView.swift             ← Statistics
│   ├── MatchModel.swift            ← Data models
│   ├── DatabaseManager.swift       ← Data persistence
│   └── Assets.xcassets/           ← App assets
└── README.md                       ← Project documentation
```

## Features

- **Large, Bold Fonts**: Score displays use 36pt bold fonts
- **Color Coding**: Zayaka (blue) and Brian (green)
- **Tab Navigation**: Score Entry, History, Statistics
- **Data Persistence**: Uses UserDefaults for local storage
- **Modern UI**: SwiftUI with proper iOS design patterns

## Troubleshooting

If you encounter issues:

1. **Make sure Xcode is installed** (not just command line tools)
2. **Try opening as Swift Package** (Option 1 above)
3. **Create a new project** and copy our files (Option 2 above)
4. **Check iOS deployment target** (should be iOS 17.0+)

The app should work on both iPhone and iPad with the large, bold fonts you requested!
