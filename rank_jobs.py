import pandas
from string import digits
import re


global POSSIBLE_QUALIFICATIONS, JOBS
POSSIBLE_QUALIFICATIONS = list()
JOBS = list() 

def get_qualifications():
    with open('qualifications.txt') as f:
        return [x.strip() for x in f.readlines()]

def get_jobs():
    jobs = pandas.read_csv('rit_jobs.csv')
    jobs_ = [' '.join(set(x.strip().split())) for x in jobs['job_description']]
    remove_digits = str.maketrans('', '', digits)
    for i in range(len(jobs)):
        jobs_[i] = jobs_[i].translate(remove_digits)
    jobs_ = [re.sub(r'[./$()]', '', job) for job in jobs_]
    return [' '.join(job.split()) for job in jobs_]


POSSIBLE_QUALIFICATIONS = get_qualifications()
JOBS = get_jobs()

def check_new_qualifications(qualifications):
    for qualification in qualifications:
        if qualification not in POSSIBLE_QUALIFICATIONS:
            POSSIBLE_QUALIFICATIONS.append(qualification)
            with open('qualifications.txt', 'a') as f:
                f.write(qualification + '\n')
    POSSIBLE_QUALIFICATIONS.append(qualification)

def job_qualifications_list(job):
    job = set(job.lower().split())

    qualifications = set()
    for i in range(len(POSSIBLE_QUALIFICATIONS)):
        if POSSIBLE_QUALIFICATIONS[i] in job:
            qualifications.add(POSSIBLE_QUALIFICATIONS[i])
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

def main(personal_qualifications):
    check_new_qualifications(personal_qualifications)
    ranked_jobs_list = sorted(get_best_jobs(JOBS, personal_qualifications), key=lambda x: -x[1])
    print(ranked_jobs_list)

if __name__ == "__main__":
    PERSONAL_QUALIFICATIONS = ["python", "c"]
    main(PERSONAL_QUALIFICATIONS)



