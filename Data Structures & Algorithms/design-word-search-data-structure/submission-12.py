class wordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.dictionary = wordNode()

    def addWord(self, word: str) -> None:
        cur = self.dictionary

        for c in word:
            if c not in cur.children:
                cur.children[c] = wordNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i >= len(word):
                return node.isEnd
            if not node.children:
                return False

            indicator = False
            if word[i] == '.':
                for c , c_node in node.children.items():
                    indicator = indicator or dfs(i + 1, c_node)
                return indicator 
            elif word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])
            else:
                return False

        return dfs(0, self.dictionary)

