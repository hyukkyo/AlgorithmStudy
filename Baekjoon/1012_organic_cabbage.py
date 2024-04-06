import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
result = []

# def bfs(x, y, visited):
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]

#     visited[y][x] = True
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         cur_x, cur_y = queue.popleft()
#         for i in range(4):
#             next_x = cur_x + dx[i]
#             next_y = cur_y + dy[i]
#             if (0 <= next_x < m) and (0 <= next_y < n):
#                 if grid[next_y][next_x] == 1 and not visited[next_y][next_x]:
#                     visited[next_y][next_x] = True
#                     queue.append((next_x, next_y))

for i in range(t):
    m, n, k = map(int, input().split())
    grid = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    # 세팅 완료


    visited = [[False]*m for _ in range(n)]
    
    def bfs(x, y):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited[y][x] = True
        queue = deque()
        queue.append((x, y))

        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if (0 <= next_x < m) and (0 <= next_y < n):
                    if grid[next_y][next_x] == 1 and not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        queue.append((next_x, next_y))
                        
    num = 0
    for j in range(n):
        for k in range(m):
            if grid[j][k] == 1 and visited[j][k] == False:
                bfs(j, k, visited=visited)
                num += 1

    print(num)