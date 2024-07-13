import sys
input = sys.stdin.readline

N, K = map(int, input().split())

count = 0
# while N != 1:
#     if N % K == 0:
#         N /= K
#         count += 1
#     else:
#         N -= 1
#         count += 1
while N >= K:
    while N % K != 0:
        N -= 1
        count += 1
    
    N //= K
    count += 1

while N > 1:
    N -= 1
    count += 1



print(count)