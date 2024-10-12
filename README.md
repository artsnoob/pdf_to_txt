# PDF to Text Converter

This Python script converts PDF files to text using Optical Character Recognition (OCR). It allows users to extract text from entire PDF documents or specific page ranges.

## Features

- Convert entire PDF documents to text
- Extract text from a single page
- Extract text from a range of pages
- Logging of the conversion process
- Error handling and informative error messages

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Tesseract OCR engine
- Poppler (for pdf2image)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/artsnoob/pdf_to_txt.git
   cd pdf_to_txt
   ```

2. Install the required Python packages:
   ```
   pip install pytesseract pdf2image
   ```

3. Install Tesseract OCR:
   - On Ubuntu:
     ```
     sudo apt-get install tesseract-ocr
     ```
   - On macOS:
     ```
     brew install tesseract
     ```
   - On Windows, download and install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

4. Install Poppler:
   - On Ubuntu:
     ```
     sudo apt-get install poppler-utils
     ```
   - On macOS:
     ```
     brew install poppler
     ```
   - On Windows, download from [poppler releases](http://blog.alivate.com.au/poppler-windows/) and add to PATH

## Usage

Run the script:

```
python convert.py
```

Follow the prompts to:
1. Enter the path to your PDF file
2. Choose extraction options:
   - Extract entire document
   - Extract a single page
   - Extract a range of pages

The script will create a text file with the same name as the input PDF in the same directory.

## Troubleshooting

If you encounter issues related to Poppler:
1. Ensure Poppler is installed correctly
2. Add Poppler to your system PATH:
   - On macOS, add the following line to your `~/.zshrc` or `~/.bash_profile`:
     ```
     export PATH="/usr/local/opt/poppler/bin:$PATH"
     ```
   - On Windows, add the Poppler `bin` directory to your system PATH
