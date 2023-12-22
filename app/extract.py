# Read text from the PDF file

from PyPDF2 import PdfReader

def extract_text(pdf_file):
    """
        :param pdf_file: the PDF file to extract
    """

    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text().replace("/n", " ")
        
    return text
