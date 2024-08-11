from pdfrw import PdfReader

# Load the PDF
pdf_path = 'WBSformular.pdf'  # Replace with your PDF file path
pdf = PdfReader(pdf_path)

# Create lists to hold field names
text_inputs = []
radioboxes = []
checkboxes = []
dropdowns = []

# Iterate through the pages and identify fields
for page in pdf.pages:
    annotations = page.get('/Annots')
    if annotations:
        for annotation in annotations:
            field_type = annotation.get('/FT')
            field_name = annotation.get('/T')
            if field_name:
                field_name_cleaned = str(field_name)[1:-1]  # Clean field name
                # Classify into form fields
                if field_type == '/Tx':
                    text_inputs.append(field_name_cleaned)  # Text Input
                elif field_type == '/Btn':
                    # Check if it's a radio button or checkbox
                    if annotation.get('/AS'):
                        radioboxes.append(field_name_cleaned)  # Radio Button
                    else:
                        checkboxes.append(field_name_cleaned)  # Checkbox
                elif field_type == '/Ch':
                    dropdowns.append(field_name_cleaned)  # Dropdown

print("Text Inputs:", text_inputs)
print("Radio Buttons:", radioboxes)
print("Checkboxes:", checkboxes)
print("Dropdowns:", dropdowns)