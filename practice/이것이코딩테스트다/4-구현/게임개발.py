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
visited = [[0] * column for _ in range(row)]
visited[cr][cc] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn_left():
    global d
    d = (d+3) % 4


count = 1 # 이동 횟수
turn_time = 0 # 탐색한 방향 갯수
while True:
    turn_left()
    nr = cr + dr[d]
    nc = cc + dc[d]

    if grid[nr][nc] == 0 and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        cr = nr
        cc = nc
        count += 1
        turn_time = 0
        continue
    else: # 해당 방향으로 못가면
        turn_time += 1
    
    if turn_time == 4: # 더 못가면 뒤로가기
        nr = cr - dr[d]
        nc = cc - dc[d]
        if grid[nr][nc] == 0: # 뒤로갈수있어?
            cr = nr
            cc = nc
        
        else: # 뒤로 못가나?
            break

        turn_time = 0
        

print(count)