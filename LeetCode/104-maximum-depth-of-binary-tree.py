from collections import deque

# level order (BFS)로 풀어보자
# def maxDepth(root):
#     max_depth = 0

#     visited = []
#     q = deque()

#     if root == None:
#         return 0
    
#     q.append((root, 1))

#     while q:
#         current_node, current_depth = q.popleft()
#         max_depth = max(current_depth, max_depth)

#         if current_node.left:
#             q.append((current_node.left, current_depth+1))
#         if current_node.right: 
#             q.append((current_node.right, current_depth+1))

#     return max_depth


# postorder로도 풀수있음.
        
def maxDepth(root):
    max_depth = 0
    if root == None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    max_depth = max(left_depth, right_depth) + 1

    return max_depth


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(val=3)
root.left = TreeNode(val=9)
root.right = TreeNode(val=20)
root.right.left = TreeNode(val=15)
root.right.right = TreeNode(val=7)

print(maxDepth(root))