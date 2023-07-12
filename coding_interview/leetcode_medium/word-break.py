class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = {"":s}
        while True:
            found = False
            for prefix in list(words.keys()):
                for word in wordDict:
                    if words[prefix].startswith(word):
                        found = True
                        words[prefix + word] = words[prefix][len(word):]
                        if not words[prefix + word]:
                            return True
                del words[prefix]
            if not found:
                return False