# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [root]
        nextlevel_, nextlevel = -1, []
        res_, res = [], []
        
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
                if nextlevel_ == -1:
                    res.append(res_)
                else:
                    res.append(res_[::-1])
                q = nextlevel
                nextlevel, res_ = [], []
                nextlevel_ = nextlevel_ * -1
        
        return res