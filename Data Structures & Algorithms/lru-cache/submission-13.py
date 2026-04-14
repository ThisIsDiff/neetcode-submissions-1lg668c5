class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.p = None
        self.n = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.mostRec = None
        self.leastRec = None

    def get(self, key: int) -> int:
        if (key in self.hashmap.keys()):
            node = self.hashmap.get(key)
            #update position
            self.update_position(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        
        #update value if key exist
        if (key in self.hashmap.keys()):
            #update value
            node = self.hashmap.get(key)
            node.value = value
            self.update_position(self.hashmap.get(key))

        #add key-value pair to the cache
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.update_position(node)
            #remove the least recent if it more than capacity
            if (self.capacity < len(self.hashmap)):
                self.rm_leastRec()
        
        return

    def update_position(self, node: Node) -> None: # updates position of existing node
        # empty hash
        # node in front
        # node in back
        # node in between 

        # empty hash
        if (not self.mostRec):
            self.mostRec = node
            self.leastRec = node
            return
        
        # node in front - no need to update position since we want it in the front anyways
        if (self.mostRec == node):
            return 

        # node in back - there's no need to worry about if the node -
        # is in the front and back b/c we check if it's front first if 
        # it is then it should do nothing and just return
        if (self.leastRec == node):
            self.leastRec = self.leastRec.n
            self.leastRec.p = None # set previous to None to previous connection issues and unused nodes 
            self.set_front(node) # saves leastrec and traverse the list to the next least recent node 
            return
        
        # node in between - mending the gap went move from the middle of the cache to the front 
        if (node.p):
            node.p.n = node.n
        if (node.n):
            node.n.p = node.p
        self.set_front(node)
        return


    def set_front(self, node: Node) -> None: # helper function to move node to the front of the hashmap
        self.mostRec.n = node
        node.p = self.mostRec # moved the least recent to most recent n = None, and p is the old most recent 
        node.n = None
        self.mostRec = node
        return

    def rm_leastRec(self) -> None:
        tmp = self.leastRec
        del self.hashmap[tmp.key]
        self.leastRec = self.leastRec.n
        tmp.n = None
        self.leastRec.p = None
        return