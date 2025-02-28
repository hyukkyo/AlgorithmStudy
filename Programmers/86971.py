# dfs로 풀어보자
def dfs(graph, v, visited):
    visited[v] = True
    count = 1

    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)

    return count

def adj_list(max_node, edges):
    graph = [[] for _ in range(max_node + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def solution(n, wires):
    result_list = []

    for i in range(len(wires)):
        remove_wire = wires[i]
        first_node = remove_wire[0]
        second_node = remove_wire[1]
        # print(first_node)
        # print(second_node)

        remain_wires = wires[:i] + wires[i+1:]
        # print(remain_wires)
        remain_graph = adj_list(n, remain_wires) # 간선 리스트 -> 인접 리스트 형태로 변경
        # print(remain_graph)
        first_visited = [False] * (n+1)
        first_nodes = dfs(remain_graph, first_node, first_visited)
        second_visited = [False] * (n+1)
        second_nodes = dfs(remain_graph, second_node, second_visited)

        result_list.append(abs(first_nodes - second_nodes))

    return min(result_list)