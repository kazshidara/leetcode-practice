# 1.  Univalued Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """Return True if Binary tree is univalued - all values are same """
        
        # BASE CASE - means we're at end of tree and no more children to inspect
        if not root:
            return True 

        if root.right:
            if root.right.val != root.val:
                return False

        if root.left:
            if root.left.val != root.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


    
    

################################################################################


