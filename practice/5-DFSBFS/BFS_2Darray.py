# 그래프가 2차원 리스트의 경우, BFS 템플릿

from collections import deque

def bfs(graph, start_r, start_c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    q.append((start_r, start_c))
    visited = set()
    visited.add((start_r, start_c))

    while q:
        r, c = q.popleft()

        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]

            if 0 <= next_r < len(graph) and 0 <= next_c < len(graph[0]):
                if (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    q.append((next_r, next_c))

    return -1

def solution():
    graph = [
        ['O', 'O', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O', 'O', 'O'],
    ]