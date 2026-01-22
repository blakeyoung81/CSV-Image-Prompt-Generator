# 📚 Medical Study Prompt Generator - File Index

**Quick Navigation for All Documentation & Scripts**

---

## 🚀 Getting Started (Read These First)

| File | Purpose | Time to Read |
|------|---------|--------------|
| **START_HERE.md** | Begin here! Quick setup guide | 2 min |
| **QUICKSTART.md** | Fastest path to running | 3 min |
| **test_setup.py** | Validate your configuration | Run it! |
| **test_api.py** | Test OpenAI API connection | Run it! |

**New user?** Start with `START_HERE.md` → Run `test_setup.py` → Run `test_api.py` → You're ready!

---

## 📖 Documentation (Learn the System)

| File | Purpose | When to Read |
|------|---------|--------------|
| **README.md** | Complete documentation | Need full details |
| **USAGE_EXAMPLES.md** | Examples & troubleshooting | Running into issues |
| **WORKFLOW.md** | Visual process flow | Want to understand flow |
| **PROJECT_SUMMARY.md** | Technical deep-dive | Developer reference |
| **INDEX.md** | This file - navigation | Finding specific info |

---

## 🔧 Scripts (Run These)

| File | Purpose | Usage |
|------|---------|-------|
| **run.py** | Interactive mode (easiest!) | `python3 run.py` |
| **generate_study_prompts.py** | Main engine | `python3 generate_study_prompts.py "exam.pdf"` |
| **test_setup.py** | Validate setup | `python3 test_setup.py` |
| **test_api.py** | Test API connection | `python3 test_api.py` |
| **setup.sh** | Auto-install dependencies | `./setup.sh` |

---

## 📦 Configuration Files

| File | Purpose | How to Create |
|------|---------|---------------|
| **requirements.txt** | Python dependencies | Already exists |
| **.env** | API key (you create) | `echo 'OPENAI_API_KEY=sk-...' > .env` |
| **.gitignore** | Git ignore rules | Already exists |

---

## 📄 Example & Reference Files

| File | Purpose |
|------|---------|
| **example_output.csv** | Sample output format |

---

## 📂 Files You Need to Add

| File | Description | Where to Get |
|------|-------------|--------------|
| **firstaid.pdf** | First Aid textbook PDF | Your copy |
| **exam.pdf** | Medical exam PDFs | NBME, USMLE, etc. |

---

## 🎯 Quick Task Reference

### "I want to set up for the first time"
1. Read: `START_HERE.md`
2. Run: `./setup.sh` or `pip3 install -r requirements.txt`
3. Create: `.env` file with API key
4. Add: `firstaid.pdf` and exam PDFs
5. Test: `python3 test_setup.py`
6. Test: `python3 test_api.py`

### "I want to generate prompts"
- **Easy way:** `python3 run.py`
- **Direct way:** `python3 generate_study_prompts.py "exam.pdf"`
- **Custom output:** `python3 generate_study_prompts.py "exam.pdf" "output.csv"`

### "I want to understand how it works"
1. Read: `README.md` (overview)
2. Read: `WORKFLOW.md` (visual flow)
3. Read: `PROJECT_SUMMARY.md` (technical details)

### "I'm having problems"
1. Run: `python3 test_setup.py` (check config)
2. Run: `python3 test_api.py` (check API)
3. Read: `USAGE_EXAMPLES.md` (troubleshooting section)

### "I want to see examples"
1. Read: `USAGE_EXAMPLES.md` (usage patterns)
2. Open: `example_output.csv` (sample output)
3. Check: `WORKFLOW.md` (console output examples)

### "I want to customize"
1. Read: `PROJECT_SUMMARY.md` (customization section)
2. Edit: `generate_study_prompts.py` (main script)
3. See: `README.md` (configuration options)

---

## 📊 File Sizes & Complexity

| Category | Files | Total Lines | Complexity |
|----------|-------|-------------|------------|
| **Core Scripts** | 3 files | ~600 lines | Medium |
| **Helper Scripts** | 3 files | ~200 lines | Simple |
| **Documentation** | 7 files | ~2000 lines | N/A |
| **Config** | 2 files | ~20 lines | Simple |

---

## 🎓 Reading Path by User Type

### 📘 First-Time User
```
START_HERE.md
    ↓
test_setup.py (run)
    ↓
test_api.py (run)
    ↓
run.py (use it!)
    ↓
USAGE_EXAMPLES.md (if issues)
```

### 📗 Regular User
```
run.py (daily use)
    ↓
USAGE_EXAMPLES.md (reference)
    ↓
QUICKSTART.md (refresher)
```

### 📕 Developer/Technical User
```
PROJECT_SUMMARY.md
    ↓
generate_study_prompts.py (read code)
    ↓
WORKFLOW.md
    ↓
Customize as needed
```

### 📙 Troubleshooter
```
test_setup.py (diagnose)
    ↓
test_api.py (diagnose)
    ↓
USAGE_EXAMPLES.md (solutions)
    ↓
README.md (reference)
```

---

## 🔍 Find Information Fast

### Setup & Installation
→ `START_HERE.md`, `QUICKSTART.md`, `setup.sh`

### API Configuration
→ `START_HERE.md`, `test_api.py`, `.env` creation

### Running the Tool
→ `run.py`, `USAGE_EXAMPLES.md`, `QUICKSTART.md`

### Troubleshooting
→ `USAGE_EXAMPLES.md`, `test_setup.py`, `test_api.py`

### Understanding the System
→ `WORKFLOW.md`, `PROJECT_SUMMARY.md`, `README.md`

### Customization
→ `PROJECT_SUMMARY.md`, `generate_study_prompts.py`

### Examples & Output
→ `USAGE_EXAMPLES.md`, `example_output.csv`

### Technical Details
→ `PROJECT_SUMMARY.md`, code comments in `.py` files

---

## 📝 Documentation Style Guide

| File | Style | Best For |
|------|-------|----------|
| **START_HERE.md** | Quick & actionable | Impatient users |
| **QUICKSTART.md** | Step-by-step | New users |
| **README.md** | Comprehensive | Reference |
| **USAGE_EXAMPLES.md** | Example-driven | Learning by doing |
| **WORKFLOW.md** | Visual diagrams | Visual learners |
| **PROJECT_SUMMARY.md** | Technical prose | Developers |

---

## 💡 Pro Tips

1. **Bookmark this file** for quick navigation
2. **Start with START_HERE.md** - it's designed to get you running FAST
3. **Run test scripts first** - catch issues early
4. **Keep USAGE_EXAMPLES.md handy** - great for troubleshooting
5. **Read code comments** - scripts are well-documented inline

---

## 🔄 File Dependencies

```
.env (you create)
    ↓
firstaid.pdf (you add)
    ↓
exam.pdf (you add)
    ↓
requirements.txt → pip install
    ↓
generate_study_prompts.py (core logic)
    ↓
run.py (optional wrapper)
    ↓
output.csv (generated)
```

---

## 📈 Version Info

- **Version:** 1.0
- **Last Updated:** 2026-01
- **Python Required:** 3.8+
- **Dependencies:** See `requirements.txt`

---

## ✨ Quick Command Reference

```bash
# Setup
./setup.sh
pip3 install -r requirements.txt
echo 'OPENAI_API_KEY=sk-...' > .env

# Test
python3 test_setup.py
python3 test_api.py

# Run
python3 run.py
python3 generate_study_prompts.py "exam.pdf"
python3 generate_study_prompts.py "exam.pdf" "output.csv"

# Batch
for f in *.pdf; do python3 generate_study_prompts.py "$f"; done
```

---

## 🎯 You Are Here

```
CSV Generator/
│
├── 📍 YOU ARE HERE: INDEX.md
│
├── 🚀 Start: START_HERE.md
├── ⚡ Quick: QUICKSTART.md
├── 📖 Full: README.md
├── 🔄 Flow: WORKFLOW.md
├── 🛠️ Tech: PROJECT_SUMMARY.md
├── 💡 Examples: USAGE_EXAMPLES.md
│
├── ▶️ Run: run.py
├── 🔧 Main: generate_study_prompts.py
├── ✅ Test: test_setup.py, test_api.py
│
└── 📦 Config: requirements.txt, .env (create)
```

---

## 🎓 Happy Studying!

**Ready?** Go to `START_HERE.md` and begin! 🚀

**Questions?** Check `README.md` for comprehensive docs.

**Issues?** Run `test_setup.py` and `test_api.py` first.

**Want examples?** See `USAGE_EXAMPLES.md`.

Good luck with your medical studies! 📚✨
