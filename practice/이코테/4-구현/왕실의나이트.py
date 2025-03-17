import sys
input = sys.stdin.readline

current_position = input()
row = int(current_position[1])
column = current_position[0]
column = int(ord(column) - 96)

# print(row, column)

dr = [2, 2, -2, -2, 1, 1, -1, -1]
dc = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(8):
    nr = row + dr[i]
    nc = column + dc[i]
    if nr > 0 and nc > 0 and nr < 9 and nc < 9:
        result = result + 1

print(result)
