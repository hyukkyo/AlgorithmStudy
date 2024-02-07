# 일단 BFS로 풀어보자. 큐를 써야겠지
from collections import deque

def bfs(start_v):
    visited = [start_v]
    queue = deque(start_v)

    while queue:
        for v in grid[start_v]:
            if v not in visited:
                visited.append(v)
                queue.append

    return visited



def numIslands(grid):
    num_of_islands = 0

    m = len(grid)
    n = len(grid[0])

    visited = [[False]*m for _ in range(n)]

    def bfs(x, y):
        visited[x][y] = True
        queue = deque((x, y))

        while queue:
            cur_x, cur_y = queue.popleft()
            for v in grid[cur_v]:
                if v not in visited:
                    visited.append(v)
                    queue.append(v)

        return visited
    

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visited[i][j] == False:
                bfs()

    return num_of_islands


grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

# grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]

print(numIslands(grid))

# 240207