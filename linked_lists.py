# 1.  Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None         # prev is None at first 
        curr = head         # start at head

        while curr:
            next = curr.next
            curr.next = prev       #switches direction of pointer
            prev = curr 
            curr = next 
        return prev


    
    

################################################################################

#2.   Find Intersection of 2 Linked Lists 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Have two pointers that move on to the next node with each loop

        A = headA
        B = headB
        
        # Keeps looping until the pointers reach the same node or NONE (end of LL)
        while A != B:
            if A is not None:
                A = A.next
            else:               # If pointer A reaches end of LL-A, it points to head of LL-B
                A = headB
            if B is not None:
                B = B.next
            else:               # Pointers switch head and iterate a second time 
                B = headA 
        return A

################################################################################

#3.  Linked List Cycle 

# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
            # b/c pointers are 2 positions apart, if the linked list is cyclic, both pointers will meet 
            if slow == fast:
                return True   

        return False 

################################################################################

#3.  Merge 2 sorted Linked Lists into a new one

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        head = sort_list = ListNode(0)
        
        while(l1 and l2):
            
            if l1.val < l2.val:
                sort_list.next = l1
                l1 = l1.next
                sort_list = sort_list.next
                
            elif l1.val >= l2.val:
                sort_list.next = l2
                l2 = l2.next
                sort_list = sort_list.next

        sort_list.next = l1 or l2
        return head.next


################################################################################

#4.  Convert sorted linked list to Binary Search Tree

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode):

        array = []

        while head:
            array.append(head.val)
            head = head.next 

        def build_tree(array):

            mid = (len(array))/2

            root = TreeNode(array[mid])

            root.left = build_tree(array[:mid])
            root.right = build_tree(array[mid + 1:])
            
            return root 

        return build_tree(array)


