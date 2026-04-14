/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        ListNode* res = new ListNode();
        ListNode* current = res;

        while (p1 || p2 || carry) {
            int val1 = (p1)? p1->val:0;
            int val2 = (p2)? p2->val:0;
            p1 = (p1)? p1->next: nullptr;
            p2 = (p2)? p2->next: nullptr;

            int total = val1 + val2 + carry;

            carry = total/10;
            ListNode* newnode = new ListNode(total%10);
            current->next = newnode;
            current = current->next;
        }
        return res->next;
    }
};
