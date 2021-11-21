"""
File to manage the creation of a report file in Word format.
Purpose is to create a file, with some fixed sections and information and using the graphs and others with the
data extracted from Excel file.
"""

from docx import Document


# Creation of the document.
def create_document():
    document = Document()
    document.add_heading('Demo heading, level 1', level=1)
    document.save('demo.docx')