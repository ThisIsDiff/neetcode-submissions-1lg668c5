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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* current = head;
        int index = 0;
        while (current) {
            index++;
            current = current->next;
        }

        if (index == 0) {
            return nullptr;
        } else if (index == n) {
            return head->next;
        }

        current = head;
        for (int i=0; i < (index - n - 1); i++) {
            current = current->next;
        }
        current->next = current->next->next;
        return head;
    }
};
