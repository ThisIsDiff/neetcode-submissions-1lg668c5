class Node {
public:
    int key;
    int value;
    Node* next;
    Node* prev;
    Node(int key, int value): 
        key(key),
        value(value),
        next(nullptr),
        prev(nullptr) {}
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> cache;
    Node* most;
    Node* least;

    void remove(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;
        
        prev->next = next;
        next->prev = prev;
    }

    void insert(Node* node) {
        Node* prev = most->prev;

        prev->next = node;
        node->prev = prev;
        node->next = most;
        most->prev = node;
    }

public:
    LRUCache(int capacity){
        this->capacity = capacity;
        this->most = new Node(0, 0);
        this->least = new Node(0, 0); 
        cache.clear();
        most->prev = least;
        least->next = most;
    }
    
    int get(int key) {
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];
            remove(node);
            insert(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node* oldnode = cache[key];
            remove(oldnode);
            delete(oldnode);
        }

        Node* newnode = new Node(key, value);
        insert(newnode);
        cache[key] = newnode;

        if (cache.size() > capacity) {
            Node* lru = least->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }
        return;
    }
};
