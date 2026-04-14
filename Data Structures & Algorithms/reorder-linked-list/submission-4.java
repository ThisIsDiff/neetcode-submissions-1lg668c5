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
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        // fast reaches the end first 
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // reverse the second half of the list 
        ListNode l2 = slow.next;
        ListNode previous = null;
        slow.next = null; // cut off the half 

        while(l2 != null) {
            ListNode next = l2.next;
            l2.next = previous;
            previous =  l2;
            l2 = next;
        }
        l2 = previous;

        while (l2 != null ) {
            ListNode l1temp = head.next;
            ListNode l2temp = l2.next;
            head.next = l2;
            head.next.next = l1temp;
            head = l1temp;
            l2 = l2temp;
        }
    }
}
