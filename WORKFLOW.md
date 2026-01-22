# 🔄 Complete Workflow Guide

Visual guide to using the Medical Study Prompt Generator.

---

## 📊 Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    SETUP (One Time)                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  1. Install Dependencies                                    │
│     $ pip3 install -r requirements.txt                      │
│     → PyPDF2, openai, python-dotenv                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  2. Get OpenAI API Key                                      │
│     → Visit https://platform.openai.com/api-keys           │
│     → Create new key (starts with sk-)                     │
│     → Add billing info                                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  3. Create .env File                                        │
│     $ echo 'OPENAI_API_KEY=sk-your-key' > .env            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  4. Add PDFs                                                │
│     → firstaid.pdf (reference textbook)                    │
│     → exam.pdf (NBME/USMLE questions)                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  5. Validate Setup                                          │
│     $ python3 test_setup.py                                │
│     → Check all ✅ marks                                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  6. Test API                                                │
│     $ python3 test_api.py                                  │
│     → Verify connection works                              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    READY TO USE! ✅                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔁 Regular Usage Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  START: New Exam to Process                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
                  ┌─────────┴─────────┐
                  │                   │
         ┌────────▼────────┐   ┌─────▼──────────┐
         │ OPTION A:       │   │ OPTION B:      │
         │ Interactive     │   │ Direct Command │
         │ $ python3 run.py│   │ $ python3 gen..│
         └────────┬────────┘   └─────┬──────────┘
                  │                   │
                  └─────────┬─────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Load First Aid PDF                                │
│  → Extract all text (~2-3 MB)                              │
│  → Store as knowledge base in memory                       │
│  ✓ Loaded X characters from First Aid                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Extract Questions from Exam PDF                   │
│  → Parse PDF into individual questions                     │
│  → Identify question numbers (1-50)                        │
│  → Extract full content for each                           │
│  ✓ Extracted 50 questions                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Process Each Question (Loop 1-50)                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────┴───────────────────┐
        │   FOR EACH QUESTION (Q1 to Q50)       │
        └───────────────────┬───────────────────┘
                            ↓
        ┌─────────────────────────────────────┐
        │  3a. Identify Key Concepts          │
        │  → AI Call #1 (GPT-4o)             │
        │  → Input: Question text             │
        │  → Output: 3-7 concept keywords     │
        │  ✓ Concepts: allosteric; enzyme... │
        └──────────────────┬──────────────────┘
                            ↓
        ┌─────────────────────────────────────┐
        │  3b. Find Relevant First Aid        │
        │  → Keyword matching in FA text      │
        │  → Extract relevant paragraphs      │
        │  → Build context (up to 3000 chars) │
        └──────────────────┬──────────────────┘
                            ↓
        ┌─────────────────────────────────────┐
        │  3c. Generate Enriched Prompt       │
        │  → AI Call #2 (GPT-4o)             │
        │  → Input: Question + Concepts + FA  │
        │  → Output: Enriched study prompt    │
        │  ✓ Prompt generated                │
        └──────────────────┬──────────────────┘
                            ↓
        ┌─────────────────────────────────────┐
        │  3d. Save to Results                │
        │  → Store Q# + Prompt                │
        │  → Continue to next question        │
        └──────────────────┬──────────────────┘
                            ↓
        ┌───────────────────┴──────────────────┐
        │   Repeat for all 50 questions        │
        │   (5-10 minutes total)               │
        └───────────────────┬──────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Export to CSV                                      │
│  → Sort by question number                                  │
│  → Write header: "Question Number,Prompt"                  │
│  → Write all 50 rows                                        │
│  ✓ Saved to: exam_study_prompts.csv                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    COMPLETE! 🎉                             │
│  → CSV file ready                                           │
│  → 50 enriched study prompts                               │
│  → Ready for studying                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 File Organization

```
CSV Generator/
│
├── 🔧 CORE SCRIPTS
│   ├── generate_study_prompts.py  ← Main engine
│   ├── run.py                      ← Interactive CLI
│   ├── test_setup.py              ← Validation tool
│   ├── test_api.py                ← API test
│   └── setup.sh                   ← Auto setup
│
├── 📚 DOCUMENTATION
│   ├── START_HERE.md              ← Begin here!
│   ├── QUICKSTART.md              ← 3-min guide
│   ├── README.md                  ← Full docs
│   ├── USAGE_EXAMPLES.md          ← Examples
│   ├── PROJECT_SUMMARY.md         ← Technical overview
│   └── WORKFLOW.md                ← This file
│
├── 📦 DEPENDENCIES
│   └── requirements.txt           ← Python packages
│
├── 📄 EXAMPLE
│   └── example_output.csv         ← Sample output
│
├── 🔐 CONFIG (create these)
│   └── .env                       ← API key (git-ignored)
│
└── 📖 INPUT FILES (add these)
    ├── firstaid.pdf               ← Reference textbook
    └── *.pdf                      ← Exam PDFs
```

---

## 🎬 Screen Output Examples

### During Setup Validation
```
============================================================
Medical Study Prompt Generator - Setup Validation
============================================================

✓ Python 3.11.5
✓ PyPDF2 installed
✓ openai installed
✓ python-dotenv installed
✓ OpenAI API key configured (sk-proj...Qx7A)
✓ firstaid.pdf found (145.2 MB)
✓ Found 2 exam PDF(s):
   - NBME 30 A Part 2-ocr.pdf (2.3 MB)
   - NBME 29.pdf (2.1 MB)

============================================================
✅ All checks passed! Ready to generate study prompts.
============================================================
```

### During API Test
```
============================================================
OpenAI API Connection Test
============================================================

✓ API Key found: sk-proj...Qx7A

Testing API connection...
✓ API Response: API test successful

Token Usage:
  - Prompt: 25
  - Completion: 4
  - Total: 29

============================================================
✅ API connection successful!
============================================================
```

### During Processing
```
============================================================
Medical Question to Study Prompt Generator
============================================================

Loading First Aid reference from: firstaid.pdf
✓ Loaded 2543891 characters from First Aid

Extracting questions from: NBME 30 A Part 2-ocr.pdf
✓ Extracted 50 questions

[1/50] Processing Question 1...
  → Identifying key concepts...
  → Concepts: Allosteric activators; enzyme kinetics; glycogen phosphorylase; Km; Vmax; fasting metabolism
  → Generating enriched prompt...
  ✓ Complete

[2/50] Processing Question 2...
  → Identifying key concepts...
  → Concepts: Acute myelogenous leukemia; AML; pancytopenia; gingival hypertrophy; blasts
  → Generating enriched prompt...
  ✓ Complete

...

[50/50] Processing Question 50...
  → Identifying key concepts...
  → Concepts: Radial head subluxation; nursemaid elbow; pediatric injury
  → Generating enriched prompt...
  ✓ Complete

============================================================
Writing results to: NBME 30 A Part 2-ocr_study_prompts.csv
✓ Successfully generated 50 study prompts!
✓ Output saved to: NBME 30 A Part 2-ocr_study_prompts.csv
============================================================
```

---

## 💡 Decision Tree: Which Script to Use?

```
START: I want to generate study prompts
    ↓
    ├─→ Need to check setup first?
    │   YES → python3 test_setup.py
    │   NO → Continue
    ↓
    ├─→ Need to test API?
    │   YES → python3 test_api.py
    │   NO → Continue
    ↓
    ├─→ How do I want to run it?
    │
    ├─→ EASY/INTERACTIVE
    │   → python3 run.py
    │   → Script shows PDFs, you choose
    │   → Auto-names output
    │
    ├─→ QUICK/AUTOMATED
    │   → python3 generate_study_prompts.py "exam.pdf"
    │   → Direct, no interaction
    │   → Auto-names output
    │
    └─→ CUSTOM OUTPUT NAME
        → python3 generate_study_prompts.py "exam.pdf" "my_output.csv"
        → Full control
```

---

## 🔍 Troubleshooting Decision Tree

```
Problem occurred?
    ↓
    ├─→ "No questions found"
    │   → Check: PDF has extractable text?
    │   → Test: Copy text from PDF manually
    │   → Fix: OCR the PDF if needed
    │
    ├─→ "API key not found"
    │   → Check: .env file exists? (ls -la .env)
    │   → Check: Key in .env? (cat .env)
    │   → Fix: echo 'OPENAI_API_KEY=sk-...' > .env
    │
    ├─→ "firstaid.pdf not found"
    │   → Check: File in directory? (ls *.pdf)
    │   → Check: Named exactly "firstaid.pdf"?
    │   → Fix: Rename or move file
    │
    ├─→ "API error / rate limit"
    │   → Check: Billing set up?
    │   → Check: Credits available?
    │   → Fix: Wait 60 seconds, try again
    │
    ├─→ "Poor quality prompts"
    │   → Check: First Aid loaded? (see console output)
    │   → Check: Using GPT-4? (not GPT-3.5)
    │   → Fix: Verify FA PDF has text, use GPT-4
    │
    └─→ "Script too slow"
        → Expected: 5-10 minutes for 50 questions
        → Normal: ~6-12 seconds per question
        → Tip: Use GPT-3.5 for speed (lower quality)
```

---

## 📊 Performance Metrics

### Time per Exam (50 questions)
- **Total:** 5-10 minutes
- **Per Question:** 6-12 seconds
- **Breakdown:**
  - PDF loading: 5-10 seconds
  - Question extraction: 10-20 seconds
  - Per question processing: 5-10 seconds
  - CSV writing: <1 second

### API Costs per Exam
| Model | Input Tokens | Output Tokens | Cost |
|-------|-------------|---------------|------|
| GPT-4o | ~150,000 | ~25,000 | $0.40-0.60 |
| GPT-3.5 | ~150,000 | ~25,000 | $0.05-0.10 |

### Token Breakdown per Question
- **Concept ID (Call #1):** ~1500 input, ~50 output
- **Prompt Gen (Call #2):** ~2000 input, ~200 output
- **First Aid context:** ~3000 tokens max per question

---

## 🎯 Success Criteria Checklist

Before running:
- [ ] Python 3.8+ installed
- [ ] `pip3 install -r requirements.txt` completed
- [ ] `.env` file created with valid API key
- [ ] `firstaid.pdf` in directory
- [ ] Exam PDF ready
- [ ] `python3 test_setup.py` shows all ✅
- [ ] `python3 test_api.py` succeeds

After running:
- [ ] CSV file created
- [ ] 50 rows in CSV (or expected count)
- [ ] Each prompt starts with "Professionally condense and explain"
- [ ] Prompts are detailed and comprehensive
- [ ] Question numbers match exam

---

## 🔄 Batch Processing Workflow

For multiple exams:

```bash
# Method 1: Process sequentially
python3 generate_study_prompts.py "NBME 29.pdf"
python3 generate_study_prompts.py "NBME 30.pdf"
python3 generate_study_prompts.py "NBME 31.pdf"

# Method 2: Batch script
for exam in NBME*.pdf; do
    echo "Processing $exam..."
    python3 generate_study_prompts.py "$exam"
done

# Method 3: Custom naming
python3 generate_study_prompts.py "NBME 29.pdf" "outputs/nbme29.csv"
python3 generate_study_prompts.py "NBME 30.pdf" "outputs/nbme30.csv"
```

---

## 📈 Quality Assurance

After generating prompts:

1. **Spot Check First 5 Prompts**
   - Open CSV
   - Read Q1-Q5 prompts
   - Verify completeness and accuracy

2. **Check Question Coverage**
   - Confirm 50 rows (or expected count)
   - Verify sequential numbering (1-50)
   - No missing questions

3. **Validate Enrichment**
   - Prompts mention First Aid concepts?
   - More detailed than just question content?
   - Include pathophysiology, mechanisms, etc.?

4. **Test with AI**
   - Copy a prompt to ChatGPT/Claude
   - Ask for detailed explanation
   - Verify it produces useful study material

---

## 🎓 Post-Processing Ideas

Once you have your CSV:

### Option 1: Anki Cards
```python
# Convert CSV to Anki-compatible format
import csv
with open('study_prompts.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Q{row['Question Number']}\t{row['Prompt']}")
```

### Option 2: Study Guide
- Import CSV to Google Sheets
- Group by topic/system
- Add your own notes
- Export as PDF

### Option 3: AI Study Session
```python
# Automated study helper
import csv, openai

with open('prompts.csv', 'r') as f:
    for row in csv.DictReader(f):
        prompt = row['Prompt']
        # Send to AI for detailed explanation
        # Save responses
```

### Option 4: Quiz Generator
- Use prompts to create practice questions
- Feed to AI: "Based on this prompt, create 3 practice questions"
- Build custom quiz bank

---

## ✅ You're All Set!

This workflow covers everything from setup to post-processing.

**Ready to start?** → See `START_HERE.md`

**Questions?** → Check `README.md` or `USAGE_EXAMPLES.md`

**Technical details?** → See `PROJECT_SUMMARY.md`

Happy studying! 📚✨
