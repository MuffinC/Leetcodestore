import math
def minimumTime(jobs, workers):
    totaltime = []
    jobs = sorted(jobs, reverse=True)
    workers = sorted(workers, reverse=True)
    for x in range(len(jobs)):
        cur=math.ceil(jobs[x] / workers[x])
        totaltime.append(cur)
    return max(totaltime)
print(minimumTime([3,18,15,9],[6,5,1,3]))