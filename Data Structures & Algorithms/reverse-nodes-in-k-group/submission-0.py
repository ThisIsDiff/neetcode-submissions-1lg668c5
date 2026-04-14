# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # restrictions 
        # The length of the linked list is n.
        # 1 <= k <= n <= 100
        # 0 <= Node.val <= 100

        if (k == 1): # reverse 1 node is the same as the original list
            return head

        current = head
        size = 0
        while (current):
            size += 1
            current = current.next
        loops = size // k 

        res = None
        current = head
        for _ in range(loops):
            # first round save new head to res for return 
            if (not res):
                res, tail, current = self.reversek(current, k) # dont' need to check tail because it's already done if its None 
            # else keep reversing 
            else:
                head, newtail, current = self.reversek(current, k)
                tail.next = head
                tail = newtail 

        if current:
            tail.next = current
        return res

    def reversek(self, head: Optional[ListNode], k: int): #reverse using pointers
        newtail = head
        current_count = 0
        current = head
        previous = None
        while (current_count < k):
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
            current_count += 1
        newhead = previous
        newstart = nxt 
        return newhead, newtail, newstart