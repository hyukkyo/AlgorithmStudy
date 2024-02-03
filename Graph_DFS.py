


graph = {
    'A':['B','C','D'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A'],
}

dfs(graph, 'A')