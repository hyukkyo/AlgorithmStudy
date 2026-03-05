from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

# 입력부
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 변수 초기화
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y, size = 0, 0, 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            # 상어의 처음 위치
            x, y = i, j

def find_fish_with_bfs(x, y, size):
    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1

    queue = deque()
    queue.append((x, y))

    fish_list = []
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] <= size:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        fish_list.append((nx, ny, distance[nx][ny]))

    if not fish_list:
        return None
    return min(fish_list, key=lambda x: (x[2], x[0], x[1]))

count = 0
time = 0

while True:
    # bfs로 먹을 물고기 1마리(최우선) 찾기
    target = find_fish_with_bfs(x, y, size)

    # 먹을 물고기 없으면 종료
    if target is None:
        break

    nx, ny, dist = target

    # 이동 시간 누적 + 위치 갱신
    time += dist
    graph[x][y] = 0
    graph[nx][ny] = 0
    x, y = nx, ny

    # 먹은 횟수/성장 처리
    count += 1
    if count == size:
        size += 1
        count = 0

print(time)