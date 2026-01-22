# 🚀 START HERE

Welcome! This tool generates enriched study prompts from medical exam PDFs using AI + First Aid.

---

## ⚡ 60-Second Quick Start

```bash
# 1. Install
pip3 install -r requirements.txt

# 2. Get API key from https://platform.openai.com/api-keys

# 3. Configure
echo 'OPENAI_API_KEY=sk-your-actual-key-here' > .env

# 4. Test
python3 test_api.py

# 5. Add your files
# - firstaid.pdf (First Aid textbook)
# - exam.pdf (NBME/USMLE exam)

# 6. Run!
python3 run.py
```

**That's it!** 🎉

---

## 📚 What You'll Need

### Required Files
1. ✅ **firstaid.pdf** - Your First Aid textbook PDF (any edition)
2. ✅ **exam.pdf** - Your medical exam PDF (NBME, USMLE, etc.)
3. ✅ **OpenAI API key** - Get from [platform.openai.com](https://platform.openai.com/api-keys)

### System Requirements
- Python 3.8 or higher
- Internet connection (for API calls)
- ~$0.50 in OpenAI credits per 50-question exam

---

## 🎯 What This Does

**Input:** NBME/USMLE exam PDF with 50 questions

**Output:** CSV file with enriched study prompts

**Example:**
```csv
Question Number,Prompt
1,"Professionally condense and explain how allosteric activators like AMP influence enzyme kinetics..."
2,"Professionally condense and explain AML presentation, pancytopenia, gingival hypertrophy..."
```

Each prompt is:
- ✅ Comprehensive and detailed
- ✅ Enriched with First Aid content
- ✅ Perfect for AI-assisted studying
- ✅ Maps 1-to-1 with questions

---

## 🛠️ Setup Steps (Detailed)

### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```

This installs:
- PyPDF2 (PDF reading)
- openai (API client)
- python-dotenv (config management)

### Step 2: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Add billing info at https://platform.openai.com/settings/organization/billing

### Step 3: Configure API Key

Create `.env` file:
```bash
echo 'OPENAI_API_KEY=sk-proj-your-actual-key-here' > .env
```

Or create manually:
```
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

### Step 4: Test Configuration
```bash
python3 test_setup.py
```

Should show all ✅ checks passing.

### Step 5: Test API Connection
```bash
python3 test_api.py
```

Should show successful API response.

### Step 6: Add PDFs

Place in this directory:
- `firstaid.pdf` - First Aid textbook
- Your exam PDF(s) - NBME, USMLE, etc.

### Step 7: Generate Prompts!

**Option A: Interactive (easiest)**
```bash
python3 run.py
```

**Option B: Command line**
```bash
python3 generate_study_prompts.py "NBME 30.pdf"
```

---

## 📖 Documentation

- **QUICKSTART.md** - 3-minute setup guide
- **README.md** - Full documentation
- **USAGE_EXAMPLES.md** - Examples and troubleshooting
- **PROJECT_SUMMARY.md** - Technical details

---

## ❓ Common Questions

### How much does it cost?
- ~$0.40-0.60 per 50-question exam (GPT-4o)
- ~$0.05-0.10 per exam (GPT-3.5, lower quality)

### How long does it take?
- 5-10 minutes per 50-question exam
- Progress shown in real-time

### What formats are supported?
- PDF with extractable text (OCR'd if scanned)
- Works best with NBME/USMLE style exams
- Should have 40-50 questions numbered

### Can I use my own textbook?
- Yes! Just name it `firstaid.pdf`
- Or edit `generate_study_prompts.py` to use different file

### What if I don't have First Aid?
- Script will still work but prompts will be less enriched
- Recommend getting any medical reference textbook PDF

---

## 🆘 Troubleshooting

### "API key not found"
```bash
# Check .env exists
ls -la .env

# Check contents (without showing key)
cat .env

# Recreate if needed
echo 'OPENAI_API_KEY=sk-your-key' > .env
```

### "No questions extracted"
Your PDF might not have extractable text. Test:
```bash
python3 -c "import PyPDF2; f=open('exam.pdf','rb'); print(PyPDF2.PdfReader(f).pages[0].extract_text()[:200])"
```

If nothing prints or garbled text, you need to OCR the PDF first.

### "firstaid.pdf not found"
```bash
# Check current directory
ls -la *.pdf

# Make sure it's named exactly "firstaid.pdf"
```

### API errors / Rate limits
- Check https://platform.openai.com/usage
- Verify billing is set up
- Try again in a few minutes

---

## 🎓 Usage Tips

1. **Start with one exam** to verify quality
2. **Review first 5 prompts** to ensure accuracy
3. **Use interactive mode** (`python3 run.py`) for ease
4. **Keep First Aid updated** for best results
5. **Organize outputs** in a separate folder

---

## 🚀 Ready to Go?

```bash
# Validate everything
python3 test_setup.py

# Test API
python3 test_api.py

# Run!
python3 run.py
```

**Questions?** Check the documentation files or the inline comments in the code.

**Good luck with your studies! 📚🎓**

---

## 📝 Quick Reference

| Task | Command |
|------|---------|
| Setup | `./setup.sh` or `pip3 install -r requirements.txt` |
| Test config | `python3 test_setup.py` |
| Test API | `python3 test_api.py` |
| Interactive run | `python3 run.py` |
| Direct run | `python3 generate_study_prompts.py "exam.pdf"` |
| Custom output | `python3 generate_study_prompts.py "exam.pdf" "output.csv"` |

---

## 🎯 Next Steps

Once you have your CSV:
1. Open in Excel/Google Sheets
2. Copy prompts to your study tool
3. Use with ChatGPT/Claude for detailed explanations
4. Create Anki cards
5. Build comprehensive study guides

**Happy studying!** 🎓✨
