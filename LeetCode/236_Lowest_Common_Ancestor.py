# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # LCA는 최소 공통 조상을 말함
        # LCA(p, q) = 자식노드 p와 q의 가장 가까운 부모 노드

        if root.left == p and root.right == q:
            return root
        

        
        
        


print(Solution.lowestCommonAncestor(root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1))
print(Solution.lowestCommonAncestor(root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4))