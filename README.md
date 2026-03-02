# ZoneBot 🏗️🗺️

ZoneBot is an AI-powered tool designed for construction companies to streamline the extraction of detailed zone data from architectural plans and documents.

## Project Overview
Construction projects often involve complex plans with numerous zones and specifications. ZoneBot automates the process of parsing these documents, identifying zones, and extracting relevant data, saving time and reducing errors.

## Features
- **PDF Parsing**: Extract text and metadata from architectural plans.
- **Data Extraction**: Identify and categorize zone data (e.g., area, usage, materials).
- **AI-Powered Analysis**: Leverage LLMs for intelligent data interpretation.
- **Reporting**: Generate structured reports from extracted data.

## Getting Started
1.  Clone the repository.
2.  **Install System Dependencies:**
    -   **Tesseract OCR**: Required for text extraction.
        -   Mac: `brew install tesseract`
        -   Linux: `sudo apt-get install tesseract-ocr`
        -   Windows: Download installer from UB-Mannheim/tesseract.
    -   **Poppler**: Required for PDF processing.
        -   Mac: `brew install poppler`
        -   Linux: `sudo apt-get install poppler-utils`
        -   Windows: Download binary from poppler website and add to PATH.
3.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  Set up your environment variables: `cp .env.example .env` and fill in your API keys.
5.  **Run the application**:
    ```bash
    python src/main.py path/to/your/plan.pdf --output processed_plan.png
    ```

## Project Structure
- `src/`: Core application logic.
  - `loader.py`: Handles image/PDF loading.
  - `preprocessor.py`: Image enhancement (binarization, denoising).
  - `detector.py`: Logic for finding zones/rooms.
  - `ocr.py`: Text extraction using Tesseract.
  - `main.py`: CLI entry point.
- `tests/`: Unit tests.
- `docs/`: Project documentation.
- `data/`: Sample data and exported reports.
