/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node copy = new Node(0);
        Node indexedcopy = copy;
        Node current = head;
        while (current != null) {
            Node newnode = new Node(current.val);
            indexedcopy.next = newnode;

            newnode.random = current.random;
            current.random = newnode;

            indexedcopy = newnode;
            current = current.next;
        }

        indexedcopy = copy.next;
        while (indexedcopy != null) {
            if (indexedcopy.random != null) {
                indexedcopy.random = indexedcopy.random.random;
            }
            indexedcopy = indexedcopy.next;
        }

        return copy.next;
    }
}

/*
use new node as place holder for the values and then actually copying it 

newnode.val = val
newnode.next = newly created node 
newnode.random = random

node.val = val 
node.next = next 
node.random = newnode
*/
