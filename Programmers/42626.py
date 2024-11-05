import heapq

def solution(scoville, K):
    answer = 0
    minheap = scoville.copy()

    heapq.heapify(minheap)
    while len(minheap) >= 2 and minheap[0] < K:
        small = heapq.heappop(minheap)
        big = heapq.heappop(minheap)

        heapq.heappush(minheap, big*2 + small)

        answer += 1

    if minheap[0] < K:
        answer = -1

    return answer