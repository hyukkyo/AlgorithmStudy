from collections import deque

def bfs(root):
    visited = []
    if root is None:
        return 0 # 노드가 없을때
    q = deque() # 큐
    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    return visited

# 이 템플릿은 안보고도 적을 수 있도록 암기하기