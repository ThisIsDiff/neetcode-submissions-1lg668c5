# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevnode = None
        currnode = head
        while currnode:
            nextnode = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = nextnode
        return prevnode

"""
nod1 val1, nod2
nod2 val2, nod3
nod3 val3, None

to do 
* next node.next = current node
* current.next = None
"""
        