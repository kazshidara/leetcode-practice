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


# 2. Merge Two Binary Trees

# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:

# Input: 
#     Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
#          3
#         / \
#        4   5
#       / \   \ 
#.     5   4   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 and t2:
            
            root = TreeNode(t1.val + t2.val)    #creating a new node (of merged tree) that's sum of values 
            root.right = self.mergeTrees(t1.right, t2.right)    #run function for the right node 
            root.left = self.mergeTrees(t1.left, t2.left)       # run function for left node
            return root                                         #return the final merged tree at end 
        else:
            return t1 or t2

################################################################################

# 3. Find the maximum depth of a tree (how many levels it has)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))



################################################################################


# 4. Inverting a binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
                
        return root

################################################################################


# 5. No Prefix Set -- implementing a Trie 

def no_prefix(words):

    data = {}
    done = False

    for word in words:
        if done:
            break
        current = data
        print("current = data:",current)
        for i, char in enumerate(word):
            if char in current.keys():
                if current[char] == 0 or i== len(word)-1:
                    print("BAD SET")
                    print(word)
                    done = True
                    break
                else:
                    current = current[char]
                    print("current, inspecting keys: ", current)
            else:
                if i == len(word) - 1:
                    current[char] = 0
                else:
                    current[char] = {}
                    print("current:", current)
                    current = current[char]
                    print("current = current[char]:", current)

    if not done:
        print("GOOD SET")

# bad set:
# print(no_prefix(['aab','aac','aacghgh','aabghgh']))   

# good set:
# print(no_prefix(['aab','defgab','abcde','cedaaa', 'bbbbbbbb', 'jabjjjad']))



################################################################################


