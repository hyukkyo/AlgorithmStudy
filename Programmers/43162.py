def dfs(graph, v, visited):
    visited[v] = True
    count = 1

    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    return count

def solution(n, computers):
    # computers는 인접행렬 형식
    # 인접행렬 형식을 인접리스트 형식으로 변환해준다
    adj_list = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                adj_list[i+1].append(j+1)
                adj_list[j+1].append(i+1)
    # print(adj_list)

    components = []
    visited = [False] * (n+1)
    for node in range(1, n+1):
        if not visited[node]:
            size = dfs(adj_list, node, visited)
            components.append(size)
    
    answer = len(components)
    return answer