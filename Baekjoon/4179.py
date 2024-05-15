import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

maze = []
maze_j = []
maze_f = []
for i in range(r):
    column = input().rstrip()
    for j in range(c):
        if column[j] == 'J':
            maze_j.append((i, j))
        elif column[j] == 'F':
            maze_f.append((i, j))
    maze.append(column)

# print(maze)
# print(maze_j)
# print(maze_f)

queue = deque()
queue.append((maze_j[0][0], maze_j[0][1], 'J')) # 사람의 현재좌표를 큐에 입력
maze[maze_j[0][0]][maze_j[0][1]] = 0 # 사람의 현재좌표를 0으로 변경

# if len(maze_f) != 0:
#     for (r, c) in maze_f:


# def bfs():
#     dx = [1,-1,0,0] 
#     dy = [0,0,1,-1]

#     while queue:
#         cx, cy = queue.popleft()
#         check_space(cx, cy)

#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
#             if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
#                 pass


# time = 0
# while True:
#     canMove = False

#     visited = [[False]*c for _ in range(r)]

#     for i in range(r):
#         for j in range(c):
#             if maze[i][j] == '#':
#                 visited[i][j] = True
#             elif maze[i][j] == 'J':
                
#             elif maze[i][j] == 'F':
                
#             if visited[i][j] == False:
#                 visited = True
#                 bfs(i, j, visited)

#     if not canMove:
#         break
#     time += 1

# print(time)