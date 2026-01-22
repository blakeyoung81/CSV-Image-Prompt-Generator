#!/bin/bash

echo "================================================"
echo "Medical Study Prompt Generator - Setup"
echo "================================================"
echo

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo

# Install requirements
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

echo
echo "================================================"
echo "⚙️  Configuration Needed"
echo "================================================"
echo
echo "1. Create .env file with your OpenAI API key:"
echo "   echo 'OPENAI_API_KEY=sk-your-key-here' > .env"
echo
echo "   Get your key from: https://platform.openai.com/api-keys"
echo
echo "2. Add your firstaid.pdf to this directory"
echo
echo "3. Run the script:"
echo "   python3 generate_study_prompts.py 'your-exam.pdf'"
echo
echo "================================================"
echo "✓ Setup complete!"
echo "================================================"
