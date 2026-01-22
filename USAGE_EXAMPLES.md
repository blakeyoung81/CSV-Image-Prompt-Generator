# Usage Examples

## Example 1: Basic Usage

```bash
python3 generate_study_prompts.py "NBME 30 A Part 2-ocr.pdf"
```

**Output:** `NBME 30 A Part 2-ocr_study_prompts.csv`

---

## Example 2: Custom Output Name

```bash
python3 generate_study_prompts.py "NBME 30.pdf" "nbme30_prompts.csv"
```

**Output:** `nbme30_prompts.csv`

---

## Example 3: Interactive Mode

```bash
python3 run.py
```

**What happens:**
1. Shows list of available exam PDFs
2. Let you select which one to process
3. Automatically names the output file
4. Shows progress for each question

---

## Example 4: Batch Processing Multiple Exams

```bash
# Process multiple exams one after another
python3 generate_study_prompts.py "NBME 29.pdf"
python3 generate_study_prompts.py "NBME 30.pdf"
python3 generate_study_prompts.py "NBME 31.pdf"
```

Or create a batch script:

```bash
#!/bin/bash
for exam in NBME*.pdf; do
    python3 generate_study_prompts.py "$exam"
done
```

---

## Example 5: Test Your Setup

```bash
python3 test_setup.py
```

**Sample output:**
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

---

## Expected Output Format

Your CSV will look like this:

```csv
Question Number,Prompt
1,"Professionally condense and explain the material relevant to how allosteric activators, such as AMP, influence enzyme kinetics (specifically Km and Vmax) in the context of skeletal muscle glycogen phosphorylase..."
2,"Professionally condense and explain the clinical presentation, laboratory findings (pancytopenia and blasts), and unique physical markers like gingival hypertrophy associated with Acute Myelogenous Leukemia (AML)..."
3,"Professionally condense and explain the expected motor, social, and verbal/cognitive developmental milestones for a 3-month-old infant..."
```

---

## Console Output During Processing

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
  → Concepts: Allosteric activators; enzyme kinetics; glycogen phosphorylase...
  → Generating enriched prompt...
  ✓ Complete

[2/50] Processing Question 2...
  → Identifying key concepts...
  → Concepts: Acute myelogenous leukemia; pancytopenia; gingival hypertrophy...
  → Generating enriched prompt...
  ✓ Complete

...

[50/50] Processing Question 50...
  → Identifying key concepts...
  → Concepts: Radial head subluxation; nursemaid elbow; pediatric injury...
  → Generating enriched prompt...
  ✓ Complete

============================================================
Writing results to: NBME 30 A Part 2-ocr_study_prompts.csv
✓ Successfully generated 50 study prompts!
✓ Output saved to: NBME 30 A Part 2-ocr_study_prompts.csv
============================================================
```

---

## Using the Output with AI Study Tools

Once you have your CSV, you can:

1. **Copy-paste into ChatGPT/Claude:**
   ```
   "Here's my study prompt: [paste prompt from CSV]
   Please explain this concept in detail with examples."
   ```

2. **Create Anki flashcards:**
   - Use the prompts as the back of cards
   - Front: "Question X" or key concept
   - Back: The enriched explanation

3. **Study guide compilation:**
   - Open CSV in Excel/Google Sheets
   - Sort by topic areas
   - Group related concepts
   - Export as study guide

4. **Batch AI processing:**
   ```python
   import csv
   import openai
   
   with open('study_prompts.csv', 'r') as f:
       reader = csv.DictReader(f)
       for row in reader:
           prompt = row['Prompt']
           # Use prompt with AI for detailed explanations
   ```

---

## Troubleshooting Examples

### Problem: Questions not extracting correctly

**Solution:** Check PDF text extraction
```bash
python3 -c "
import PyPDF2
with open('exam.pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    print(reader.pages[0].extract_text()[:500])
"
```

If you see garbled text or nothing, your PDF needs OCR.

### Problem: Prompts are too generic

**Possible causes:**
1. First Aid PDF not loading properly
2. Question extraction failed
3. API rate limits

**Solution:** Check logs for errors and verify First Aid PDF.

### Problem: API costs too high

**Solutions:**
- Switch from GPT-4 to GPT-3.5-turbo (edit `generate_study_prompts.py`)
- Reduce `max_tokens` parameter
- Process fewer questions at a time

---

## Advanced Customization

### Change AI Model

Edit `generate_study_prompts.py`:

```python
# Line ~67 and ~94
model="gpt-4o"  # Change to "gpt-3.5-turbo" for cost savings
```

### Adjust Prompt Style

Edit the prompt template in `generate_enriched_prompt()` method to customize:
- Level of detail
- Focus areas (pathophysiology vs clinical)
- Format (bullet points vs paragraph)

### Process Different Question Counts

The script auto-detects question count. Works with:
- 40-question blocks
- 50-question blocks
- Custom ranges (modify extraction logic)

---

## Tips for Best Results

1. **Use high-quality OCR PDFs**
   - Text should be selectable
   - Clean formatting helps extraction

2. **Keep First Aid updated**
   - Use latest edition
   - Ensure PDF has selectable text

3. **Review first few outputs**
   - Verify quality before processing all exams
   - Adjust parameters if needed

4. **Save API costs**
   - Process multiple exams in one session
   - Use GPT-3.5 for initial draft, GPT-4 for final version

5. **Organize outputs**
   ```bash
   mkdir outputs
   mv *_study_prompts.csv outputs/
   ```
