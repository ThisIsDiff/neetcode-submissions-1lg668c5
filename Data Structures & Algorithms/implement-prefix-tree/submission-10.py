class PrefixTree:

    wordList = None

    def __init__(self):
        self.prefix = set()
        self.wordList = set()
        return


    def insert(self, word: str) -> None:
        self.wordList.add(word)
        # for i in range(1, len(word)-1):
        #     self.prefix.add(word[0:i])
        return


    def search(self, word: str) -> bool:
        if word in self.wordList:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.wordList:
            if prefix == word[:len(prefix)]:
                return True
        return False
        