# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(input().split())

# row_now = 0
# column_now = 0

# for direction in arr:
#     if direction == 'R' and column_now + 1 < N:
#         column_now = column_now + 1
#     elif direction == 'L' and column_now - 1 >= 0:
#         column_now = column_now - 1
#     elif direction == 'U' and row_now - 1 >= 0:
#         row_now = row_now - 1
#     elif direction == 'D' and row_now + 1 < N:
#         row_now = row_now + 1
    
# print(row_now + 1, column_now + 1)

n = int(input())
r, c = 1, 1
plans = input().split()

dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nc = c + dc[i]
            nr = r + dr[i]
    
    if nc < 1 or nr < 1 or nc > n or nr > n:
        continue

    r, c = nr, nc

print(r, c)