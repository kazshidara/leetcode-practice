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

