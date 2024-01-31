from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# level order (BFS)로 풀어보자
class Solution(object):
    def maxDepth(self, root):
        depth = 0

        visited = []
        q = deque()

        if root == None:
            return 0
        
        q.append(root)

        while q:
            current_node = q.popleft()
            visited.append = current_node.val

            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

        return depth