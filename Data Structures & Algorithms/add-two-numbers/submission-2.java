/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode res = new ListNode();
        ListNode current = res;
        while (p1 != null || p2 != null || carry != 0) {
            int val1 = (p1 != null)? p1.val : 0;
            int val2 = (p2 != null)? p2.val : 0;
            p1 = (p1 != null)? p1.next : null;
            p2 = (p2 != null)? p2.next : null;

            int total = val1 + val2 + carry;

            carry = total/10;
            ListNode newnode = new ListNode(total%10);
            current.next = newnode;
            current = current.next;
        }

        return res.next;
    }
}
