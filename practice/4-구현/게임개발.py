import sys
input = sys.stdin.readline

row, column = map(int, input().split())
cr, cc, d = map(int, input().split())
# d(방향)가 0북 1동 2남 3서


grid = []
for i in range(row):
    grid_row = list(map(int, input().split())) # 0육지 1바다
    grid.append(grid_row)

# print(grid)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
# 북 서 남 동 순으로 탐색하도록 배치

# 현재 위치에서 방향 탐색
for i in range(4):
    nr = cr + dr[i]
    nc = cc + dc[i]
    