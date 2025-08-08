#!/bin/bash

# GinRummyTracker - Add Files to Xcode Project Script
# This script copies all necessary files and provides detailed instructions

echo "🎯 GinRummyTracker - Add Files to Xcode Project"
echo "================================================"
echo ""

# Check if we're in the right directory
if [ ! -d "GinRummyTracker" ]; then
    echo "❌ Error: Please run this script from the GinRummyTracker directory"
    echo "Current directory: $(pwd)"
    echo "Expected: /Users/briangreen/ff2/GinRummyTracker"
    exit 1
fi

echo "✅ Found GinRummyTracker directory"
echo ""

# List all files that will be copied
echo "📁 Files to be copied:"
echo "----------------------"
ls -la GinRummyTracker/*.swift
echo ""
ls -la GinRummyTracker/Assets.xcassets
echo ""
ls -la "GinRummyTracker/Preview Content"
echo ""

# Ask user for target directory
echo "🎯 STEP 1: Enter your Xcode project directory"
echo "Example: /Users/briangreen/Desktop/MyNewProject"
echo ""
read -p "Enter the path to your Xcode project: " TARGET_DIR

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ Error: Target directory does not exist: $TARGET_DIR"
    exit 1
fi

echo "✅ Target directory found: $TARGET_DIR"
echo ""

# Copy all Swift files
echo "📋 STEP 2: Copying Swift files..."
cp GinRummyTracker/*.swift "$TARGET_DIR/"
echo "✅ Copied Swift files:"
ls "$TARGET_DIR"/*.swift
echo ""

# Copy Assets
echo "📋 STEP 3: Copying Assets..."
if [ -d "$TARGET_DIR/Assets.xcassets" ]; then
    echo "⚠️  Assets.xcassets already exists in target. Backing up..."
    mv "$TARGET_DIR/Assets.xcassets" "$TARGET_DIR/Assets.xcassets.backup"
fi
cp -r GinRummyTracker/Assets.xcassets "$TARGET_DIR/"
echo "✅ Copied Assets.xcassets"
echo ""

# Copy Preview Content
echo "📋 STEP 4: Copying Preview Content..."
if [ -d "$TARGET_DIR/Preview Content" ]; then
    echo "⚠️  Preview Content already exists in target. Backing up..."
    mv "$TARGET_DIR/Preview Content" "$TARGET_DIR/Preview Content.backup"
fi
cp -r "GinRummyTracker/Preview Content" "$TARGET_DIR/"
echo "✅ Copied Preview Content"
echo ""

echo "🎉 STEP 5: Files copied successfully!"
echo "====================================="
echo ""
echo "📱 Now follow these steps in Xcode:"
echo ""
echo "1. Open your Xcode project"
echo "2. In the Project Navigator (left panel), right-click on your project"
echo "3. Select 'Add Files to [ProjectName]'"
echo "4. Navigate to: $TARGET_DIR"
echo "5. Select ALL the following files:"
echo ""

# List files to add
echo "   Swift Files:"
for file in "$TARGET_DIR"/*.swift; do
    if [ -f "$file" ]; then
        echo "   - $(basename "$file")"
    fi
done

echo ""
echo "   Asset Files:"
echo "   - Assets.xcassets (folder)"
echo "   - Preview Content (folder)"
echo ""

echo "6. Make sure 'Add to target' is checked for your app target"
echo "7. Click 'Add'"
echo ""
echo "8. Build and run (⌘+R)"
echo ""
echo "🎯 Your GinRummyTracker app should now work with:"
echo "   - Large, bold fonts (36pt for scores)"
echo "   - Color coding (Zayaka blue, Brian green)"
echo "   - Tab navigation (Score Entry, History, Statistics)"
echo "   - Data persistence (saves matches locally)"
echo ""
echo "📁 Files copied to: $TARGET_DIR"
echo ""

# Create a summary file
SUMMARY_FILE="$TARGET_DIR/GinRummyTracker_Setup_Summary.txt"
cat > "$SUMMARY_FILE" << EOF
GinRummyTracker Setup Summary
============================

Files copied to: $TARGET_DIR

Swift Files:
$(ls "$TARGET_DIR"/*.swift 2>/dev/null | sed 's/.*\//- /')

Asset Files:
- Assets.xcassets (folder)
- Preview Content (folder)

Next Steps in Xcode:
1. Open your Xcode project
2. Right-click on project in navigator
3. Select 'Add Files to [ProjectName]'
4. Select all copied files
5. Make sure 'Add to target' is checked
6. Click 'Add'
7. Build and run (⌘+R)

Features:
- Large, bold fonts (36pt for scores)
- Color coding (Zayaka blue, Brian green)
- Tab navigation (Score Entry, History, Statistics)
- Data persistence (saves matches locally)

Generated: $(date)
EOF

echo "📝 Setup summary saved to: $SUMMARY_FILE"
echo ""
echo "🎉 Setup complete! Follow the Xcode steps above to add files to your project."
