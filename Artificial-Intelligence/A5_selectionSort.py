"""
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, n):
    # Sort the jobs by decreasing profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Result array to store the job sequence
    result = [-1] * n
    job_sequence = ['-1'] * n

    # Iterate through all the jobs
    for job in jobs:
        # Find a free slot for this job, starting from its deadline
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] == -1:  # If the slot is free
                result[j] = job.job_id
                job_sequence[j] = job.job_id
                break

    # Calculate total profit
    total_profit = sum([jobs[i - 1].profit for i in result if i != -1])
    return job_sequence, total_profit

if __name__ == "__main__":
    # List of jobs (job_id, deadline, profit)
    jobs = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 1, 40),
        Job(4, 1, 30)
    ]
    
    # Maximum deadline to decide the array size
    max_deadline = max(job.deadline for job in jobs)

    # Get the optimal job sequence and the total profit
    job_sequence, total_profit = job_scheduling(jobs, max_deadline)
    
    # Print the results
    print("Job sequence to maximize profit:", job_sequence)
    print("Total Profit:", total_profit)
"""


#######################################################################################

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, n):
    # Sort the jobs by decreasing profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Result array to store the job sequence
    result = [-1] * n
    job_sequence = ['-1'] * n

    # Iterate through all the jobs
    for job in jobs:
        # Find a free slot for this job, starting from its deadline
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] == -1:  # If the slot is free
                result[j] = job.job_id
                job_sequence[j] = job.job_id
                break

    # Calculate total profit
    total_profit = sum([jobs[i - 1].profit for i in result if i != -1])
    return job_sequence, total_profit

if __name__ == "__main__":
    # List of profits (in decreasing order)
    profits = [40, 30, 20, 10]

    jobs = []
    # Take input for deadlines
    for i in range(1, len(profits) + 1):
        deadline = int(input(f"Enter the deadline for Job {i}: "))
        jobs.append(Job(i, deadline, profits[i-1]))

    # Maximum deadline to decide the array size
    max_deadline = max(job.deadline for job in jobs)

    # Get the optimal job sequence and the total profit
    job_sequence, total_profit = job_scheduling(jobs, max_deadline)
    
    # Print the results
    print("Job sequence to maximize profit:", job_sequence)
    print("Total Profit:", total_profit)
