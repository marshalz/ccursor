# How to Run the GinRummyTracker iOS App

## Method 1: Create New iOS Project (Recommended)

### Step 1: Create New Project
1. **Open Xcode**
2. **File → New → Project**
3. **Choose**: iOS → App
4. **Product Name**: GinRummyTracker
5. **Interface**: SwiftUI
6. **Language**: Swift
7. **Save to**: Choose any location

### Step 2: Replace Files
Replace the generated files with our custom files:

1. **Delete** the generated `ContentView.swift`
2. **Copy** our files from `/Users/briangreen/ff2/GinRummyTracker/GinRummyTracker/`:
   - `ContentView.swift`
   - `ScoreEntryView.swift`
   - `HistoryView.swift`
   - `StatsView.swift`
   - `MatchModel.swift`
   - `DatabaseManager.swift`

### Step 3: Run the App
1. **Select a simulator** (iPhone 15, iPad, etc.)
2. **Press ⌘+R** or click the ▶️ button
3. **The app will launch** in the simulator

## Method 2: Open as Swift Package

### Step 1: Open Package
1. **Open Xcode**
2. **File → Open...**
3. **Navigate to**: `/Users/briangreen/ff2/GinRummyTracker/`
4. **Select**: `Package.swift`
5. **Click**: "Open"

### Step 2: Add iOS Target
1. **Right-click** on the package in the navigator
2. **Add Target**
3. **Choose**: iOS → App
4. **Name**: GinRummyTracker
5. **Copy** our Swift files to the new target

### Step 3: Run
1. **Select the iOS target**
2. **Choose simulator**
3. **Press ⌘+R**

## Method 3: Quick Test

### Step 1: Open Individual Files
1. **Open Xcode**
2. **File → Open...**
3. **Navigate to**: `/Users/briangreen/ff2/GinRummyTracker/GinRummyTracker/`
4. **Select**: `GinRummyTrackerApp.swift`
5. **Click**: "Open"

### Step 2: Create New Project
1. **File → New → Project**
2. **iOS → App**
3. **Copy** all our Swift files to the new project
4. **Run** with ⌘+R

## What You'll See

The app has **3 tabs**:

1. **Score Entry**: 
   - Large, bold input fields (24pt)
   - Current totals display (36pt bold)
   - Add/Clear buttons

2. **History**: 
   - List of all completed matches
   - Winner, scores, and dates

3. **Statistics**: 
   - Win rates and averages
   - Total matches played

## Features

- ✅ **Large, Bold Fonts**: 36pt bold for score displays
- ✅ **Color Coding**: Zayaka (blue), Brian (green)
- ✅ **Touch-Friendly**: Optimized for iOS
- ✅ **Data Persistence**: Saves all matches locally
- ✅ **Modern UI**: SwiftUI with proper iOS design

## Troubleshooting

**If you get build errors:**
1. Make sure all Swift files are in the project
2. Check that iOS deployment target is 17.0+
3. Clean build folder (⌘+Shift+K)
4. Rebuild (⌘+B)

**If the app doesn't run:**
1. Select a valid iOS simulator
2. Make sure the target is selected
3. Check that the main app file has `@main`

The app should run perfectly on both iPhone and iPad simulators! 🎯
