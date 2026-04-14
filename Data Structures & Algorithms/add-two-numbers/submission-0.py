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
        index = res
        while (p1 or p2):
            if (p1 and p2):
                tmp = p1.val + p2.val
                p1 = p1.next
                p2 = p2.next
            elif (p1):
                tmp = p1.val
                p1 = p1.next
            else:
                tmp = p2.val
                p2 = p2.next

            tmp += carry;
            carry = tmp // 10
            node = ListNode(tmp%10)
            index.next = node
            index = index.next

        if (carry):
            index.next = ListNode(carry)

        return res.next

            