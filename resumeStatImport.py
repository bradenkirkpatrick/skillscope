import json
import os

def load_compare_data():
    """Load data from compareD.json."""
    with open('compareD/compareD.json') as f:
        return json.load(f)

def format_data(data):
    """Format data to match the structure of mockStats.ts."""
    def format_entries(entries):
        return [
            f"{{ name: '{entry['skill']}', value: '{entry['proficiency']}%' }}"
            for entry in entries
        ]
    
    return {
        'languages': format_entries(data['Languages']),
        'libraries': format_entries(data['Libraries']),
        'tools': format_entries(data['Tools']),
        'softSkills': format_entries(data['Soft Skills'])
    }

def write_resume_stats(formatted_data):
    """Write formatted data to resumeStats.ts."""
    content = (
        "import { StatsData } from '../types/stats';\n"
        "export const resumeStats: StatsData = {\n"
        f"languages: [\n{',\n'.join(formatted_data['languages'])}\n],"
        f"libraries: [\n{',\n'.join(formatted_data['libraries'])}\n],"
        f"tools: [\n{',\n'.join(formatted_data['tools'])}\n],"
        f"softSkills: [\n{',\n'.join(formatted_data['softSkills'])}\n],"
        "};"
    )
    with open('skill-scope-site-2/src/data/resumeStats.ts', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    compare_data = load_compare_data()
    formatted_data = format_data(compare_data)
    write_resume_stats(formatted_data)
