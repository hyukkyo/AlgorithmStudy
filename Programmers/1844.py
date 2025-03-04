# 최단거리를 구하는 문제
# BFS로 풀어보자
from collections import deque

def solution(maps):
    n = len(maps[0]) # column(세로줄)의 갯수
    m = len(maps) # row(가로줄)의 갯수

    # 주의할 점. 2차원 배열에서는 l[r][c]로 접근하는거다. 세로 -> 가로 순으로.
    visited = [[0]*n for _ in range(m)] # 전부 0으로 초기화
    visited[0][0] = 1 # 시작지점을 1로 초기화

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                continue
            if maps[nr][nc] == 1 and visited[nr][nc] == 0: # 길이 있고, 아직 방문하지 않은 곳일 경우에
                visited[nr][nc] = visited[r][c] + 1 # 해당 경로로 이동하면서 1추가
                q.append((nr, nc))
        
    if visited[m-1][n-1] == 0:
        return -1

    return visited[m-1][n-1]