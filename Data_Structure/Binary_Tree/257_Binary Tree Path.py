	def binaryTreePaths(root):
	  if not root:
	    return []
	  elif not root.left and not root.right:
	    return [str(root.val)]
	  else:
	    res = binaryTreePaths(root.left) + binaryTreePaths(root.right)
	    for i, v in enumerate(res):
	      res[i] = str(root.val) + "->" + str(v)
  return res