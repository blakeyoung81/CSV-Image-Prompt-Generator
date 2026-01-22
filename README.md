# Medical Question Study Prompt Generator

Automatically generates enriched study prompts from medical exam PDFs (like NBME, USMLE practice exams) using AI and First Aid as a reference textbook.

## Features

- 📄 Reads PDF exam files with 50 questions
- 🤖 Uses GPT-4 to analyze each question
- 📚 Enriches prompts with First Aid textbook content
- 📊 Outputs clean CSV with question number and detailed study prompt
- 🎯 Creates comprehensive, professionally formatted study materials

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file in this directory:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

Get your API key from: https://platform.openai.com/api-keys

### 3. Add First Aid PDF

Place your `firstaid.pdf` file in this directory. This will be used as the knowledge base to enrich the study prompts.

## Usage

### 🎨 GUI Mode (Easiest - Recommended!)

Launch the user-friendly graphical interface:

```bash
# Option 1: Double-click or run the launcher
./launch_gui.sh

# Option 2: Run directly with Python
python3 gui_app.py
```

**GUI Features:**
- 🔑 **Easy API Key Setup** - Popup dialog if no key is configured
- 📝 **Customizable Input Description** - Default: "An NBME exam of 50 questions..."
- 🔢 **Flexible Question Count** - Default: 50 (or set to 'auto' to detect)
- 📁 **File Browser** - Easy PDF selection with auto-detection
- 📊 **Live Progress** - Real-time status updates and progress bar
- ✨ **Auto-Detection** - Automatically finds PDFs in current directory

### 💻 Command Line Mode

#### Basic Usage

```bash
python generate_study_prompts.py "NBME 30 A Part 2-ocr.pdf"
```

This will:
1. Extract all 50 questions from the PDF
2. Identify key concepts in each question
3. Generate enriched study prompts using AI + First Aid
4. Save to `NBME 30 A Part 2-ocr_study_prompts.csv`

#### Specify Output File

```bash
python generate_study_prompts.py "NBME 30 A Part 2-ocr.pdf" my_output.csv
```

#### Interactive Mode

```bash
python3 run.py
```

## Output Format

The generated CSV has two columns:

```csv
Question Number,Prompt
1,"Professionally condense and explain the material relevant to how allosteric activators, such as AMP, influence enzyme kinetics..."
2,"Professionally condense and explain the clinical presentation, laboratory findings (pancytopenia and blasts), and unique physical markers..."
```

Each prompt is:
- ✅ Comprehensive and detailed
- ✅ Enriched with First Aid content
- ✅ Professionally formatted
- ✅ Covers pathophysiology, clinical findings, diagnosis, and mechanisms
- ✅ Ready to use for AI-assisted studying

## How It Works

1. **PDF Extraction**: Reads both the exam PDF and First Aid PDF
2. **Question Parsing**: Intelligently splits the exam into individual questions
3. **Concept Identification**: AI analyzes each question to identify key medical concepts
4. **First Aid Integration**: Finds relevant sections in First Aid matching the concepts
5. **Prompt Generation**: Creates enriched, comprehensive study prompts combining question content and First Aid material
6. **CSV Export**: Saves results in a clean, 1-to-1 mapping with question numbers

## Requirements

- Python 3.8+
- OpenAI API key (GPT-4 access)
- First Aid PDF (`firstaid.pdf`)
- Exam PDF with medical questions

## Cost Estimate

Using GPT-4o:
- ~$0.30-0.50 per 50-question exam
- Depends on question length and API pricing

## Troubleshooting

**"No questions found"**
- Check that your PDF has extractable text (OCR processed)
- Verify questions are numbered 1-50

**"OPENAI_API_KEY not found"**
- Make sure `.env` file exists with your API key
- Check the key starts with `sk-`

**"firstaid.pdf not found"**
- Place the First Aid PDF in the same folder as the script
- Ensure it's named exactly `firstaid.pdf`

## Example Output

```csv
Question Number,Prompt
1,"Professionally condense and explain the material relevant to how allosteric activators, such as AMP, influence enzyme kinetics (specifically Km and Vmax) in the context of skeletal muscle glycogen phosphorylase, including the physiological significance of AMP as a fasting signal and its role in upregulating glycogenolysis through conformational changes at the enzyme's active site."
```

## License

MIT License - Feel free to use and modify!
