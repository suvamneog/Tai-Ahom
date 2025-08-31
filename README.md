# Tai-Ahom Manuscripts Digitization & Translation

## 📋 Overview

This project is part of our **B.Tech CSE Final Year** work.  
We aim to digitize, preserve, and translate endangered Tai-Ahom manuscripts using:

- OCR (Optical Character Recognition) → Convert scanned manuscripts into digital text
- Machine Translation (MT) → Translate from Ahom → Assamese → English
- Web Portal → Make manuscripts accessible online

---

## 📁 Repository Structure

```
tai-ahom/
├── data/
│   ├── raw/                    # Extracted manuscript scans (PNG)
│   ├── clean/                  # Preprocessed images (denoised, binarized, deskewed)
│   └── gt/                     # Ground-truth transcriptions (for OCR training)
├── docs/
│   ├── references/             # Extracted text pages from PDFs
│   ├── metadata.json           # Manuscript metadata and annotations
│   └── progress_reports/       # Weekly/monthly progress documentation
├── models/
│   ├── ocr/                    # OCR models (Tesseract, TrOCR)
│   └── mt/                     # Translation models (mBART, NLLB)
├── notebooks/                  # Jupyter/Colab notebooks for experiments
├── portal/                     # Web application (React + Node.js)
├── extract_pdf.py              # Script to extract text/images/metadata from PDFs
├── preprocess_images.py        # Script to preprocess manuscript images
└── prepare_tesseract_training.py # Script to prepare training data
```

---

##  Features (Planned)

- Data Collection & Cleanup → Extract, preprocess, and annotate manuscripts
- OCR → Fine-tune Tesseract/TrOCR for Ahom script recognition
- Machine Translation → Build parallel corpus and fine-tune MT models
- Web Portal → Upload manuscripts → OCR → Translate → Save results
- Evaluation → Measure OCR (CER) and MT (BLEU/chrF) scores

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 16+ (for web portal)
- Git
- (Optional) CUDA-capable GPU for model training

### 1. Clone the Repository

```bash
git clone https://github.com/suvamneog/tai-ahom.git
cd tai-ahom
```

### 2. Install Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Extract Data from PDF

```bash
python3 extract_pdf.py
```

### 4. Preprocess Images

```bash
python3 preprocess_images.py
```

### 5. Prepare Training Data

```bash
python3 prepare_tesseract_training.py
```

### 6. Set Up Web Portal (Optional)

```bash
cd portal
npm install
npm run dev
```

---

## 👥 Team Roles

| Team | Responsibilities |
|------|------------------|
|  Data Team | Collect manuscripts, clean images, annotate ground truth |
|  OCR Team | Train OCR models (Tesseract/TrOCR) |
|  MT Team | Build translation dataset and train MT models |
|  Web Team | Build portal (React + Node.js) |

---

##  Project Tracking

We maintain a Google Sheet Tracker with tasks, owners, deadlines, and evidence links.  

---

##  Current Status

###  Completed
- [x] Repository structured
- [x] Extracted text, images, and metadata from manuscripts
- [x] Preprocessed manuscript scans
- [x] OCR training pipeline ready (awaiting ground truth transcription)

### 🔄 In Progress
- [ ] Manual transcription for ground truth (`data/gt/`)
- [ ] Fine-tune Tesseract OCR on Ahom script
- [ ] Build translation corpus (Ahom → Assamese → English)
- [ ] Setup web portal for user interaction
- [ ] Weekly progress documentation

---

##  Next Steps

1. Manual transcription for ground truth (`data/gt/`)
2. Fine-tune Tesseract OCR on Ahom script
3. Build translation corpus (Ahom → Assamese → English)
4. Setup web portal for user interaction
5. Weekly progress documentation

---

## Model Evaluation

### OCR Metrics
- CER (Character Error Rate) → Primary metric for OCR accuracy
- WER (Word Error Rate) → Secondary metric for word-level accuracy

### Translation Metrics
- BLEU Score → Primary metric for translation quality
- chrF Score → Character-level F-score for translation evaluation

---

##  Technology Stack

- OCR: Tesseract, TrOCR (Transformer-based OCR)
- Machine Translation: mBART, NLLB (No Language Left Behind)
- Web Portal: React.js + Node.js + Express
- Image Processing: OpenCV, PIL
- Machine Learning: PyTorch, Transformers

---

##  License

This project is for **academic research & preservation purposes only**.

### Usage Rights
-  Academic research and educational purposes
-  Non-commercial cultural preservation efforts
-  Citation in academic publications (with proper attribution)
-  Commercial use without explicit permission
-  Redistribution without source attribution

---

##  Acknowledgments

- Cultural Consultants → Tai-Ahom community elders and scholars
- Technical Mentors → Faculty advisors and industry experts
- Data Contributors → Museums, libraries, and private collectors
- Open Source Community → Tesseract, Hugging Face, and related projects

---

Preserving the past, building the future.
