import heapq
from collections import deque

def solution(priorities, location):
    q = deque()
    hq = []
    for i in range(len(priorities)):
        q.append((priorities[i], i))
        heapq.heappush(hq, (-priorities[i], i))

    answer = []
    while q:
        if q[0][0] < -hq[0][0]:
            # 뒤로 넘기기
            q.rotate(-1)
        else:
            heapq.heappop(hq)
            answer.append(q.popleft())

    for i in range(len(answer)):
        if answer[i][1] == location:
            return i+1