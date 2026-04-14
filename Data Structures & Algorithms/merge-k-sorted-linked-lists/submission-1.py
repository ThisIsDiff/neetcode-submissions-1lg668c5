# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None

        # for node in lists:
        #     res = self.merge2Lists(node,res)
        # return res

        while (len(lists) > 1):
            mergedLS = []

            for i in range(0, len(lists), 2):
                if (len(lists) > (i + 1)):
                    mergedLS.append(self.merge2Lists(lists[i], lists[i+1]))
                else:
                    mergedLS.append(lists[i])
            lists = mergedLS
        return lists[0] if (len(lists)) else None

    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        res = ListNode()
        current = res
        while (list1 and list2):
            if (list1.val < list2.val):
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if (list1):
            current.next = list1
        elif (list2):
            current.next = list2
        return res.next