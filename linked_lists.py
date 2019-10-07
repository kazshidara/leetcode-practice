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

#3.  Circular Linked Lists



