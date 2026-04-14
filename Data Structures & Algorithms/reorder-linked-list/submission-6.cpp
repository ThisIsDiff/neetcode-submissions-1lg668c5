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
    void reorderList(ListNode* head) {
        // spliting the list 
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse l2
        ListNode* l2 = slow->next;
        ListNode* previous = nullptr;
        slow->next = nullptr;

        while (l2) {
            ListNode* next = l2->next;
            l2->next = previous;
            previous = l2;
            l2 = next;
        }

        // combine l1 and l2
        ListNode* l1 = head;
        l2 = previous;

        while (l2) {
            ListNode* tmp1 = l1->next;
            ListNode* tmp2 = l2->next;
            l1->next = l2;
            l2->next = tmp1;
            l1 = tmp1;
            l2 = tmp2;
        }
    }
};
