class Trie:
    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        ptr = self.data
        for i in range(len(word)):
            if word[i] not in ptr:
                ptr[word[i]] = {}
            ptr = ptr[word[i]]
            if i == len(word) - 1:
                ptr["is_word"] = True

    def search(self, word: str) -> bool:
        ptr = self.data
        for i in range(len(word)):
            if word[i] not in ptr or \
            (i==len(word)-1 and "is_word" not in ptr[word[i]]):
                return False
            ptr = ptr[word[i]]
        return True

    def startsWith(self, prefix: str) -> bool:
        ptr = self.data
        for i in range(len(prefix)):
            if prefix[i] not in ptr:
                return False
            ptr = ptr[prefix[i]]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)