# 🧠 NLP Report Generation System

A GUI-based intelligent report generator that extracts, summarizes, translates, and converts document content to speech. It supports PDFs, DOCX, and image files, and provides outputs in text, audio, PDF, and DOCX formats.

---

## 🚀 Features

- 📤 **Uploads**: Images (JPG/PNG), PDFs, DOCX  
- 🔍 **Text Extraction**: OCR + File Parsing  
- 🧠 **NLP**: Summarization using BART  
- 🌍 **Translation**: Kannada & Hindi  
- 🔊 **Text-to-Speech**: `pyttsx3` (offline)  
- 📤 **Export Options**: PDF, DOCX, TXT  
- 🖥️ **GUI**: Modern design using CustomTkinter  

---

## 💻 Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nlp-report-generator.git
cd nlp-report-generator
```

### 2. Python Environment

Ensure Python 3.7.4 must be installed.

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

> ✅ This project has been tested with Python 3.7.4 for compatibility.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing or incomplete, manually install:

```bash
pip install transformers torch pytesseract pdfplumber python-docx Pillow tk
pip install customtkinter spacy nltk deep-translator pyttsx3 fpdf PyMuPDF
```

---

### 4. Install External Tools

#### ✅ Tesseract OCR

Used for image-based text extraction.

- Download: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Windows Installation Path:  
  `C:\Program Files\Tesseract-OCR\tesseract.exe`

In your code, set the path:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### 🗣 Text-to-Speech Support

`pyttsx3` works offline.

For Windows voice support:

```bash
pip install pywin32
```

---

## 🔧 Running the App

### 1. Start Main Launcher (Home Page):

```bash
python main.py
```

### 2. To Directly Run Report Generator:

```bash
python notebook.py
```

---

## 📝 Functional Summary

- `main.py`: Launches the home screen GUI
- `notebook.py`: Handles
  - File selection
  - Text extraction (OCR or parsing)
  - Summarization (Hugging Face BART)
  - Translation (deep-translator)
  - Text-to-speech (pyttsx3)
  - Export (PDF, DOCX)

---

## 📌 Notes

- You must manually set the Tesseract path in Windows
- Requires `DejaVuSans.ttf` for multi-language PDF export
- Summarizer will auto-download models from HuggingFace on first run

---

## 🆘 Troubleshooting

| Issue                     | Solution                                                  |
|--------------------------|-----------------------------------------------------------|
| Tesseract Not Found      | Check file path and update in code                        |
| Translation Fails        | Ensure active internet connection                         |
| No Voice Output (Windows)| Install `pywin32` and verify speakers are working         |
| GUI Crashes on Large Files| Optimize OCR input or reduce file size                   |
