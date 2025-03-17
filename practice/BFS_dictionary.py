# 그래프가 딕셔너리 형태일때의 BFS 템플릿

from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start]) # set을 사용한다

    while q:
        v = q.popleft()

        # if v == 'T': # 종료조건이 있다면 여기서 다룬다
        #     return v

        for neighbor in graph[v]:
            if neighbor not in visited:
                # if neighbor != 'X': # 추가 이동조건이 있다면 여기서 다룬다
                visited.add(neighbor)
                q.append(neighbor)

    return -1

def solution():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }