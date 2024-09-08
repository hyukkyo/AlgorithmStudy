import sys
input = sys.stdin.readline

row, column = map(int, input().split())
cr, cc, d = map(int, input().split())
# d(방향)가 0북 1동 2남 3서
# d 기준으로 왼쪽부터 탐색
# 0 -> 3 -> 2 -> 1
# 1 -> 0 -> 3 -> 2
# 2 -> 1 -> 0 -> 3
# 3 -> 2 -> 1 -> 0

grid = []
for i in range(row):
    grid_row = list(map(int, input().split())) # 0육지 1바다
    grid.append(grid_row)

# print(grid)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 현재 위치에서 방향 탐색
for i in range(4):
    nd = (d + 3) % 4 # 다음 방향
    nr = cr + dr[nd]
    nc = cc + dc[nd]

    