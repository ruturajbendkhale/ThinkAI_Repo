from pdfrw import PdfReader

# Load the PDF
pdf_path = 'somegermanform.pdf'  # Replace with your PDF file path
pdf = PdfReader(pdf_path)

# Create lists to hold field names
radioboxes = []
dropdowns = []

# Iterate through the pages and identify fields
for page in pdf.pages:
    annotations = page.get('/Annots')
    if annotations:
        for annotation in annotations:
            field_type = annotation.get('/FT')
            field_name = annotation.get('/T')
            if field_name:
                # Clean field name by stripping parentheses and ensure it's a string
                field_name_cleaned = str(field_name)[1:-1]
                # Classify into radioboxes or dropdowns
                if field_type == '/Btn' and annotation.get('/AS'):
                    # Check if it's a radio button
                    radioboxes.append(field_name_cleaned)
                elif field_type == '/Ch':
                    # Check if it's a dropdown
                    dropdowns.append(field_name_cleaned)

print("Radio Boxes:", radioboxes)
print("Dropdowns:", dropdowns)
print("Raw Field Name:", field_name)