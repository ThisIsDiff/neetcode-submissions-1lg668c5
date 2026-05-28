class PrefixTree:

    def __init__(self):
        self.wordList = set()


    def insert(self, word: str) -> None:
        self.wordList.add(word)
        # for i in range(1, len(word)-1):
        #     self.prefix.add(word[0:i])


    def search(self, word: str) -> bool:
        return word in self.wordList

    def startsWith(self, prefix: str) -> bool:
        for word in self.wordList:
            if prefix == word[:len(prefix)]:
                return True
        return False
        