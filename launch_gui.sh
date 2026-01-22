#!/bin/bash

# Launch the Medical Study Prompt Generator GUI

cd "$(dirname "$0")"

echo "🚀 Launching Medical Study Prompt Generator..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "❌ tkinter is not installed!"
    echo "Install with: brew install python-tk (macOS)"
    exit 1
fi

# Install dependencies if needed
if ! python3 -c "import PyPDF2" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Launch GUI
python3 gui_app.py
