# 재귀로 구현하는 DFS
def dfs(cur_node):
    if cur_node is None:
        return
    dfs(cur_node.left)
    dfs(cur_node.right)
dfs(root)

# # 전위순회 preorder
# def preorder(cur_node):
#     if cur_node is None:
#         return
    
#     print(cur_node.value)
#     preorder(cur_node.left)
#     preorder(cur_node.right)
# preorder(root)

# # 중위순회 inorder
# def inorder(cur_node):
#     if cur_node is None:
#         return
    
#     inorder(cur_node.left)
#     print(cur_node.value)
#     inorder(cur_node.right)
# inorder(root)

# # 후위순회 postorder
# def postorder(cur_node):
#     if cur_node is None:
#         return
    
#     postorder(cur_node.left)
#     postorder(cur_node.right)
#     print(cur_node.value)
# postorder(root)