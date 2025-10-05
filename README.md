# PDF Form NER Project

This project demonstrates generating PDF forms, creating datasets for Named Entity Recognition (NER), training a SpaCy model, and testing it. The project contains three main Python scripts:  

**1️⃣ PdfGeneration.py** – Generates synthetic PDF forms with fake data for training and testing the NER model. Features: multiple fields like `Agent Name`, `Agent Email`, `Nice Class`, etc.; supports randomized or fixed field order; draws a logo at the top; saves PDF and JSON data. Usage: `python PdfGeneration.py`  

**2️⃣ DeepLearningScript.py** – Trains a SpaCy NER model using generated JSON data. Features: reads JSON files with labeled data; creates training examples; trains SpaCy NER with multiple epochs; saves model to `model_forms`. Usage: `python DeepLearningScript.py`. Notes: you can continue training an existing model with `spacy.load()`, adjust `epochs` and `drop` for performance.  

**3️⃣ TestingScript.py** – Tests the trained NER model on new PDF or text data. Features: reads JSON or text files; extracts entities with SpaCy; prints recognized entities and labels. Usage: `python TestingScript.py`  

**Project Structure:**  
├─ data/ # Generated PDFs and JSON data
├─ model_forms/ # Saved SpaCy NER model
├─ PdfGeneration.py
├─ DeepLearningScript.py
├─ TestingScript.py
└─ README.md

**Dependencies:** Python 3.10+, Faker, ReportLab, Pillow, spaCy. Install via: `pip install -r requirements.txt`  
