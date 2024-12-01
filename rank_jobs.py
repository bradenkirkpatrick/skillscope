import pandas as pd
import re
from string import digits

# Functions to read qualifications from text files
def get_languages():
    """Read programming languages from 'qualifications/languages.txt'."""
    with open('qualifications/languages.txt') as f:
        return [line.strip().lower() for line in f]

def get_libraries():
    """Read programming libraries from 'qualifications/libraries.txt'."""
    with open('qualifications/libraries.txt') as f:
        return [line.strip().lower() for line in f]

def get_tools():
    """Read tools from 'qualifications/tools.txt'."""
    with open('qualifications/tools.txt') as f:
        return [line.strip().lower() for line in f]

def get_softskills():
    """Read soft skills from 'qualifications/softskills.txt'."""
    with open('qualifications/softskills.txt') as f:
        return [line.strip().lower() for line in f]

# Function to read and clean job descriptions from CSV file
def get_jobs():
    """Read and clean job descriptions from 'cleanedJobs.csv'."""
    jobs = pd.read_csv('cleanedJobs.csv')
    jobs.columns = jobs.columns.str.strip().str.replace(r'^\W+|\W+$', '', regex=True)
    # Identify the 'job_description' column
    job_desc_col = next((col for col in jobs.columns if 'job_description' in col.lower()), None)
    if not job_desc_col:
        raise KeyError("The 'job_description' column is missing from the cleanedJobs.csv file.")

    job_descriptions = jobs[job_desc_col].fillna('').astype(str)
    remove_digits = str.maketrans('', '', digits)
    cleaned_jobs = []
    for description in job_descriptions:
        description = ' '.join(set(description.strip().split()))
        description = description.translate(remove_digits)
        # Remove special characters and punctuation
        description = re.sub(r'[^\w\s]', ' ', description)
        # Convert to lowercase
        description = description.lower()
        cleaned_jobs.append(' '.join(description.split()))
    return cleaned_jobs

# Function to check and add new qualifications to the list
def check_new_qualifications(qualifications, qualifications_list):
    """Check and add new qualifications to the list."""
    for qualification in qualifications:
        if qualification not in qualifications_list:
            qualifications_list.append(qualification)
            with open('qualifications.txt', 'a') as f:
                f.write(qualification + '\n')
    return qualifications_list

# Function to extract qualifications from a job description
def extract_job_qualifications(job_description, qualifications_list):
    """Extract qualifications from a job description."""
    qualifications_found = set()
    for qualification in qualifications_list:
        # Create a regex pattern to match whole words (case-insensitive)
        pattern = r'\b' + re.escape(qualification) + r'\b'
        if re.search(pattern, job_description):
            qualifications_found.add(qualification)
    return qualifications_found

# Basic algorithm to rank jobs based on qualifications
def get_best_jobs(job_descriptions, personal_qualifications):
    """Rank jobs based on personal qualifications."""
    ranked_jobs = []
    for description in job_descriptions:
        job_qualifications = extract_job_qualifications(description, personal_qualifications)
        valid_qualifications = job_qualifications & personal_qualifications
        invalid_qualifications = job_qualifications - personal_qualifications
        if invalid_qualifications:
            score = len(valid_qualifications) / len(invalid_qualifications)
        else:
            score = len(valid_qualifications)
        ranked_jobs.append((description[:15], round(score, 2)))
    return ranked_jobs

# Function to get the most common qualifications of a specific type from jobs
def get_top_qualifications(job_descriptions, qualification_type):
    """Get the most common qualifications of a specific type from jobs."""
    qualifications_count = {}
    if qualification_type == "languages":
        skills = POSSIBLE_LANGUAGES
    elif qualification_type == "libraries":
        skills = POSSIBLE_LIBRARIES
    elif qualification_type == "softskills":
        skills = POSSIBLE_SOFTSKILLS
    elif qualification_type == "tools":
        skills = POSSIBLE_TOOLS
    else:
        return {}
    for description in job_descriptions:
        job_qualifications = extract_job_qualifications(description, skills)
        for qualification in job_qualifications:
            qualifications_count[qualification] = qualifications_count.get(qualification, 0) + 1
    return qualifications_count

# Function to convert counts to percentages
def convert_counts_to_percentages(counts_dict):
    """Convert counts in a dictionary to percentages based on total qualifications found."""
    total_counts = sum(counts_dict.values())
    for key in counts_dict:
        counts_dict[key] = round((counts_dict[key] / total_counts) * 100, 2)
    return counts_dict

# Function to generate mockStats.ts file
def generate_mock_stats():
    """Generate the mockStats.ts file with the top qualifications."""
    best_languages = get_top_qualifications(JOBS, "languages")
    sorted_languages = dict(sorted(best_languages.items(), key=lambda item: item[1], reverse=True))
    percentages_languages = convert_counts_to_percentages(sorted_languages)
    language_keys = list(percentages_languages.keys())

    best_libraries = get_top_qualifications(JOBS, "libraries")
    sorted_libraries = dict(sorted(best_libraries.items(), key=lambda item: item[1], reverse=True))
    percentages_libraries = convert_counts_to_percentages(sorted_libraries)
    library_keys = list(percentages_libraries.keys())

    best_tools = get_top_qualifications(JOBS, "tools")
    sorted_tools = dict(sorted(best_tools.items(), key=lambda item: item[1], reverse=True))
    percentages_tools = convert_counts_to_percentages(sorted_tools)
    tool_keys = list(percentages_tools.keys())

    best_softskills = get_top_qualifications(JOBS, "softskills")
    sorted_softskills = dict(sorted(best_softskills.items(), key=lambda item: item[1], reverse=True))
    percentages_softskills = convert_counts_to_percentages(sorted_softskills)
    softskill_keys = list(percentages_softskills.keys())

    def get_top_5_entries(sorted_keys, percentages_dict):
        return [
            f"{{ name: '{sorted_keys[i]}', value: '{percentages_dict[sorted_keys[i]]}%' }}"
            for i in range(min(5, len(sorted_keys)))
        ]

    content = (
        "import { StatsData } from '../types/stats';\n"
        "export const mockStats: StatsData = {\n"
        f"languages: [\n{',\n'.join(get_top_5_entries(language_keys, percentages_languages))}\n],"
        f"libraries: [\n{',\n'.join(get_top_5_entries(library_keys, percentages_libraries))}\n],"
        f"tools: [\n{',\n'.join(get_top_5_entries(tool_keys, percentages_tools))}\n],"
        f"softSkills: [\n{',\n'.join(get_top_5_entries(softskill_keys, percentages_softskills))}\n],"
        "};"
    )

    with open('skill-scope-site-2/src/data/mockStats.ts', 'w') as f:
        f.write(content)

# Load qualifications and jobs
POSSIBLE_LANGUAGES = get_languages()
POSSIBLE_LIBRARIES = get_libraries()
POSSIBLE_TOOLS = get_tools()
POSSIBLE_SOFTSKILLS = get_softskills()
JOBS = get_jobs()

# Example usage
if __name__ == "__main__":
    generate_mock_stats()
