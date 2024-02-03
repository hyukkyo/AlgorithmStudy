graph = {
    'A':['B','C','D'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A'],
}

# 매개변수가 많아서 visited는 걍 밖으로 빼줌
visited = []

def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)

dfs('A')