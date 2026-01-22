# Project Summary: Medical Study Prompt Generator

## 🎯 What This Does

Transforms medical exam PDFs (NBME, USMLE practice exams) into enriched study prompts using AI and First Aid as a knowledge base.

**Input:** Exam PDF with 50 questions  
**Output:** CSV with 50 detailed, enriched study prompts (1-to-1 mapping)

---

## 📁 Project Structure

```
CSV Generator/
├── generate_study_prompts.py  # Main script (core logic)
├── run.py                      # Interactive CLI wrapper
├── test_setup.py              # Setup validation tool
├── setup.sh                   # Automated setup script
│
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
│
├── README.md                 # Full documentation
├── QUICKSTART.md             # 3-minute setup guide
├── USAGE_EXAMPLES.md         # Detailed usage examples
├── PROJECT_SUMMARY.md        # This file
│
├── example_output.csv        # Sample output format
│
├── firstaid.pdf              # [USER ADDS] First Aid reference
└── *.pdf                     # [USER ADDS] Exam PDFs
```

---

## 🚀 Quick Start

```bash
# 1. Setup
./setup.sh

# 2. Configure
echo 'OPENAI_API_KEY=sk-your-key' > .env

# 3. Add files
# - Place firstaid.pdf here
# - Place exam PDFs here

# 4. Test
python3 test_setup.py

# 5. Run
python3 run.py
```

---

## 🔧 Core Components

### 1. `generate_study_prompts.py` (Main Engine)

**Classes:**
- `MedicalPromptGenerator` - Main orchestrator

**Key Methods:**
- `_load_firstaid()` - Loads First Aid PDF as knowledge base
- `extract_questions_from_pdf()` - Extracts 50 questions from exam PDF
- `identify_key_concepts()` - Uses AI to identify medical concepts
- `_find_relevant_firstaid_section()` - Matches concepts to First Aid content
- `generate_enriched_prompt()` - Creates final enriched prompt
- `process_exam()` - Main pipeline orchestrator

**AI Integration:**
- Uses OpenAI GPT-4o model
- 2 API calls per question:
  1. Concept identification
  2. Enriched prompt generation
- Temperature: 0.3-0.4 for consistency

---

### 2. `run.py` (User-Friendly Interface)

- Interactive PDF selection
- Auto-detects exam PDFs
- Validates configuration
- Shows progress
- Handles errors gracefully

---

### 3. `test_setup.py` (Validation)

Checks:
- ✅ Python version (3.8+)
- ✅ Dependencies installed
- ✅ API key configured
- ✅ First Aid PDF present
- ✅ Exam PDFs available

---

## 🔄 Processing Pipeline

```
1. LOAD FIRST AID
   ↓
   Extract text from firstaid.pdf
   Store as knowledge base (2-3 MB text)

2. EXTRACT QUESTIONS
   ↓
   Parse exam PDF into 50 individual questions
   Each with number + full content

3. FOR EACH QUESTION:
   ↓
   a) IDENTIFY CONCEPTS (AI Call #1)
      "Analyze this question → key concepts"
      Output: 3-7 concept keywords
   ↓
   b) FIND RELEVANT FIRST AID SECTIONS
      Keyword matching in First Aid text
      Extract relevant paragraphs
   ↓
   c) GENERATE ENRICHED PROMPT (AI Call #2)
      Input: Question + Concepts + First Aid excerpt
      Output: Comprehensive study prompt
   ↓
   d) SAVE TO RESULTS

4. EXPORT TO CSV
   ↓
   Question Number, Prompt
   1, "Professionally condense..."
   2, "Professionally condense..."
   ...
```

---

## 📊 Output Format

### CSV Structure
```csv
Question Number,Prompt
1,"[Enriched prompt for Q1]"
2,"[Enriched prompt for Q2]"
...
50,"[Enriched prompt for Q50]"
```

### Prompt Structure
Each prompt:
- Starts with "Professionally condense and explain..."
- Covers ALL key concepts in the question
- Integrates First Aid material
- Includes pathophysiology, clinical presentation, diagnosis, mechanisms
- 2-4 sentences typically
- Highly detailed but concise

### Example Prompt
```
"Professionally condense and explain the material relevant to how 
allosteric activators, such as AMP, influence enzyme kinetics 
(specifically Km and Vmax) in the context of skeletal muscle glycogen 
phosphorylase, including the biochemical definition of Km as substrate 
concentration at half-maximal velocity, the role of conformational 
changes in increasing substrate affinity, and the physiological 
significance of AMP as a fasting signal that upregulates glycogenolysis 
when cellular energy status is depleted."
```

---

## 💰 Cost Analysis

### Per 50-Question Exam

**Using GPT-4o:**
- 100 API calls (2 per question)
- Input tokens: ~150,000
- Output tokens: ~25,000
- **Cost: ~$0.40-0.60 per exam**

**Using GPT-3.5-turbo:**
- Same call count
- **Cost: ~$0.05-0.10 per exam**
- Lower quality prompts

**Processing Time:**
- 5-10 minutes per exam
- ~6-12 seconds per question
- Parallel processing not used (to respect rate limits)

---

## 🛠️ Technical Details

### Dependencies
```
PyPDF2==3.0.1      # PDF text extraction
openai==1.12.0     # OpenAI API client
python-dotenv==1.0.1  # Environment variables
```

### Python Requirements
- Python 3.8 or higher
- Works on macOS, Linux, Windows

### API Requirements
- OpenAI API key
- GPT-4 access (recommended)
- GPT-3.5 works but lower quality

### PDF Requirements
- **Input Exam PDF:**
  - Must have extractable text (OCR'd if scanned)
  - Questions numbered 1-50
  - Standard NBME/USMLE format preferred

- **First Aid PDF:**
  - Any edition (latest recommended)
  - Must have extractable text
  - ~100-200 MB typical

---

## 🎓 Use Cases

1. **USMLE Step 1/2 Prep**
   - Process NBME self-assessments
   - Process UWorld blocks
   - Create comprehensive review materials

2. **Medical School Exams**
   - Past exam review
   - Topic-based question banks
   - Board review courses

3. **Anki Card Creation**
   - Use prompts as card content
   - Organize by systems/topics
   - High-yield concept reinforcement

4. **AI-Assisted Studying**
   - Feed prompts to ChatGPT/Claude
   - Get detailed explanations
   - Generate practice questions

---

## 🔐 Security Notes

- API key stored in `.env` (git-ignored)
- No data sent to external servers except OpenAI
- PDFs processed locally
- No persistent storage of API responses

---

## 🐛 Known Limitations

1. **PDF Parsing**
   - Requires well-formatted PDFs
   - Scanned images need OCR first
   - Complex layouts may confuse parser

2. **Question Count**
   - Optimized for 50-question blocks
   - Works with 40+ questions
   - May need adjustment for other formats

3. **First Aid Matching**
   - Simple keyword matching
   - May miss nuanced connections
   - Not a semantic search (yet)

4. **API Costs**
   - Can add up with many exams
   - No caching between runs
   - Each run is independent

---

## 🚀 Future Enhancements

### Potential Improvements

1. **Better PDF Parsing**
   - OCR integration (Tesseract)
   - Table/image extraction
   - Multi-column support

2. **Enhanced First Aid Integration**
   - Semantic search (embeddings)
   - Cross-referencing
   - Multiple textbook support

3. **Caching**
   - Cache concept identification
   - Reuse First Aid sections
   - Resume interrupted runs

4. **Batch Processing**
   - Parallel API calls
   - Queue management
   - Progress persistence

5. **Output Formats**
   - Anki deck export
   - Markdown notes
   - JSON structured data

6. **Quality Control**
   - Prompt validation
   - Completeness checking
   - User feedback loop

---

## 📝 Customization Guide

### Change AI Model
Edit `generate_study_prompts.py`:
```python
# Line ~67 and ~94
model="gpt-4o"  # → "gpt-3.5-turbo" or "gpt-4-turbo"
```

### Adjust Detail Level
Edit prompt template in `generate_enriched_prompt()`:
```python
prompt = f"""...
Generate a SINGLE, comprehensive study prompt that:
1. [Customize requirements here]
...
"""
```

### Modify Temperature
```python
temperature=0.4  # Higher = more creative, Lower = more focused
```

### Change Max Tokens
```python
max_tokens=500  # Increase for longer prompts
```

---

## 📚 Documentation Files

- **README.md** - Comprehensive documentation
- **QUICKSTART.md** - 3-minute getting started
- **USAGE_EXAMPLES.md** - Detailed examples and troubleshooting
- **PROJECT_SUMMARY.md** - This file (technical overview)

---

## 🤝 Support

### Common Issues

1. **No questions extracted**
   → Check PDF has selectable text

2. **API errors**
   → Verify API key, check rate limits

3. **Poor quality prompts**
   → Ensure First Aid PDF is loaded
   → Try GPT-4 instead of 3.5

4. **Slow processing**
   → Normal! 5-10 min per exam
   → Consider GPT-3.5 for speed

---

## ✅ Success Checklist

Before first run:
- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with OpenAI API key
- [ ] `firstaid.pdf` in project directory
- [ ] Exam PDF ready
- [ ] Run `python3 test_setup.py` - all checks pass

---

## 🎉 Ready to Use!

```bash
# Test everything
python3 test_setup.py

# Run interactively
python3 run.py

# Or direct
python3 generate_study_prompts.py "your-exam.pdf"
```

**Enjoy your enriched study materials! 📚🎓**
