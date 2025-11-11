import sys
input = sys.stdin.readline

N, M = map(int, input().split())

max_num = 0
for _ in range(N):
    column = list(map(int, input().split()))
    # min_num = 10000
    min_num = min(column)
    # for j in range(M):
    #     min_num = min(min_num, column[j])
    max_num = max(max_num, min_num)

print(max_num)