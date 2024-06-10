import PyPDF2
import pandas as pd
import csv
import docx

def read_pdf(file):
    """
    Read text content from a PDF file.
    
    Args:
    - file: File object of the PDF file.
    
    Returns:
    - str: Text content of the PDF.
    """
    reader = PyPDF2.PdfReader(file)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

def read_xlsx(file):
    """
    Read data from an Excel file and convert it to CSV format.
    
    Args:
    - file: File object of the Excel file.
    
    Returns:
    - str: CSV-formatted data.
    """
    df = pd.read_excel(file)
    return df.to_csv(index=False)

def read_csv(file):
    """
    Read text content from a CSV file.
    
    Args:
    - file: File object of the CSV file.
    
    Returns:
    - str: Text content of the CSV.
    """
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    content = "\n".join([",".join(row) for row in reader])
    return content

def read_docx(file):
    """
    Read text content from a DOCX file.
    
    Args:
    - file: File object of the DOCX file.
    
    Returns:
    - str: Text content of the DOCX.
    """
    doc = docx.Document(file)
    content = "\n".join([para.text for para in doc.paragraphs])
    return content
