# 📄 PDF Generator Guide

Professional PDF generator that creates beautiful documents from numbered images.

---

## 🎯 What It Does

Takes a folder of numbered images (like screenshots of questions) and creates a professional PDF with:
- Beautiful title page with custom title
- 2 images per page in clean layout
- Professional headers and footers
- Page numbers
- Clean, organized format

---

## 🚀 Quick Start

### GUI Mode (Easiest)

```bash
python3 pdf_generator_gui.py
```

**Then:**
1. Enter your PDF title (default: "NBME 30")
2. Add optional additional text
3. Select your image folder
4. Choose output location
5. Click "Generate PDF"

### Command Line Mode

```bash
python3 generate_pdf_from_images.py <image_folder> -o output.pdf -t "NBME 30"
```

---

## 📁 Image Folder Setup

### Required Format

Your images should be numbered:
```
my_images/
├── 1.png
├── 2.jpg
├── 3.png
├── 4.jpeg
...
├── 50.png
```

### Supported Formats
- ✅ PNG (.png)
- ✅ JPEG (.jpg, .jpeg)
- ✅ GIF (.gif)
- ✅ BMP (.bmp)
- ✅ TIFF (.tiff)

### Naming Conventions

The script auto-detects images by number:
- `1.png`, `2.png`, `3.png` ✅
- `question1.jpg`, `question2.jpg` ✅
- `q_1.png`, `q_2.png` ✅
- `img001.png`, `img002.png` ✅

**Numbers are extracted and sorted automatically!**

---

## 🎨 PDF Output Format

### Title Page (Page 1)
```
┌─────────────────────────────────────┐
│                                     │
│         [Purple Background]         │
│                                     │
│            NBME 30                  │
│       (Your Custom Title)           │
│                                     │
│      Practice Questions             │
│    (Your Additional Text)           │
│                                     │
│        January 22, 2026             │
│                                     │
│   Professional Study Material       │
│                                     │
└─────────────────────────────────────┘
```

### Content Pages (Page 2+)
```
┌─────────────────────────────────────┐
│ NBME 30          Page 2 of 26       │
│─────────────────────────────────────│
│                                     │
│     [Image 1 - Question 1]          │
│                                     │
│         Question 1                  │
│                                     │
│─────────────────────────────────────│
│                                     │
│     [Image 2 - Question 2]          │
│                                     │
│         Question 2                  │
│                                     │
│─────────────────────────────────────│
│                2                    │
└─────────────────────────────────────┘
```

---

## 💻 Command Line Usage

### Basic Usage

```bash
python3 generate_pdf_from_images.py images/
```
Creates `output.pdf` with default title "NBME 30"

### Custom Title

```bash
python3 generate_pdf_from_images.py images/ -t "NBME 31"
```

### Custom Output Name

```bash
python3 generate_pdf_from_images.py images/ -o my_exam.pdf
```

### Additional Text

```bash
python3 generate_pdf_from_images.py images/ -t "NBME 30" -a "Practice Questions"
```

### Full Example

```bash
python3 generate_pdf_from_images.py \
    ~/Desktop/nbme_images \
    -o ~/Documents/NBME_30.pdf \
    -t "NBME 30 Form A" \
    -a "Self-Assessment Practice"
```

### A4 Paper Size

```bash
python3 generate_pdf_from_images.py images/ --a4
```
(Default is Letter size)

---

## 🎨 GUI Mode Features

### Interface Sections

**1. PDF Settings**
- Title field (default: "NBME 30")
- Additional text field (optional)

**2. Files**
- Image folder browser
- Output PDF location

**3. Progress**
- Real-time status updates
- Shows each page being created

**4. Generate Button**
- One-click PDF creation
- Shows success message with location

### Auto-Features

✅ **Auto Output Naming:** Based on title  
✅ **Smart Folder Detection:** Remembers last folder  
✅ **Progress Updates:** See what's happening  
✅ **Error Handling:** Clear error messages  

---

## 📊 Examples

### Example 1: NBME Exam

```bash
# Folder structure:
nbme30/
├── 1.png
├── 2.png
...
└── 50.png

# Command:
python3 generate_pdf_from_images.py nbme30/ \
    -o "NBME_30_Complete.pdf" \
    -t "NBME 30" \
    -a "Comprehensive Basic Science Self-Assessment"

# Result:
NBME_30_Complete.pdf (26 pages total)
- 1 title page
- 25 pages with 2 questions each
```

### Example 2: Custom Question Bank

```bash
# Folder structure:
my_questions/
├── q1.jpg
├── q2.jpg
...
└── q25.jpg

# Command:
python3 generate_pdf_from_images.py my_questions/ \
    -o "Custom_Questions.pdf" \
    -t "Cardiology Review" \
    -a "High-Yield Practice Questions"

# Result:
Custom_Questions.pdf (14 pages total)
- 1 title page
- 13 pages with 2 questions each (last page has 1)
```

### Example 3: Study Material

```bash
# Using GUI:
python3 pdf_generator_gui.py

# Then fill in:
Title: "Step 1 Review"
Additional Text: "System-Based Questions"
Image Folder: /Users/me/Desktop/step1_images
Output: /Users/me/Documents/Step1_Review.pdf

# Click "Generate PDF"
```

---

## 🎯 Use Cases

### 1. Creating Study PDFs from Screenshots
- Screenshot each question
- Number them sequentially
- Generate professional PDF
- Print or share digitally

### 2. Organizing Practice Questions
- Compile questions from various sources
- Create unified PDF
- Easy to review and annotate

### 3. Creating Flashcard PDFs
- Images of flashcards
- 2 per page for printing
- Professional format

### 4. Converting Image Banks to PDF
- Medical image banks
- Radiology cases
- Pathology slides

---

## ⚙️ Technical Details

### Image Processing
- **Automatic scaling:** Images fit optimally on page
- **Aspect ratio:** Preserved automatically
- **Quality:** High-resolution maintained
- **Centering:** Images centered on page

### Page Layout
- **Margins:** 0.75 inches all around
- **Header height:** 0.6 inches
- **Footer height:** 0.6 inches
- **Image spacing:** Optimal padding

### PDF Properties
- **Page size:** Letter (8.5" × 11") or A4
- **Orientation:** Portrait
- **Color space:** RGB
- **Compression:** Automatic

---

## 🐛 Troubleshooting

### "No images found in folder!"

**Causes:**
- Empty folder
- Images not numbered
- Wrong image format

**Solution:**
- Check folder has images
- Ensure images have numbers in filename
- Use supported formats (PNG, JPEG, etc.)

### "Could not add image"

**Causes:**
- Corrupted image file
- Unsupported format
- File permission issues

**Solution:**
- Check image opens in Preview/Photos
- Convert to PNG or JPEG
- Check file permissions

### Images look pixelated

**Solution:**
- Use higher resolution source images
- Minimum 1024×768 recommended
- 1920×1080 or higher for best quality

### PDF file size too large

**Solution:**
- Compress images before adding
- Use JPEG instead of PNG
- Reduce image resolution

---

## 💡 Pro Tips

### 1. Image Quality
- Use PNG for screenshots (better quality)
- Use JPEG for photos (smaller size)
- Don't scale up low-res images

### 2. Naming
- Use consistent numbering: 01, 02, 03...
- Pad with zeros for proper sorting
- Keep filenames simple

### 3. Organization
- One folder per exam/set
- Name folders clearly
- Keep source images organized

### 4. Batch Processing
- Process multiple sets in sequence
- Use scripts for automation
- Keep templates consistent

### 5. Printing
- Letter size is standard in US
- A4 is standard internationally
- Set printer to "Actual Size" not "Fit to Page"

---

## 📝 Command Reference

### All Options

```bash
python3 generate_pdf_from_images.py --help

Usage: generate_pdf_from_images.py [-h] [-o OUTPUT] [-t TITLE] 
                                    [-a ADDITIONAL_TEXT] [--letter] [--a4]
                                    image_folder

Arguments:
  image_folder          Folder containing numbered images

Options:
  -h, --help           Show help message
  -o, --output         Output PDF filename (default: output.pdf)
  -t, --title          PDF title (default: NBME 30)
  -a, --additional-text Additional text for title page
  --letter             Use Letter size (default)
  --a4                 Use A4 size
```

---

## 🎨 Customization

### Changing Colors

Edit `generate_pdf_from_images.py`:

```python
# Title page background (line ~95)
c.setFillColor(colors.HexColor('#667eea'))  # Purple

# Change to:
c.setFillColor(colors.HexColor('#3b82f6'))  # Blue
```

### Changing Layout

Edit spacing constants:

```python
# Line ~14
self.margin = 0.75 * inch  # Change margins

# Line ~150-160
content_height = ...  # Adjust image sizes
```

### Adding Watermarks

Add after `_add_footer`:

```python
c.setFont("Helvetica", 40)
c.setFillColorRGB(0.9, 0.9, 0.9, alpha=0.3)
c.saveState()
c.translate(self.width/2, self.height/2)
c.rotate(45)
c.drawCentredString(0, 0, "DRAFT")
c.restoreState()
```

---

## 🚀 Integration with Other Tools

### With Study Prompt Generator

```bash
# 1. Generate study prompts
python3 generate_study_prompts.py exam.pdf

# 2. Screenshot each prompt
# (use any screenshot tool)

# 3. Create PDF
python3 generate_pdf_from_images.py screenshots/ -t "Study Guide"
```

### With Anki

```bash
# 1. Create PDF
python3 generate_pdf_from_images.py images/

# 2. Import PDF pages as images in Anki
# 3. Use with image occlusion add-on
```

---

## 📚 More Help

- **Main Documentation:** See `README.md`
- **Web Interface:** See `GUI_GUIDE.md`
- **General Help:** See `INDEX.md`

---

## ✅ Summary

**The PDF Generator makes it easy to:**
- ✅ Create professional PDFs from images
- ✅ 2 images per page layout
- ✅ Beautiful title page
- ✅ Custom titles and text
- ✅ Command line or GUI
- ✅ High-quality output

**Perfect for creating study materials!** 📚✨
