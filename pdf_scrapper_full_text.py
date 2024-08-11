from pdfrw import PdfReader
import json

# Load the PDF
pdf_path = 'Antrag_auf_Wohnberechtigungsschein.pdf'  # Replace with your PDF file path
pdf = PdfReader(pdf_path)

# Create lists to hold field information
text_fields = []
checkboxes = []
dropdowns = []

# Iterate through the pages and identify fields
for page in pdf.pages:
    annotations = page.get('/Annots')
    if annotations:
        for annotation in annotations:
            field_type = annotation.get('/FT')
            field_name = annotation.get('/T')
            tooltip_text = annotation.get('/TU')
            # Clean field name and tooltip text
            field_name_cleaned = str(field_name)[1:-1] if field_name else ''
            tooltip_text_cleaned = str(tooltip_text)[1:-1] if tooltip_text else ''

            # Classify into form fields
            if field_type == '/Tx':  # Text Field
                text_fields.append({
                    'Field Name': field_name_cleaned,
                    'Tooltip': tooltip_text_cleaned
                })
            elif field_type == '/Btn' and annotation.get('/AS'):  # Checkbox
                checkboxes.append({
                    'Field Name': field_name_cleaned,
                    'Tooltip': tooltip_text_cleaned
                })
            elif field_type == '/Ch':  # Dropdown
                options = annotation.get('/Opt')
                options_list = [str(opt) for opt in options] if options else []
                dropdowns.append({
                    'Field Name': field_name_cleaned,
                    'Tooltip': tooltip_text_cleaned,
                    'Options': options_list
                })

# Save the extracted fields to a JSON file
extracted_data = {
    'Text Fields': text_fields,
    'Checkboxes': checkboxes,
    'Dropdowns': dropdowns
}
output_json_path = 'extracted_fields.json'
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)

print(f"Data has been saved to {output_json_path}")