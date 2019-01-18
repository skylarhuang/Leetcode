# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [root]
        nextlevel = []
        res, res_ = [], []
        
        while q:
            head = q.pop(0)

            if not head:
                return []

            res_.append(head.val)
            if head.left:
                nextlevel.append(head.left)
            if head.right:
                nextlevel.append(head.right)
            
            if not q:
                res.append(res_)
                q = nextlevel
                nextlevel, res_ = [], []
                
        return res