import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
result = []

for i in range(t):
    m, n, k = map(int, input().split())
    grid = [[0]*n for _ in range(m)]

    for j in range(k):
        y, x = map(int, input().split())
        grid[y][x] = 1
    # 세팅 완료


    visited = [[False]*n for _ in range(m)]
    
    
    def bfs(y, x):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited[y][x] = True
        queue = deque()
        queue.append((y, x))

        while queue:
            cur_y, cur_x = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if (0 <= next_x < n) and (0 <= next_y < m):
                    if grid[next_y][next_x] == 1 and not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        queue.append((next_y, next_x))


                        
    num = 0
    for j in range(m):
        for k in range(n):
            if grid[j][k] == 1 and visited[j][k] == False:
                bfs(j, k)
                num += 1

    print(num)