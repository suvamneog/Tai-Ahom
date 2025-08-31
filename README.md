# Tai-Ahom Manuscripts Digitization & Translation

## Overview
This project is part of our **B.Tech CSE Final Year** work.  
We aim to digitize, preserve, and translate endangered Tai-Ahom manuscripts using:

- **OCR (Optical Character Recognition)** → Convert scanned manuscripts into digital text.  
- **Machine Translation (MT)** → Translate from Ahom → Assamese → English.  
- **Web Portal** → Make manuscripts accessible online.  

---

## Repository Structure

tai-ahom/
├─ data/
│  ├─ raw/        # Extracted manuscript scans (PNG)
│  ├─ clean/      # Preprocessed images (denoised, binarized, deskewed)
│  ├─ gt/         # Ground-truth transcriptions (for OCR training)
├─ docs/
│  ├─ references/ # Extracted text pages from PDFs
│  ├─ metadata.json
│  └─ progress_reports/
├─ models/
│  ├─ ocr/        # OCR models (Tesseract, TrOCR)
│  └─ mt/         # Translation models (mBART, NLLB)
├─ notebooks/     # Jupyter/Colab notebooks for experiments
├─ portal/        # Web application (React + Node.js)
├─ extract_pdf.py # Script to extract text/images/metadata from PDFs
└─ preprocess_images.py # Script to preprocess manuscript images

---

## Features (Planned)
- Data Collection & Cleanup → Extract, preprocess, and annotate manuscripts.  
- OCR → Fine-tune Tesseract/TrOCR for Ahom script recognition.  
- Machine Translation → Build parallel corpus and fine-tune MT models.  
- Web Portal → Upload manuscripts → OCR → Translate → Save results.  
- Evaluation → Measure OCR (CER) and MT (BLEU/chrF) scores.  

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/tai-ahom.git
cd tai-ahom

2. Install Dependencies

pip install -r requirements.txt

3. Extract Data from PDF

python3 extract_pdf.py

4. Preprocess Images

python3 preprocess_images.py

5. Prepare Training Data

python3 prepare_tesseract_training.py


⸻

Team Roles
	•	Data Team → Collect manuscripts, clean images, annotate ground truth.
	•	OCR Team → Train OCR models (Tesseract/TrOCR).
	•	MT Team → Build translation dataset and train MT models.
	•	Web Team → Build portal (React + Node.js).
	•	QA/Docs Team → Track metrics (CER, BLEU) & prepare reports.

⸻

Project Tracking

We maintain a Google Sheet Tracker with tasks, owners, deadlines, and evidence links.
(Add link here when ready)

⸻

Reports
	•	Progress Report PDF (docs/TaiAhom_Progress_Report.pdf)

⸻

Current Status
	•	Repository structured
	•	Extracted text, images, and metadata from manuscripts
	•	Preprocessed manuscript scans
	•	OCR training pipeline ready (awaiting ground truth transcription)

⸻

Next Steps
	•	Manual transcription for ground truth (data/gt/).
	•	Fine-tune Tesseract OCR on Ahom script.
	•	Build translation corpus (Ahom → Assamese → English).
	•	Setup web portal for user interaction.
	•	Weekly progress documentation.

⸻

License

This project is for academic research & preservation purposes only.

---
