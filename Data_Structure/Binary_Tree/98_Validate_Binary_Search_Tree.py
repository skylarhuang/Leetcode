# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))
        
    def helper(self, root, lo, hi):
        if not root:
            return True
        if root.val <= lo or root.val >= hi:
            return False
        
        return self.helper(root.left, lo, root.val) and self.helper(root.right, root.val, hi)
        