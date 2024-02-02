from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# level order (BFS)로 풀어보자
# class Solution(object):
#     def maxDepth(self, root):
#         max_depth = 0

#         visited = []
#         q = deque()

#         if root == None:
#             return 0
        
#         q.append((root, 1))

#         while q:
#             current_node, current_depth = q.popleft()
#             visited.append = current_node.val
#             max_depth = max(current_depth, max_depth)

#             if current_node.left:
#                 q.append((current_node.left, current_depth+1))
#             if current_node.right: 
#                 q.append((current_node.right, current_depth+1))

#         return max_depth
    
# postorder로도 풀수있음.