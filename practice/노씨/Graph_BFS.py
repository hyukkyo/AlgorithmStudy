from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]: # 'A'의 BCD를 돌면서
            if v not in visited:
                visited.append(v)
                queue.append(v)

    return visited


graph = {
    'A':['B','C','D'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A'],
}

bfs(graph, 'A')