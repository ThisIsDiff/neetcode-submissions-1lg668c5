# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if (list1 and list2 and list1.val <= list2.val):
            current = list1
            p1 = p1.next
            head = list1
        elif (not list1) and  (list2):
            return list2
        elif (not list2) and list1:
            return list1
        elif (list1 and list2 and list1.val > list2.val):
            head = list2 
            current = list2
            p2 = p2.next
        else:
            return None
    
        while (p1 or p2):
            if (p1 and p2 and p1.val <= p2.val):
                current.next = p1
                p1 = p1.next
            elif (not p1) and p2:
                current.next = p2
                break
            elif (not p2) and p1:
                current.next = p1
                break
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        return head 

"""
return
    * list1 if (list1 and list2 and list1.val >= list2.val) or list1
    * else list2 
"""