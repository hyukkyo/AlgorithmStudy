# BFS로 풀면 될듯
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip())))

# print(grid)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c)) # 0, 0부터 시작
    while queue:
        r, c = queue.popleft() # 0, 0 빼냄
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m: # 이동범위 넘어가면 패스
                continue

            if grid[nr][nc] == 0: # 해당 범위안인데, 벽이면 패스
                continue

            if grid[nr][nc] == 1: # 길이면? 
                grid[nr][nc] = grid[r][c]+ 1 # 이동 하면서 숫자 1 더하기
                queue.append((nr, nc)) # (1, 0) 넣기

    return grid[n-1][m-1]
    
print(bfs(0, 0))