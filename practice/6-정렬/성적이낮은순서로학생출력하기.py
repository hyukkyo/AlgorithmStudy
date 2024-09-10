import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda student: student[1])

for i in arr:
    print(i[0], end=' ')