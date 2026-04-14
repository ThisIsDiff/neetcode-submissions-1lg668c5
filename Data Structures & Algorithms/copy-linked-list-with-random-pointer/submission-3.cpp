/*
// Definition for a Node.
class Node {
public:
    int val;
    Node*->next;
    Node* random;
    
    Node(int _val) {
        val = _val;
    ->next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* current = head;
        Node* copy = new Node(0);
        Node* incopy = copy;

        while (current) {
            Node* newnode = new Node(current->val);
            incopy->next = newnode;

            newnode->random = current->random;
            current->random = newnode;

            incopy = incopy->next; // incopy = newnode, same but incopy->next is easier to read and understand
            current = current->next;
        }


        incopy = copy->next;
        while (incopy) {
            if (incopy->random) {
                incopy->random = incopy->random->random;
            }
            incopy = incopy->next;
        }

        return copy->next;
    }
};
