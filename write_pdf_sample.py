from pdfrw import PdfReader, PdfWriter, PdfName, PdfDict

# Load the PDF
pdf_path = 'somegermanform.pdf'  # Replace with your PDF file path
pdf = PdfReader(pdf_path)

# Update the 'telefon' field
for page in pdf.pages:
    annotations = page.get('/Annots')
    if annotations:
        for annotation in annotations:
            field_name = annotation.get('/T')
            if field_name and field_name[1:-1] == 'telefon':  # Remove parentheses
                annotation.update(
                    PdfDict(
                        V='0123456789',  # Set the value for the 'telefon' field
                        Ff=1  # Set the field as read-only if needed
                    )
                )

# Save the updated PDF
output_path = 'updated_pdf_file.pdf'  # Specify the output file path
PdfWriter(output_path, trailer=pdf).write()