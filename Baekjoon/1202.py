import sys
import heapq

# sys.stdin.readline() === input()
n, k = map(int, sys.stdin.readline().split())

mv_list = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    mv_list.append([m, v])
mv_list.sort()

c_list = []
for _ in range(k):
    c = int(sys.stdin.readline())
    c_list.append(c)
c_list.sort()

enable_jewel = []
sum = 0
for c in c_list:
    while mv_list and mv_list[0][0] <= c:
        heapq.heappush(enable_jewel, -mv_list[0][1])
        heapq.heappop(mv_list)
    if enable_jewel:
        sum -= heapq.heappop(enable_jewel)
print(sum)
        


# 모르겠다
# 최대힙(우선순위큐) 사용하기

