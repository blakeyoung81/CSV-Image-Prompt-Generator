#!/bin/bash

# Launch the Medical Study Prompt Generator Web Interface

cd "$(dirname "$0")"

echo "======================================================================"
echo "🌐 Medical Study Prompt Generator - Web Interface"
echo "======================================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Install dependencies if needed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

echo "🚀 Starting web server..."
echo ""
echo "======================================================================"
echo ""
echo "  👉 Open your browser and go to: http://localhost:5000"
echo ""
echo "======================================================================"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Launch web app
python3 web_app.py
