# api/file_reader.py
import PyPDF2
import pandas as pd
import csv
import docx

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

def read_xlsx(file):
    df = pd.read_excel(file)
    return df.to_csv(index=False)

def read_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    content = "\n".join([",".join(row) for row in reader])
    return content

def read_docx(file):
    doc = docx.Document(file)
    content = "\n".join([para.text for para in doc.paragraphs])
    return content
