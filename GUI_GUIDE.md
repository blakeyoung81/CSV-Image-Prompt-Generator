# 🎨 GUI User Guide

Complete guide to using the Medical Study Prompt Generator graphical interface.

---

## 🚀 Launching the GUI

### Method 1: Launcher Script (Recommended)
```bash
./launch_gui.sh
```

### Method 2: Direct Python
```bash
python3 gui_app.py
```

### Method 3: Double-Click (macOS/Linux)
Make `gui_app.py` executable and double-click it:
```bash
chmod +x gui_app.py
```

---

## 📖 Interface Overview

The GUI is organized into 5 main sections:

### 1. 🔑 OpenAI API Configuration
- Shows API key status (✅ Configured or ⚠️ Required)
- Button to enter or change API key
- **First time?** A popup will automatically appear asking for your key

### 2. 📝 Input Description
- **"What is the nature of your input?"**
  - Default: "An NBME exam of 50 questions with some explanations..."
  - Customize this to describe your specific exam format
  
- **"How many questions do you want to generate?"**
  - Default: 50
  - Set to "auto" to automatically detect question count
  - Or enter any specific number

### 3. 📁 File Selection
- **Input Exam PDF:** Your NBME/USMLE exam PDF
- **First Aid PDF:** Your First Aid textbook PDF
- **Output CSV File:** Where to save the results
- Each has a "Browse" button for easy file selection
- Auto-detects PDFs in the current directory on startup

### 4. 📊 Progress
- **Progress Bar:** Shows generation is running
- **Status Log:** Real-time updates on what's happening
  - Loading First Aid
  - Extracting questions
  - Processing each question
  - Final results

### 5. 🚀 Generate Button
- Big green button at the bottom
- Click to start generation
- Disabled during processing to prevent duplicate runs

---

## 🔐 First-Time Setup: API Key

### When You Launch Without an API Key

A popup will appear asking for your OpenAI API key:

**Steps:**
1. Visit https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Paste it into the popup dialog
6. Click "Save"

**What Happens:**
- The key is saved to a `.env` file
- The GUI restarts to load the new configuration
- ✅ You're ready to generate prompts!

**Security:**
- Your API key is stored locally in `.env`
- The `.env` file is git-ignored (never uploaded to GitHub)
- The key field shows `****` for security

---

## 📝 Customizing Input Description

The input description helps the AI understand your exam format.

### Default Description
```
An NBME exam of 50 questions with some explanations 
that needs to be enriched by firstaid and made into prompts
```

### Custom Examples

**For a shorter exam:**
```
An NBME practice block with 40 questions that needs 
detailed explanations enriched with First Aid content
```

**For UWorld questions:**
```
A UWorld question block with explanations requiring 
comprehensive First Aid integration and pathophysiology details
```

**For custom question bank:**
```
A custom medical question bank focusing on [TOPIC] 
that needs First Aid enrichment and clinical correlation
```

### Tips:
- Be specific about the exam type
- Mention any special focus areas
- Keep it concise but descriptive

---

## 🔢 Setting Question Count

### Options:

**1. Specific Number (Default: 50)**
```
Enter: 50
```
- Processes exactly 50 questions
- Good when you know the exact count

**2. Auto-Detection**
```
Enter: auto
```
- Automatically detects how many questions are in the PDF
- Recommended for varying exam lengths

**3. Custom Range**
```
Enter: 25
```
- Processes 25 questions
- Useful for partial processing or testing

---

## 📁 File Selection Guide

### Input Exam PDF

**What it is:** Your medical exam PDF (NBME, USMLE, UWorld, etc.)

**Requirements:**
- Must be a PDF file
- Should have extractable text (OCR'd if scanned)
- Questions should be numbered

**Example names:**
- `NBME 30 A Part 2-ocr.pdf`
- `UWorld Block 1.pdf`
- `Practice Exam.pdf`

### First Aid PDF

**What it is:** Your First Aid medical textbook PDF

**Requirements:**
- Must be a PDF file
- Should have extractable text
- Any edition works (latest recommended)

**Common names:**
- `first aid.pdf`
- `First Aid Step 1 2026.pdf`
- `firstaid.pdf`

**Auto-detection:** The GUI automatically looks for files named:
- `first aid.pdf`
- `firstaid.pdf`
- `First Aid.pdf`

### Output CSV File

**What it is:** Where your generated study prompts will be saved

**Format:** CSV (Comma-Separated Values)

**Default naming:** `[input_filename]_study_prompts.csv`

**Example:**
- Input: `NBME 30.pdf`
- Output: `NBME 30_study_prompts.csv`

---

## 📊 Understanding Progress Updates

### What You'll See:

#### 1. Initialization
```
============================================================
Medical Study Prompt Generator
============================================================

Loading First Aid reference from: first aid.pdf
✓ Loaded 2271995 characters from First Aid
```

#### 2. Question Extraction
```
Extracting questions from: input.pdf
  Using NBME format pattern (found 50 markers)
✓ Extracted 50 questions
```

#### 3. Processing Each Question
```
[1/50] Processing Question 1...
  → Identifying key concepts...
  → Concepts: Allosteric activators; enzyme kinetics...
  → Generating enriched prompt...
  ✓ Complete
```

This repeats for all 50 questions.

#### 4. Completion
```
============================================================
✓ Successfully generated 50 study prompts!
✓ Output saved to: output.csv
============================================================
```

### Time Estimates:
- **Per question:** 6-12 seconds
- **50 questions:** 5-10 minutes
- **Grab a coffee!** ☕

---

## ✅ Success! What Happens Next

### Completion Dialog

A popup appears:
```
Success!

Successfully generated 50 study prompts!

Saved to:
/path/to/your/output.csv
```

### Your CSV File

**Location:** Where you specified in "Output CSV File"

**Format:**
```csv
Question Number,Prompt
1,"Professionally condense and explain..."
2,"Professionally condense and explain..."
...
```

### What to Do With It:

1. **Open in Excel/Google Sheets**
   - Import the CSV
   - Read and organize prompts

2. **Use with AI Study Tools**
   - Copy prompts to ChatGPT/Claude
   - Ask for detailed explanations

3. **Create Anki Cards**
   - Front: Question number
   - Back: The enriched prompt

4. **Build Study Guides**
   - Organize by topic
   - Add your own notes

---

## 🐛 Troubleshooting

### "Please enter your OpenAI API key!"

**Solution:** Click "Enter API Key" button and follow the setup steps.

### "Please select a valid input PDF file!"

**Causes:**
- No file selected
- File doesn't exist
- Wrong file format

**Solution:** Click "Select Input PDF" and choose a valid PDF file.

### "Please select a valid First Aid PDF file!"

**Causes:**
- No First Aid PDF selected
- File doesn't exist

**Solution:** Click "Select First Aid PDF" and choose your First Aid textbook PDF.

### GUI Won't Launch

**Check:**
```bash
# Test if tkinter is installed
python3 -c "import tkinter"
```

**If error on macOS:**
```bash
brew install python-tk
```

**If error on Linux:**
```bash
sudo apt-get install python3-tk
```

### Progress Stuck

**If the progress bar stops:**
- Check the status log for error messages
- The API might be rate-limited (wait 60 seconds)
- Check your internet connection

### API Errors

**Common issues:**
- Invalid API key
- No billing/credits on OpenAI account
- Rate limit exceeded
- Network connection issues

**Solutions:**
1. Verify your API key at https://platform.openai.com/api-keys
2. Check billing at https://platform.openai.com/settings/organization/billing
3. Wait a minute and try again
4. Check internet connection

---

## 💡 Pro Tips

### 1. Auto-Detection is Smart
- Place your PDFs in the same directory as the GUI
- The GUI will automatically find and select them
- Saves time on file selection

### 2. Customize for Better Results
- Update the input description to match your exam type
- More specific descriptions = better AI understanding

### 3. Monitor Progress
- Watch the status log to see which question is processing
- Estimated time: ~10 seconds per question

### 4. Keep the Window Open
- Don't close the GUI while generating
- The progress will complete automatically

### 5. Save Your Settings
- The API key is saved permanently to `.env`
- You only need to enter it once

### 6. Batch Processing
- Generate one exam, then load another
- Keep the GUI open and process multiple exams
- Output files won't overwrite (different names)

---

## 🎨 Interface Tips

### Keyboard Shortcuts
- **Tab:** Move between fields
- **Enter:** (in API key dialog) Save key
- **Ctrl/Cmd + C:** Copy from status log

### Window Features
- **Resizable:** Drag corners to resize
- **Scrollable:** Status log auto-scrolls
- **Always accessible:** Window stays on top during generation

### Copy Status Log
- Click in the status text area
- Select text (Ctrl/Cmd + A for all)
- Copy (Ctrl/Cmd + C)
- Useful for debugging or keeping records

---

## 🔄 Updating the GUI

### When Updates Are Available

```bash
cd "/path/to/CSV Generator"
git pull origin main
pip3 install -r requirements.txt --upgrade
```

### Your Settings Are Safe
- `.env` file is never overwritten
- Your API key remains configured
- PDF selections reset (that's normal)

---

## 📚 More Help

- **Full Documentation:** See `README.md`
- **Quick Start:** See `START_HERE.md`
- **Examples:** See `USAGE_EXAMPLES.md`
- **Technical Details:** See `PROJECT_SUMMARY.md`

---

## 🎉 You're Ready!

The GUI makes generating study prompts effortless. Just:
1. ✅ Enter your API key (first time only)
2. ✅ Select your PDF files
3. ✅ Click "Generate"
4. ☕ Wait 5-10 minutes
5. 🎓 Study with your enriched prompts!

**Happy studying!** 📚✨
