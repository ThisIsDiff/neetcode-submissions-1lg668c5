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
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next!=null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}

/*
leetcode 141 solution
time: O(n)
space: O(1)

Explanation:
    * here we're using the slow and fast method such that slow goes in 1 by 1 pace and fast is 2 times as fast as slow
    * such that if there's a loop there's a 100% chance of the fast looping back and get up to where slow is
    * so all we need to do is to check if the node at fast and slow are the same, return true for loop if there is 
    * if there's no loop then fast will hit an empty/null node first, at this point we return false for no loop 

1) initialize slow and fast at head
2) in the while loop if fast and fast.next exist continue
3) slow move to next and fast move to next next
4) if slow and fast is equal return true, there's loop
5) while loops end meaning no loop, return false
*/
