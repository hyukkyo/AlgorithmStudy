import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
for i in range(n):
    column = list(map(int, input().split()))
    grid.append(column)


result = 0

# 1. 벽 3개 넣기
# 2. 값이 2인곳에서 2로 BFS
# 3. 값이 0인곳에서 BFS하면서 갯수를 뱉음.
# 4. 최댓값 갱신
    
def make_walls(num):
    if num == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                make_walls(num+1)
                grid[i][j] = 0 


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    test_grid = copy.deepcopy(grid) # deepcopy를 안해주면 제대로 작동이 안되네
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if (0 <= next_x < n) and (0 <= next_y < m):
                if test_grid[next_x][next_y] == 0:
                    test_grid[next_x][next_y] = 2
                    queue.append((next_x, next_y))

    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == 0:
                count += 1
    
    result = max(result, count)


make_walls(0)

print(result)