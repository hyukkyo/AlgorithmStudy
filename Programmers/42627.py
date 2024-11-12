import heapq

def solution(jobs):
    min_heap = []

    answer = 0
    current_time = 0
    start = -1

    i = 0
    while i < len(jobs):

        for job in jobs:
            if start < job[0] < current_time:
                heapq.heappush(min_heap, (job[1], job[0]))
        
    return answer