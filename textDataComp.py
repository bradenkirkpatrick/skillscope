import os
import json
import re
from pdfConverter import extract_text_from_pdf

# Extract text from the PDF file
pdf_path = 'skill-scope-site-2/uploads/resume.pdf'
pdf_text = extract_text_from_pdf(pdf_path)

# Preprocess PDF text
pdf_words = set(re.findall(r'\b\w+\b', pdf_text.lower()))

# Load data from JSON files in collected_data folder
collected_data_path = 'collected_data'
json_files = [f for f in os.listdir(collected_data_path) if f.endswith('.json')]
collected_data = []

for json_file in json_files:
    with open(os.path.join(collected_data_path, json_file), 'r') as file:
        data = json.load(file)
        collected_data.append(data)

# Find matching points between PDF text and collected data
matching_info = []

for data in collected_data:
    # ...existing code...
    for category, content in data.items():
        if isinstance(content, str):
            content_words = set(re.findall(r'\b\w+\b', content.lower()))
            if pdf_words.intersection(content_words):
                matching_info.append((category, content))
        elif isinstance(content, list):
            for item in content:
                item_words = set(re.findall(r'\b\w+\b', str(item).lower()))
                if pdf_words.intersection(item_words):
                    matching_info.append((category, item))
        # ...existing code...

# Display the important matching information
for category, content in matching_info:
    print(f"Matched in '{category}': {content}")
