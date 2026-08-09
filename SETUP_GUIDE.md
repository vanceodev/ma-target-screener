# Setup & Usage Guide

This guide explains how to set up and use the **M&A Target Screener** project.

Repository: [https://github.com/vanceodev/ma-target-screener](https://github.com/vanceodev/ma-target-screener)

---

## 1. Clone the Repository

```bash
git clone https://github.com/vanceodev/ma-target-screener.git
cd ma-target-screener
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Virtual Environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

If you run into a permissions/execution policy error, run this first:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Your Identity (Required by SEC)

Open `analyze_ticker.py` and update these two lines:

```python
COMPANY_NAME = "Your Name"
EMAIL = "your.email@example.com"
```

The SEC requires a real name and email address when downloading filings.

## 6. Run the Script

```bash
python analyze_ticker.py
```

When prompted, enter any U.S. stock ticker (ex: `NVDA`, `SNOW`, `CRM`, `AAPL`).

## 7. Generate the M&A Thesis

After the script finishes, open the `outputs` folder. Upload the `.txt` file into an LLM of your choosing.

**Recommended prompt:**

```text
You are a senior Private Equity associate specializing in technology M&A.

Your task is to write a clear, structured, and insightful M&A investment thesis based on the company's latest 10-K sections (Business Description, Risk Factors, and MD&A).

Follow this exact structure:

# [Company Name] ([Ticker]) – M&A / Strategic Attractiveness Thesis

### 1. Business Quality & Moat
### 2. Growth Drivers
### 3. Key Risks
### 4. Capital Intensity & Cash Flow Characteristics
### 5. Overall M&A Attractiveness: [High / Medium-High / Medium / Medium-Low / Low]

Tone: Professional, concise, and analytical. Write like a real PE investment memo. Avoid fluff.
```
