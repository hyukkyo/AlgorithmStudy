from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

graph = []
for _ in range(N):
    row = list(input())
    graph.append(row)

visited = [[0]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

result_normal = 0
result = 0

# 정상인 기준
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            result_normal += 1

# R을 G로 바꿈
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 적록
# 다시 초기화
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            result += 1

print(result_normal, result)