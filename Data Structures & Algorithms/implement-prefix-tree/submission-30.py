class trieNode:
    def __init__(self):
        self.children = {}
        self.isLastc = False

class PrefixTree:

    def __init__(self):
        self.root = trieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if not cur.children.get(c):
                cur.children[c] = trieNode()
            cur = cur.children[c]
        cur.isLastc = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                return False
            cur = cur.children[c]
        return cur.isLastc
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.children.get(c):
                return False
            cur = cur.children[c]
        return True 
        