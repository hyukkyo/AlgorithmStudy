import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())

a = []
for _ in range(n):
    column = list(map(int, input().split()))
    a.append(column)

def isBetween(num1, num2):
    return (l <= abs(num1-num2) <= r)



def bfs(x,y, visited):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    queue = deque()
    queue.append((x,y))

    union = []
    union.append((x,y))

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if (0 <= next_x < n) and (0 <= next_y < n) and visited[next_x][next_y] == False:
                if isBetween(a[cur_x][cur_y], a[next_x][next_y]):
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    union.append((next_x, next_y))
    return union

day = 0
while True:
    CanMove = False
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                union = bfs(i, j, visited)

                if len(union) > 1: # 인구이동이 있었다면
                    CanMove = True

                    avg = sum([a[x][y] for x, y in union]) // len(union)
                    for x,y in union:
                        a[x][y] = avg
                    

    if CanMove == False:
        break
    day += 1

print(day)