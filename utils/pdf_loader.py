from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text