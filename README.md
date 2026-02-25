# 📄 AI Contract Review Bot

### AI Engineer Hiring Task — Contract & Document Review Automation

An AI-powered legal document analysis system that extracts key clauses, identifies risks, and generates structured summaries from contracts (PDF or raw text).

Built as part of an AI Engineer Fresher Hiring Assignment.

---

## 🚀 Project Overview

Businesses regularly deal with contracts such as NDAs, service agreements, vendor contracts, and employment letters. Manually reviewing these documents is slow, expensive, and error-prone.

This application automates contract analysis using a Large Language Model (LLM) to:

* Extract key contract details
* Identify legal risk patterns
* Highlight risky clauses
* Generate a plain-English summary
* Present results in a clean, structured UI

The system demonstrates real-world LLM integration for legal document intelligence.

---

## 🏗 Architecture

**Frontend:** Streamlit
**Backend:** Flask API
**LLM Provider:** Groq (LLaMA 3 model)
**PDF Parsing:** pdfplumber

```
User (Streamlit UI)
        ↓
Upload PDF / Paste Text
        ↓
Flask Backend (/analyze)
        ↓
Groq LLM (Clause Extraction + Risk Analysis)
        ↓
Structured JSON Response
        ↓
Streamlit UI (Formatted Report + Risk Flags)
```

---

## ✨ Features

### 📂 Document Input

* Upload `.pdf` contract files
* Or paste raw contract text
* Automatic text extraction from PDF

### 🧠 AI-Powered Clause Extraction

Extracts:

* Parties involved
* Contract duration
* Payment terms
* Termination clauses
* Renewal terms
* Confidentiality clauses
* Liability clauses

### ⚠ Risk Flag System

Identifies and highlights:

* Auto-renewal traps
* Liability risks
* Missing exit clauses

Risk flags are clearly labeled and color-coded.

### 📝 Plain English Summary

Generates a concise summary understandable by non-lawyers.

### 📊 Structured Output

Results are displayed in organized sections — not as a single block of text.

---

## 🛠 Tech Stack

| Layer             | Technology         |
| ----------------- | ------------------ |
| AI Brain          | Groq LLM (LLaMA 3) |
| Backend           | Python + Flask     |
| Frontend          | Streamlit          |
| PDF Parsing       | pdfplumber         |
| API Communication | requests           |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sahithuppala05/contract-review-bot.git
cd contract-review-bot
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the backend folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get your API key from:
[https://console.groq.com](https://console.groq.com)

---

### 5️⃣ Run Backend (Flask)

```bash
cd backend
python app.py
```

Backend runs at:

```
http://127.0.0.1:10000
```

---

### 6️⃣ Run Frontend (Streamlit)

Open a new terminal:

```bash
cd frontend
streamlit run streamlit_app.py
```

App runs at:

```
http://localhost:8501
```

---

## 🧪 How to Test

You can test using:

* NDA templates
* Service agreements
* Employment offer letters
* Vendor contracts

Upload a PDF → Click Analyze → View structured report with risk flags.

---

## 📊 Evaluation Alignment

This project demonstrates:

* ✅ LLM API integration (real AI analysis)
* ✅ Structured JSON extraction
* ✅ Risk detection logic
* ✅ Clean frontend-backend separation
* ✅ Organized and readable output
* ✅ Clear setup documentation

---

## 📌 Key Design Decisions

* Used temperature = 0 for deterministic extraction.
* Forced structured JSON output from LLM.
* Separated backend from frontend for production scalability.
* Implemented error handling for invalid JSON from model.
* Designed risk flags to simulate real legal review workflow.

---

## 🔮 Future Improvements

* Clause-by-clause highlighting
* Confidence scoring per extraction
* Export as PDF report
* Multi-document comparison
* Clause deviation detection against standard templates
* Role-based dashboard (legal team vs founders)

---
