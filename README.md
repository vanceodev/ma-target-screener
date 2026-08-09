# NLP-Driven M&A Target Screening & Deal Thesis Generator

## Overview
This project creates a practical pipeline that downloads SEC 10-K filings, extracts key sections (Business, Risk Factors, and MD&A), and prepares clean text for LLM-powered generation of structured Private Equity-style M&A investment theses.

It is designed to demonstrate technical and analytical skills relevant to Investment Banking, Private Equity, and Hedge Fund roles.

## Disclaimer
The investment theses generated using this tool are produced by an AI model for **educational and research purposes only**. They do **not** constitute investment advice, financial recommendations, or professional analysis. Always perform your own due diligence.

## Features
- Automated download of the latest 10-K filing for any U.S. public company
- Extraction of Business, Risk Factors, and MD&A sections
- Clean text output ready for use with Google AI Studio / Gemini or other LLMs
- Simple and extensible structure

## Project Structure
```text
ma-target-screener/
├── analyze_ticker.py      # Main script
├── requirements.txt
├── .gitignore
├── README.md
├── data/                  # Temporary SEC filings (ignored by git)
└── outputs/
    └── ready_for_llm/     # Clean text files for LLM input