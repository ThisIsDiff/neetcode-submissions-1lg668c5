# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        current = head
        while (current):
            size += 1
            current = current.next

        if size == 1:
            return None
    
        index = size - n
        prev = None
        current = head
        for _ in range(index):
            prev = current
            current = current.next
        
        if prev:
            prev.next = current.next
            return head
        else:
            return current.next

# [1]
# size = 1
# n = 1 
# loops 1 time