# 일단 BFS로 풀어보자. 큐를 써야겠지?
from collections import deque

def numIslands(grid):
    num_of_islands = 0

    m = len(grid)
    n = len(grid[0])

    visited = [[False]*n for _ in range(m)] # 2차원 배열 초기화

    def bfs(x, y): # 2차원 bfs도 형태를 암기해야 함
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited[x][y] = True
        queue = deque((x, y))

        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n: # out of range, 물인곳 처리해주기
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:

                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

            
    

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visited[i][j] == False:
                bfs(i, j)
                num_of_islands += 1
                # dfs()

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