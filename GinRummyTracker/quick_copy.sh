#!/bin/bash

# Quick copy command for GinRummyTracker files
# Usage: ./quick_copy.sh /path/to/your/xcode/project

if [ $# -eq 0 ]; then
    echo "❌ Error: Please provide the target Xcode project directory"
    echo "Usage: ./quick_copy.sh /path/to/your/xcode/project"
    echo ""
    echo "Example: ./quick_copy.sh /Users/briangreen/Desktop/MyNewProject"
    exit 1
fi

TARGET_DIR="$1"

echo "🎯 Copying GinRummyTracker files to: $TARGET_DIR"
echo ""

# Copy all files
cp GinRummyTracker/*.swift "$TARGET_DIR/"
cp -r GinRummyTracker/Assets.xcassets "$TARGET_DIR/"
cp -r "GinRummyTracker/Preview Content" "$TARGET_DIR/"

echo "✅ Files copied successfully!"
echo ""
echo "📱 Next steps in Xcode:"
echo "1. Open your Xcode project"
echo "2. Right-click on project → 'Add Files to [ProjectName]'"
echo "3. Select all copied files"
echo "4. Make sure 'Add to target' is checked"
echo "5. Click 'Add'"
echo "6. Build and run (⌘+R)"
echo ""
echo "🎯 Your app will have:"
echo "   - Large, bold fonts (36pt for scores)"
echo "   - Color coding (Zayaka blue, Brian green)"
echo "   - Tab navigation (Score Entry, History, Statistics)"
echo "   - Data persistence (saves matches locally)"
