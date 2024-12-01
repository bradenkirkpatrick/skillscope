import pandas
from string import digits
import re



def get_languages():
    with open('qualifications/languages.txt') as f:
        return [x.strip() for x in f.readlines()]

def get_libraries():
    with open('qualifications/libraries.txt') as f:
        return [x.strip() for x in f.readlines()]
    
def get_tools():
    with open('qualifications/tools.txt') as f:
        return [x.strip() for x in f.readlines()]
    
def get_softskills():
    with open('qualifications/softskills.txt') as f:
        return [x.strip() for x in f.readlines()]

def get_jobs():
    jobs = pandas.read_csv('cleanedJobs.csv')
    jobs_ = [' '.join(set(x.strip().split())) for x in jobs['job_description']]
    remove_digits = str.maketrans('', '', digits)
    for i in range(len(jobs)):
        jobs_[i] = jobs_[i].translate(remove_digits)
    jobs_ = [re.sub(r'[./$()]', '', job) for job in jobs_]
    return [' '.join(job.split()) for job in jobs_]


POSSIBLE_LANGUAGES = get_languages()
POSSIBLE_LIBRARIES = get_libraries()
POSSIBLE_TOOLS = get_tools()
POSSIBLE_SOFTSKILLS = get_softskills()
JOBS = get_jobs()

def check_new_qualifications(qualifications, list_):
    for qualification in qualifications:
        if qualification not in list_:
            list_.append(qualification)
            with open('qualifications.txt', 'a') as f:
                f.write(qualification + '\n')
    list_.append(qualification)
    return list_

def job_qualifications_list(job, qualifications_list):
    job = job.lower()

    qualifications = set()
    for qualification in qualifications_list:
        if qualification in job:
            qualifications.add(qualification)
    return qualifications

# basic algorithm to rank jobs based on qualifications # replace with ML model?
def get_best_jobs(jobs, personal_qualifications):
    ranked_jobs_list = list()
    for i in range(len(jobs)):
        job_qualifications = job_qualifications_list(jobs[i])
        # replace with one hot encoding for data processing
        valid_qualifactions = job_qualifications.intersection(personal_qualifications)
        invalid_qualifications = job_qualifications.difference(personal_qualifications)
        #
        # replace with ML model?
        try:
            try:
                num = len(valid_qualifactions) / len(invalid_qualifications)
            except ZeroDivisionError:
                num = len(valid_qualifactions)
        except ZeroDivisionError:
            num = 1 / len(invalid_qualifications)
        #
        ranked_jobs_list.append((jobs[i][:15], round(num, 2)))
    return ranked_jobs_list

def get_best(jobs, type):
    jobs_dict = dict()
    if type == "languages":
        skills = POSSIBLE_LANGUAGES
    elif type == "libraries":
        skills = POSSIBLE_LIBRARIES
    elif type == "softkills":
        skills = POSSIBLE_SOFTSKILLS
    elif type == "tools":
        skills = POSSIBLE_TOOLS
    for job in jobs:
        job_qualifications = job_qualifications_list(job, skills)
        for qualification in job_qualifications:
            if qualification in jobs_dict:
                jobs_dict[qualification] += 1
            else:
                jobs_dict[qualification] = 1
    return jobs_dict

# def main(personal_qualifications):
#     check_new_qualifications(personal_qualifications)
#     ranked_jobs_list = sorted(get_best_jobs(JOBS, personal_qualifications), key=lambda x: -x[1])
#     print(ranked_jobs_list)

# if __name__ == "__main__":
#     PERSONAL_QUALIFICATIONS = ["python", "c"]
#     main(PERSONAL_QUALIFICATIONS)

def percent_of_dict(dictionary, total):
    for key in dictionary:
        dictionary[key] = round((dictionary[key] / total) * 100, 2)
    return dictionary

# if __name__ == "__main__":
#     # # languages
#     # best_languages = get_best(JOBS, "languages")
#     # sorted_best_languages = dict(sorted(best_languages.items(), key=lambda item: item[1], reverse=True))
#     # print(sorted_best_languages)
#     # # percent
#     # print(percent_of_dict(sorted_best_languages, len(JOBS)))

#     # # libraries
#     # best_libraries = get_best(JOBS, "libraries")
#     # sorted_best_libraries = dict(sorted(best_libraries.items(), key=lambda item: item[1], reverse=True))
#     # print(sorted_best_libraries)
#     # # percent
#     # print(percent_of_dict(sorted_best_libraries, len(JOBS)))

#     # # tools
#     # best_tools = get_best(JOBS, "tools")
#     # sorted_best_tools = dict(sorted(best_tools.items(), key=lambda item: item[1], reverse=True))
#     # print(sorted_best_tools)
#     # # percent
#     # print(percent_of_dict(sorted_best_tools, len(JOBS)))

#     # softskills
#     best_softskills = get_best(JOBS, "softkills")
#     sorted_best_softskills = dict(sorted(best_softskills.items(), key=lambda item: item[1], reverse=True))
#     print(sorted_best_softskills)
#     # percent
#     print(percent_of_dict(sorted_best_softskills, len(JOBS)))
          
def hit_it_boy():
    best_languages = get_best(JOBS, "languages")
    sorted_best_languages = percent_of_dict(dict(sorted(best_languages.items(), key=lambda item: item[1], reverse=True)), len(JOBS))
    sorted_best_languages_keys = list(sorted_best_languages.keys())

    best_libraries = get_best(JOBS, "libraries")
    sorted_best_libraries = percent_of_dict(dict(sorted(best_libraries.items(), key=lambda item: item[1], reverse=True)), len(JOBS))
    sorted_best_libraries_keys = list(sorted_best_libraries.keys())

    best_tools = get_best(JOBS, "tools")
    sorted_best_tools = percent_of_dict(dict(sorted(best_tools.items(), key=lambda item: item[1], reverse=True)), len(JOBS))
    sorted_best_tools_keys = list(sorted_best_tools.keys())

    best_softskills = get_best(JOBS, "softkills")
    sorted_best_softskills = percent_of_dict(dict(sorted(best_softskills.items(), key=lambda item: item[1], reverse=True)), len(JOBS))
    sorted_best_softskills_keys = list(sorted_best_softskills.keys())
    hit = "import { StatsData } from '../types/stats';\n export const mockStats: StatsData = {\n languages: [\n"+"{ name: '"+f"{sorted_best_languages_keys[0]}"+"', value: '"+f"{sorted_best_languages[sorted_best_languages_keys[0]]}'"+" },\n"+"{ name: '"+f"{sorted_best_languages_keys[1]}"+"', value: '"+f"{sorted_best_languages[sorted_best_languages_keys[1]]}'"+" },\n"+"{ name: '"+f"{sorted_best_languages_keys[2]}"+"', value: '"+f"{sorted_best_languages[sorted_best_languages_keys[2]]}'"+" },\n"+"{ name: '"+f"{sorted_best_languages_keys[3]}"+"', value: '"+f"{sorted_best_languages[sorted_best_languages_keys[3]]}'"+" },\n"+"{ name: '"+f"{sorted_best_languages_keys[4]}"+"', value: '"+f"{sorted_best_languages[sorted_best_languages_keys[4]]}'"+" },\n],libraries: ["+"{ name: '"+f"{sorted_best_libraries_keys[0]}"+"', value: '"+f"{sorted_best_libraries[sorted_best_libraries_keys[0]]}'"+" },\n{ name: '"+f"{sorted_best_libraries_keys[1]}', value: '"+f"{sorted_best_libraries[sorted_best_libraries_keys[1]]}'"+" },\n{ name: '"+f"{sorted_best_libraries_keys[2]}', value: '"+f"{sorted_best_libraries[sorted_best_libraries_keys[2]]}'"+" },\n{ name: '"+f"{sorted_best_libraries_keys[3]}', value: '"+f"{sorted_best_libraries[sorted_best_libraries_keys[3]]}'"+" },\n{ name: '"+f"{sorted_best_libraries_keys[4]}', value: '"+f"{sorted_best_libraries[sorted_best_libraries_keys[4]]}'"+" },\n],tools: ["+"{ name: '"+f"{sorted_best_tools_keys[0]}"+"', value: '"+f"{sorted_best_tools[sorted_best_tools_keys[0]]}'"+" },\n"+"{ name: '"+f"{sorted_best_tools_keys[1]}"+"', value: '"+f"{sorted_best_tools[sorted_best_tools_keys[1]]}'"+" },\n"+"{ name: '"+f"{sorted_best_tools_keys[2]}"+"', value: '"+f"{sorted_best_tools[sorted_best_tools_keys[2]]}'"+" },\n"+"{ name: '"+f"{sorted_best_tools_keys[3]}"+"', value: '"+f"{sorted_best_tools[sorted_best_tools_keys[3]]}'"+" },\n"+"{ name: '"+f"{sorted_best_tools_keys[4]}"+"', value: '"+f"{sorted_best_tools[sorted_best_tools_keys[4]]}'"+" },\n],softSkills: [{ name: '"+f"{sorted_best_softskills_keys[0]}"+"', value: '"+f"{sorted_best_softskills[sorted_best_softskills_keys[0]]}'"+" },\n"+"{ name: '"+f"{sorted_best_softskills_keys[1]}"+"', value: '"+f"{sorted_best_softskills[sorted_best_softskills_keys[1]]}'"+" },\n"+"{ name: '"+f"{sorted_best_softskills_keys[2]}"+"', value: '"+f"{sorted_best_softskills[sorted_best_softskills_keys[2]]}'"+" },\n"+"{ name: '"+f"{sorted_best_softskills_keys[3]}"+"', value: '"+f"{sorted_best_softskills[sorted_best_softskills_keys[3]]}'"+" },\n"+"{ name: '"+f"{sorted_best_softskills_keys[4]}"+"', value: '"+f"{sorted_best_softskills[sorted_best_softskills_keys[4]]}'"+" },\n],};"
    with open('skill-scope-site-2/src/data/mockStats.ts', 'w') as f:
        f.write(hit)

if __name__ == "__main__":
    hit_it_boy()
