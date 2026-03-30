from collections import deque

def bfs(start, visited, distance, graph):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

def solution(n, edge):
    # 인접 리스트 만들기
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n+1)
    distance = [0] * (n+1)

    bfs(1, visited, distance, graph)
    return distance.count(max(distance))