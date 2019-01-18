class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root and not root.left and not root.right:
            return 1

        if root.left and root.right:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            depth = min(left, right)
        else:
            if root.left:
                depth = self.minDepth(root.left)
            else:
                depth = self.minDepth(root.right)
        
        return depth+1