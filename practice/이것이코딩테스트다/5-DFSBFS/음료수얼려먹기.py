# DFS로 풀면 됨

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid_row = list(map(int, input().strip()))
    grid.append(grid_row)

# print(grid)

visited = [[False]*m for _ in range(n)]

def dfs(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    
    if grid[r][c] == 0:
        grid[r][c] = 1
        
        dfs(r-1, c)
        dfs(r, c-1)
        dfs(r+1, c)
        dfs(r, c+1)
        return True
    
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
