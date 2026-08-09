"""
M&A Target Screener - Section Extractor
Downloads the latest 10-K for any ticker and extracts
Business, Risk Factors, and MD&A sections for LLM analysis.
"""

import re
from pathlib import Path
from sec_edgar_downloader import Downloader
from bs4 import BeautifulSoup

# ====================== CONFIG ======================
# Replace these with your own information before running
COMPANY_NAME = "Your Name or Company Name"
EMAIL = "your.email@example.com"
# ====================================================


def download_latest_10k(ticker: str) -> Path:
    output_dir = Path("data/temp_filings")
    output_dir.mkdir(parents=True, exist_ok=True)

    dl = Downloader(COMPANY_NAME, EMAIL, output_dir)
    print(f"Downloading latest 10-K for {ticker.upper()}...")
    dl.get("10-K", ticker.upper(), limit=1)
    print("Download complete.")
    return output_dir


def find_latest_submission(ticker: str, base_dir: Path) -> Path:
    ticker = ticker.upper()
    search_path = base_dir / "sec-edgar-filings" / ticker / "10-K"

    if not search_path.exists():
        raise FileNotFoundError(f"No 10-K filings found for {ticker}")

    folders = sorted([f for f in search_path.iterdir() if f.is_dir()], reverse=True)
    if not folders:
        raise FileNotFoundError("No filing folders found")

    submission_file = folders[0] / "full-submission.txt"
    if not submission_file.exists():
        raise FileNotFoundError("full-submission.txt not found")

    return submission_file


def clean_text(text: str) -> str:
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def extract_section(text: str, start_patterns: list, end_patterns: list, max_chars: int = 12000) -> str:
    start_idx = None
    for pattern in start_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            start_idx = match.start()
            break

    if start_idx is None:
        return "Section not found."

    end_idx = len(text)
    for pattern in end_patterns:
        match = re.search(pattern, text[start_idx + 200:], re.IGNORECASE)
        if match:
            end_idx = start_idx + 200 + match.start()
            break

    section = clean_text(text[start_idx:end_idx])
    if len(section) > max_chars:
        section = section[:max_chars] + "\n\n[... Section truncated for length ...]"
    return section


def process_ticker(ticker: str):
    ticker = ticker.upper().strip()
    print(f"\n{'='*60}")
    print(f"Processing: {ticker}")
    print(f"{'='*60}")

    base_dir = download_latest_10k(ticker)
    submission_file = find_latest_submission(ticker, base_dir)

    with open(submission_file, "r", encoding="utf-8", errors="ignore") as f:
        raw = f.read()

    soup = BeautifulSoup(raw, "lxml")
    text = soup.get_text(separator="\n")

    business = extract_section(
        text,
        start_patterns=[r"Item\s*1[\.\s]+Business", r"ITEM\s*1[\.\s]+BUSINESS"],
        end_patterns=[r"Item\s*1A[\.\s]+Risk", r"ITEM\s*1A"],
        max_chars=10000
    )

    risk_factors = extract_section(
        text,
        start_patterns=[r"Item\s*1A[\.\s]+Risk\s*Factors", r"ITEM\s*1A[\.\s]+RISK"],
        end_patterns=[r"Item\s*1B", r"Item\s*2[\.\s]+Properties", r"ITEM\s*2"],
        max_chars=14000
    )

    mda = extract_section(
        text,
        start_patterns=[r"Item\s*7[\.\s]+Management.?s\s+Discussion", r"ITEM\s*7[\.\s]+MANAGEMENT"],
        end_patterns=[r"Item\s*7A", r"Item\s*8[\.\s]+Financial", r"ITEM\s*8"],
        max_chars=11000
    )

    output_dir = Path("outputs/ready_for_llm")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{ticker}_for_llm.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Company Ticker: {ticker}\n\n")
        f.write("=" * 80 + "\nBUSINESS SECTION\n" + "=" * 80 + "\n\n")
        f.write(business)
        f.write("\n\n" + "=" * 80 + "\nRISK FACTORS\n" + "=" * 80 + "\n\n")
        f.write(risk_factors)
        f.write("\n\n" + "=" * 80 + "\nMD&A\n" + "=" * 80 + "\n\n")
        f.write(mda)

    print(f"\n✅ Success! File saved to: {output_file}")
    print("→ Copy the content of this file and paste it into Google AI Studio.")


if __name__ == "__main__":
    ticker = input("\nEnter stock ticker (e.g. NVDA, CRM, SNOW): ").strip()
    if ticker:
        process_ticker(ticker)
    else:
        print("No ticker entered.")