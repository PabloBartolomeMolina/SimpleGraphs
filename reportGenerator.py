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


# Open a given document if it exists.
def open_document(filename):
    try:
        document = Document(f'./{filename}.docx')
        print("Document: "f'{filename}.docx' " is open")
        document.add_paragraph(
            'First item in ordered list', style='List Number'
        )
        document.add_paragraph(
            'Second item in ordered list', style='List Number'
        )
        records = (
            (3, '101', 'Spam'),
            (7, '422', 'Eggs'),
            (4, '631', 'Spam, spam, eggs, and spam')
        )
        table = document.add_table(rows=1, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Qty'
        hdr_cells[1].text = 'Id'
        hdr_cells[2].text = 'Desc'
        for qty, id1, desc in records:
            row_cells = table.add_row().cells
            row_cells[0].text = str(qty)
            row_cells[1].text = id1
            row_cells[2].text = desc
        p = document.add_paragraph()
        r = p.add_run()
        r.add_text('Good Morning every body,This is my graph : ')
        r.add_picture('./simplegraph1.png')
        r.add_text("Demo image with demo data")

        document.save('demo.docx')
    except:
        print("\nDocument not found:\n" f'{filename}.docx')

