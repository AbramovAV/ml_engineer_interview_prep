class WordDictionary:
    from collections import deque
    def __init__(self):
        self.data = {}
        self.cur_idx = 0

    def addWord(self, word: str) -> None:
        ptr = self.data
        for i in range(len(word)):
            if word[i] not in ptr:
                ptr[word[i]] = [None, {}]
            if i == len(word)-1:
                ptr[word[i]][0] = self.cur_idx
                self.cur_idx += 1
            ptr = ptr[word[i]][1]

    def search(self, word: str) -> bool:
        stack = deque([(self.data, 0, word[0])])
        while stack:
            ptr, idx, char = stack.pop()
            if char in ptr:
                if idx == len(word)-1:
                    if ptr[char][0] is not None:
                        return True
                else:
                    stack.append((ptr[char][1], idx+1, word[idx+1]))
            elif char == ".":
                for key in ptr:
                    stack.append((ptr, idx, key))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)