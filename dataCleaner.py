import pandas as pd
import re

file_name = "rit_jobs.csv"
file_name_output = "cleanedJobs.csv"

# Read the CSV file
df = pd.read_csv(file_name, sep="\t or ,", engine='python')

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

df = df.map(lambda x: normalize_text(x) if isinstance(x, str) else x)

# Define specific unwanted words to be removed from text
unwanted_words = [
    "gleason col", "engineering bs", "bs col", "tech bs", "bs golisano", 
    "golisano col", "col compinfo", "engineering ms", "ms golisano", 
    "work", "posistion type", "application process", "jobcoopinternship", 
    "consider candidates", "engineering tech", "details position", 
    "application deadline", "experince", "job type", "addiontal job", 
    "field", "desired majors", "enineeringelectrical", "ms compinfo", 
    "desired start", "study eg", "willing", "defined period", "experience", 
    "additional job", "job type", "ms compinfo", "cptopt interest", "temporarily authorized", 
    "type coopinternship", "ability", "will", "compensation per", "team", "per week", "hours per", 
    "employee", "ms col", "employer", "engineeringelectrical", "must", "week date", "project", 
    "coopinternship compensation", "per hour", "customer", "optcpt", "engineeringmechanical", 
    "saunders college", "product", "engineering", "hour location", "support", "provide", 
    "position", "software", "id hours", "desired class", "class levels", "program", "company", 
    "engineeringcomputer", "nologyelec mech", "optcpt yes", "knowledge", "system", "service", 
    "required", "ms college", "principle", "nologymechatronics eng", "ny usa", " u ", 
    "sciencecomputer science", "sciencesoftware compinfo", "coopinternship location", 
    "5th year", "world", "year senior", "end date", "desired end", "people", "learn", 
    "compinfo sciencecomputer", "4th year", "year juniorsenior", "nologyelectrical engineer", 
    "business", "solution", "engineer tech", "nologymechan", "juniorsenior 5th", "science ms", 
    "role", "design development", "new york", "application", "environment", "job offer", 
    "sciencegame design", "united states", "related resources", "resources job", 
    "offer guidelines", "ethical professional", "professional practice", "engineeringindustrial sys", 
    "sys engineer", "3rd year", "year junior", "data", "including", "sciencecomputing security", 
    "engineeringengineering management", "client", "development ms", "skill", "type fulltime", 
    "junior 4th", "eng tech", "one", "engineeringbiomedical", "intern", "design", "tool", "date jan", 
    "eng phd", "requirement", "andor", "job function", "id cptopt", "technical", "need", "make", "develop", 
    "engineeringmechanical engineering", "compinfo sciencecybersecurity", "id job", "management ms", "compinfo sciencesoftware", 
    "6th year", "year masters", "manufacturing", "part", "committed", "sciencecomputing info", "computer science", "per year", 
    "able", "december related", "2nd year", "preferred", "well", "senior 6th", "year sophomore", "education", "bachelors degree",
    "ing", "sophomore 3rd", "levels 2nd", "college", "include", "benefit", "compinfo sciencecomputing", "electrical engineering", 
    "help", "compinfo sciencegame", "ms saunders", "follow", "based", "quality", "year location", "equal opportunity", "etc", 
    "nologymanufact", "test", "engineeringindustrial", "date may", "strong", "understanding", "within", "nologyrobotics manuf", 
    "manuf eng", "future", "nologycomputer", "student", "equipment", "computer engineering", "build", 
    "sciencecomputational mathematics", "opportunity employer", "yes december", "process", "perform", "industry", "career", 
    "info compinfo", "sexual orientation", "following", "plus", "building", "internship", "technology", "usa id", "national origin",
    "processes", "employment", "value", "construction", "individual", "scienceweb mobile", "jan desired", "additional documents", 
    "use", "market", "fulltime compensation", "drive", "testing", "research", "create"
]

# Function to remove specific unwanted words from text
def remove_unwanted_words(text):
    for word in unwanted_words:
        text = text.replace(word, '')
    return text

# Apply the function to clean specific unwanted words
df = df.map(lambda x: remove_unwanted_words(x) if isinstance(x, str) else x)

# Remove duplicate rows
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv(file_name_output, index=False)