# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 = l1
        p2 = l2
        res = ListNode()
        current = res
        while (p1 or p2 or carry):
            # if (p1 and p2):
            #     tmp = p1.val + p2.val
            #     p1 = p1.next
            #     p2 = p2.next
            # elif (p1):
            #     tmp = p1.val
            #     p1 = p1.next
            # else:
            #     tmp = p2.val
            #     p2 = p2.next

            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            tmp = val1 + val2 + carry

            carry = tmp // 10
            node = ListNode(tmp%10)
            current.next = node
            current = current.next

        return res.next

            