import os
import json
import re
from pdfConverter import extract_text_from_pdf

# Extract text from the PDF file
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, 'skill-scope-site-2/uploads/resume.pdf')  # Use absolute path
pdf_text = extract_text_from_pdf(pdf_path)

# Preprocess PDF text
pdf_words = set(re.findall(r'\b\w+\b', pdf_text.lower()))

# Load data from JSON files in collected_data folder
collected_data_path = os.path.join(script_dir, 'collected_data')
json_files = [f for f in os.listdir(collected_data_path) if f.endswith('.json')]
collected_data = []

# Define category mapping
category_mapping = {
    'tools_data.json': 'Tools',
    'softskills_data.json': 'Soft Skills',
    'libraries_data.json': 'Libraries',
    'languages_data.json': 'Languages'
}

# Initialize matched_info with categories
matched_info = {
    'Tools': [],
    'Soft Skills': [],
    'Libraries': [],
    'Languages': []
}

for json_file in json_files:
    with open(os.path.join(collected_data_path, json_file), 'r') as file:
        data = json.load(file)
        category = category_mapping.get(json_file, 'Others')
        for aspect, percentage in data.items():
            if aspect.lower() in pdf_words:
                matched_info[category].append({
                    'skill': aspect,
                    'proficiency': percentage
                })

# Output the matched information as JSON
print(json.dumps(matched_info))
