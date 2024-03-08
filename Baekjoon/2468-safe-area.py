import sys
from collections import deque
# BFS로 풀거임

input = sys.stdin.readline

N = int(input())
grid = []
MAX = 0
for _ in range(N):
    column = list(map(int, input().split()))
    max_column = max(column)
    MAX = max(MAX, max_column)
    grid.append(column)

# 비가 오는 높이 0~최대값-1까지 돌면서 safe area를 확인

def bfs(x, y, height, v):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    v[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] > height and not v[nx][ny]:

                    v[nx][ny] = True
                    queue.append((nx, ny))



max_safe_area = 0 # 비높이가 0이면 값이 1이기 떄문에, 무조건 1이상임
for h in range(MAX): # 비높이 1부터 MAX-1까지
    visited = [[False]*N for _ in range(N)]
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited) # 함수를 돌리면 해당 영역이 True로 색칠됨
                safe_area += 1


    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
