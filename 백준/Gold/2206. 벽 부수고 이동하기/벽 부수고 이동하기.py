from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = []
for i in range(n):
    row = list(map(int, input()))
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3차원 행렬. z, y, x 순으로 선언한다.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
# z좌표가 0인 2차원 배열은 안부순 , 1은 부순 경로

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()

        # 맨 끝에 도달하면 return
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            # 범위 밖으로 나가면 스킵
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 다음 좌표가 벽이고, 기존 좌표가 안부순 벽이라면
            if graph[nx][ny] == 1 and c == 0:
                # 부순 경로를 만들어서 기존 좌표 값 + 1
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1)) # 벽을 부순 이후의 케이스

            # 다음 좌표가 벽이 아니고, 방문을 아직 안했으면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1 # 자연스럽게 경로 이동
                queue.append((nx, ny, c))
    
    return -1

print(bfs(0, 0, 0))
