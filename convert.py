import os
import pytesseract
from pdf2image import convert_from_path
import logging
import sys

logging.basicConfig(level=logging.INFO)

def pdf_to_txt(pdf_path, start_page=None, end_page=None):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_path = os.path.join(os.path.dirname(pdf_path), f"{base_name}.txt")
    
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path)
        
        # Adjust page range
        if start_page is not None:
            start_page = max(1, min(start_page, len(images))) - 1
        else:
            start_page = 0
        
        if end_page is not None:
            end_page = min(end_page, len(images))
        else:
            end_page = len(images)
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for i, image in enumerate(images[start_page:end_page], start=start_page+1):
                # Perform OCR on each image
                text = pytesseract.image_to_string(image)
                if text.strip():
                    txt_file.write(text)
                    logging.info(f"Extracted text from page {i}")
                else:
                    logging.warning(f"No text extracted from page {i}")
        
        if os.path.getsize(txt_path) == 0:
            logging.warning(f"The output file {txt_path} is empty. The PDF might not contain readable text.")
        else:
            logging.info(f"Converted {pdf_path} to {txt_path}")
    except Exception as e:
        logging.error(f"An error occurred while processing {pdf_path}: {str(e)}")
        if "poppler" in str(e).lower():
            logging.error("Poppler might not be installed or not in PATH. Please install Poppler and ensure it's in your system PATH.")
            logging.error("On macOS, you can install Poppler using Homebrew: brew install poppler")
            logging.error("Then add the following line to your ~/.zshrc or ~/.bash_profile:")
            logging.error('export PATH="/usr/local/opt/poppler/bin:$PATH"')
        sys.exit(1)

def convert_pdf(input_file, start_page=None, end_page=None):
    if not os.path.isfile(input_file) or not input_file.lower().endswith('.pdf'):
        print(f"Error: {input_file} is not a valid PDF file.")
        return

    pdf_to_txt(input_file, start_page, end_page)

def get_page_range():
    while True:
        choice = input("Choose an option:\n1. Extract entire document\n2. Extract a single page\n3. Extract a range of pages\nEnter your choice (1/2/3): ")
        if choice == '1':
            return None, None
        elif choice == '2':
            page = int(input("Enter the page number to extract: "))
            return page, page
        elif choice == '3':
            start = int(input("Enter the start page: "))
            end = int(input("Enter the end page: "))
            return start, end
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    input_file = input("Enter the input PDF file path: ")
    start_page, end_page = get_page_range()
    convert_pdf(input_file, start_page, end_page)
