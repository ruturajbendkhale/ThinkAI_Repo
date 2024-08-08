from pdfrw import PdfReader

# Load the PDF
pdf_path = 'somegermanform.pdf'  # Replace with your PDF file path
pdf = PdfReader(pdf_path)

# Create a list to hold full radio button texts
radio_button_full_texts = []

# Iterate through the pages and identify radio button fields
for page in pdf.pages:
    annotations = page.get('/Annots')
    if annotations:
        for annotation in annotations:
            field_type = annotation.get('/FT')
            if field_type == '/Btn' and annotation.get('/AS'):
                # Extract the full text from the /TU or /Alt attribute
                full_text = annotation.get('/TU') or annotation.get('/Alt')
                if full_text:
                    # Clean the full text by removing parentheses
                    full_text_cleaned = str(full_text)[1:-1]
                    radio_button_full_texts.append(full_text_cleaned)

# Print the full text of radio buttons
print('Radio Button Full Texts:', radio_button_full_texts)