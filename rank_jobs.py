
# The point of this script is to rank jobs based on qualifications.
# main takes in a list of jobs strings and a list of personal qualifications.

POSSIBLE_QUALIFICATIONS = list()
with open('qualifications.txt') as f:
    POSSIBLE_QUALIFICATIONS = [x.strip() for x in f.readlines()]

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

def main(job, personal_qualifications):
    personal_qualifications.lower()
    check_new_qualifications(personal_qualifications)
    ranked_jobs_list = sorted(get_best_jobs(job, personal_qualifications), key=lambda x: -x[1])
    print(ranked_jobs_list)

if __name__ == "__main__":
    JOBS = ["I like python. Program some python for me: 1,000,000₽.", "Nah, bitch, c++ is king.", "james bond.", "c and python with java", "python java bash go"] #just a placeholder
    PERSONAL_QUALIFICATIONS = ["python", "c"] #just a placeholder
    main(JOBS, PERSONAL_QUALIFICATIONS)



