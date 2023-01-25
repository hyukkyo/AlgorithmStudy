# import sys

# n, k = map(int, sys.stdin.readline().split())

# arr = list(range(1, n+1))


# print('<', end='')
# i = 0
# for _ in range(n):
#     i += k-1
#     if i >= len(arr):
#         i = i % len(arr)

#     print(arr[i], end=', ')
#     del arr[i]

# print('\b\b>')
# 왜 안되지 위에거???

N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]

answer = []
num = 0

for t in range(N):
    num += K-1  
    if num >= len(arr):
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')