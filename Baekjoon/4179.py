import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

maze = []
for _ in range(r):
    column = input().rstrip()
    maze.append(column)

def bfs(x, y, visited):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                pass


time = 0
while True:
    canMove = False

    visited = [[False]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if visited[r][c] == False:
                visited = True
                bfs(i, j, visited)

    if not canMove:
        break
    time += 1

print(time)