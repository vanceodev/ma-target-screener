# NLP-Driven M&A Target Screening & Deal Thesis Generator

## Overview
This project builds a practical pipeline that downloads SEC 10-K filings, extracts key sections (Business, Risk Factors, and MD&A), and prepares clean text for LLM-powered generation of structured Private Equity-style M&A investment theses.

It is designed to demonstrate technical and analytical skills relevant to Investment Banking, Private Equity, and Hedge Fund roles.

## Disclaimer
The investment theses generated using this tool are produced by an AI model for **educational and research purposes only**. They do **not** constitute investment advice, financial recommendations, or professional analysis. Always perform your own due diligence.

## Features
- Automated download of the latest 10-K filing for any U.S. public company
- Extraction of Business, Risk Factors, and MD&A sections
- Clean text output ready for use with ChatGPT, Claude, Gemini, or other LLMs
- Example theses included

## Example Output
Sample M&A theses generated using this pipeline are available in the [`examples/`](examples/) folder:
- [Apple (AAPL)](examples/AAPL_MA_Thesis.md)
- [Microsoft (MSFT)](examples/MSFT_MA_Thesis.md)

## Project Structure
```text
ma-target-screener/
├── analyze_ticker.py          # Main extraction script
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
├── examples/                  # Sample M&A theses
│   ├── AAPL_MA_Thesis.md
│   └── MSFT_MA_Thesis.md
├── data/                      # Temporary SEC filings (ignored by git)
└── outputs/
    └── ready_for_llm/         # Clean text files for LLM input
