class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        left_, right_ = self.getHeight(root.left), self.getHeight(root.right)
        left,  right= self.isBalanced(root.left), self.isBalanced(root.right)

        # Have to return left&right&abs, because if left or right is determined as imbalanced
        # The result may not be pass to root, but root is balanced.
        # [1,2,2,3,null,null,4,null,null,4]
        return left and right and abs(left_-right_)<2

    
    def getHeight(self, root):
        if not root: return 0
        left, right = self.getHeight(root.left), self.getHeight(root.right)
        return max(left, right)+1