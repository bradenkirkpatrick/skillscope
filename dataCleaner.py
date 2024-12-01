import pandas as pd
import re

file_name = "rit_jobs.csv"
file_name_output = "cleanedJobs.csv"

# Read the CSV file
df = pd.read_csv(file_name, sep="\t or ,")

# Define unwanted keywords
unwanted_keywords = [
    "keywords search location distance from location",
    "create job alert",
    "page",
    "privacy policy",
    "terms of use"
]

# Function to check if a row contains any unwanted keywords
def contains_unwanted_keywords(row):
    row_str = ' '.join(row.astype(str)).lower()
    return any(keyword in row_str for keyword in unwanted_keywords)

# Filter out rows containing unwanted keywords
df = df[~df.apply(contains_unwanted_keywords, axis=1)]

# Normalize text in all columns
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

df = df.applymap(lambda x: normalize_text(x) if isinstance(x, str) else x)

# Remove duplicate rows
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv(file_name_output, index=False)