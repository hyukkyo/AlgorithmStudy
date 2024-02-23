# BFS로 풀면 될거같음
import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip())))

path = grid

def bfs(grid, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]


    path[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x >= 0 and next_x < N and next_y >= 0 and next_y < M:
                if grid[next_x][next_y] == 1 and path[next_x][next_y] == 1:
                    path[next_x][next_y] += 1
                    queue.append((next_x, next_y))

    return path[-1][-1]



print(bfs(grid, 0, 0))
