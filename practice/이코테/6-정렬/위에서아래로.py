import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True) # 내림차순

for i in arr:
    print(i, end=' ')