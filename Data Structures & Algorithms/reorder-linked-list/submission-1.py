# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # #gets the size of the linkedlist
        # current = head
        # half = 0
        # while (current):
        #     half += 1
        #     current = current.next
        
        # #separates the seconde half of the list such that list2 is the second half and the first half is cut off by setting the last node of the first half to None
        # half = math.ceil(half/2)
        # current = head
        # for i in range(half-1):
        #     current = current.next

        # list2 = current.next
        # current.next = None

        slow = fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        #now previous is the second half of the initial list in reverse
        previous = None
        list2curr = slow.next
        slow.next = None
        while(list2curr):
            nextnode = list2curr.next
            list2curr.next = previous
            previous = list2curr
            list2curr = nextnode

        #merging 2 halfs of the list 
        islist1 = False
        current = head
        list1 = head.next
        list2 = previous
        while (list1 and list2):
            if islist1:
                current.next = list1
                list1 = list1.next
                islist1 = False
            else:
                current.next = list2
                list2 = list2.next
                islist1 = True
            current = current.next

        current.next = list1 if list1 else list2

