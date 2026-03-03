import PyPDF2
from bs4 import BeautifulSoup

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def extract_text_from_html(html_path):
    """
    Extracts text from an HTML file.
    """
    with open(html_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        text = soup.get_text()
    return text

def main():
    # Example usage (will be updated later)
    pass

if __name__ == "__main__":
    main()
