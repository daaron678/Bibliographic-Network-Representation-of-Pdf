import pymupdf  # PDF text extraction, install with venv: https://pymupdf.readthedocs.io/en/latest/installation.html 
import argparse # handle cli args
import sys
from pathlib import Path

# extract_text_from_pdf() taken from https://github.com/matheusmaldaner/PlatosCave/blob/main/backend/main.py 
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text content from a PDF file using PyMuPDF.
    Returns:
        Extracted text content as a string

    Raises:
        FileNotFoundError: If PDF file doesn't exist
        Exception: If PDF extraction fails
    """
    pdf_path_obj = Path(pdf_path).resolve()

    if not pdf_path_obj.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if not pdf_path_obj.is_file():
        raise ValueError(f"Path is not a file: {pdf_path}")

    print(f"[MAIN.PY DEBUG] Extracting text from PDF: {pdf_path}", file=sys.stderr, flush=True)
    try:
        # Open the PDF file
        doc = pymupdf.open(pdf_path) 
        text_content = []
        page_count = len(doc) - 1  # exclude last page (bibliography) of the article 

        # Extract text from each page
        for page_num in range(page_count):
            page = doc[page_num]
            page_text = page.get_text() 
            # if page_text.strip():  # evaluates to false if len(page_text) is 0 (empty string) so that empty pages are excluded 
            #     text_content.append(f"--- Page {page_num + 1} ---\n{page_text}")

        doc.close()

        extracted_text = "\n\n".join(text_content) # add two newlines after every page
        print(f"[MAIN.PY DEBUG] Extracted {len(extracted_text)} characters from {page_count} pages", file=sys.stderr, flush=True)

        return extracted_text

    except Exception as e:
        print(f"[MAIN.PY DEBUG] Error extracting PDF text: {e}", file=sys.stderr, flush=True)
        raise Exception(f"Failed to extract text from PDF: {e}")

def build_attributes():
    return

def main(pdf_path: str):   # main(path, keywords: semantic network)
    extract_text_from_pdf(pdf_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze research papers from URL or PDF file.")
    parser.add_argument("filepath", type=str, help="The path to the PDF file.")
    args = parser.parse_args()
    main(args.filepath)
    
    # CLI format to run program:
    # python main.py "../article.pdf"
    
    
    
    
    