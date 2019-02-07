	    def lowestCommonAncestor(self, root, p, q):
	        if not root:
	            return None
	        if root == q or root == p:
	            return root
	        
	        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
	        
	        if left and right:
	            return root
	        # If not left or not right, then p and q are not in the same tree
	        if left and not right:
	            return left
	        if right and not left:
            return right