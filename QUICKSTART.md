# Quick Start Guide

Get up and running in 3 minutes! ⚡

## Step 1: Install (30 seconds)

```bash
# Run the setup script
./setup.sh

# OR manually:
pip3 install -r requirements.txt
```

## Step 2: Configure (1 minute)

### Get OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it

### Add to .env file
```bash
echo 'OPENAI_API_KEY=sk-your-actual-key-here' > .env
```

## Step 3: Add Files (30 seconds)

Put these files in this folder:
- ✅ `firstaid.pdf` (your First Aid textbook PDF)
- ✅ Your exam PDF (e.g., `NBME 30 A Part 2-ocr.pdf`)

## Step 4: Run! (5-10 minutes)

### Option A: Interactive Mode (Easiest)
```bash
python3 run.py
```
It will show you available PDFs and let you choose!

### Option B: Direct Command
```bash
python3 generate_study_prompts.py "NBME 30 A Part 2-ocr.pdf"
```

### Option C: Custom Output Name
```bash
python3 generate_study_prompts.py "My Exam.pdf" "my_output.csv"
```

## What Happens?

The script will:
1. 📄 Extract all 50 questions from your exam PDF
2. 🧠 Use AI to identify key concepts in each question
3. 📚 Find relevant First Aid content
4. ✨ Generate enriched study prompts
5. 💾 Save to CSV file

Progress is shown in real-time:
```
[1/50] Processing Question 1...
  → Identifying key concepts...
  → Concepts: Allosteric activators; enzyme kinetics...
  → Generating enriched prompt...
  ✓ Complete
```

## Output

You'll get a CSV file like:
```
NBME 30 A Part 2-ocr_study_prompts.csv
```

With format:
```csv
Question Number,Prompt
1,"Professionally condense and explain..."
2,"Professionally condense and explain..."
```

## Cost

- ~$0.30-0.50 per 50-question exam (using GPT-4o)
- Cheaper if you use GPT-3.5 (but lower quality)

## Troubleshooting

### "No questions found"
- Make sure your PDF has selectable text (not just an image)
- Try opening the PDF and copying text - if you can't, it needs OCR first

### "API key not found"
```bash
# Check .env file exists
ls -la .env

# Check contents (without showing key)
cat .env | grep OPENAI_API_KEY
```

### "firstaid.pdf not found"
```bash
# List PDFs in folder
ls -la *.pdf

# Make sure it's named exactly "firstaid.pdf"
```

### Script is slow
- Normal! Processing 50 questions takes 5-10 minutes
- Each question makes 2 API calls to GPT-4
- Grab a coffee ☕

## Tips

1. **Better PDFs = Better Results**
   - Use OCR'd PDFs with selectable text
   - Clean PDFs work better than scanned ones

2. **Batch Processing**
   - Process multiple exams in one session
   - Your API costs will be similar

3. **Review Output**
   - Check the first few prompts to ensure quality
   - If prompts seem off, the PDF might not have parsed correctly

4. **Customize**
   - Edit `generate_study_prompts.py` to change prompt style
   - Modify temperature (0.3-0.7) for creativity vs accuracy balance

## Need Help?

Check the full README.md for detailed documentation!
