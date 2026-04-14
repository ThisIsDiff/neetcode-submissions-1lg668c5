public class Node {
    int key;
    int value;
    Node next;
    Node prev;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}


class LRUCache {

    private int capacity;
    private Node least;
    private Node most;
    private HashMap<Integer, Node> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.least = new Node(0, 0);
        this.most = new Node(0, 0);
        this.most.prev = this.least;
        this.least.next =  this.most;
        this.cache = new HashMap<>();
    }

    private void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
        return;
    }

    private void insert(Node node) {
        Node dumpy_most = this.most;
        Node second_most = this.most.prev;

        node.next = dumpy_most;
        node.prev = second_most;

        dumpy_most.prev = node;
        second_most.next = node;
        return;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            remove(cache.get(key));
        }

        Node newnode = new Node(key, value);
        cache.put(key, newnode);
        insert(newnode);

        if (cache.size() > capacity) {
            Node lru = least.next;
            cache.remove(lru.key); // remove from hashmap 
            remove(lru); // remove from linked list
        }
        return;
    }
}
