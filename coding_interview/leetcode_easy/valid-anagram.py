class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_mapping = {}
        for char in s:
            if char not in char_mapping:
                char_mapping[char] = 0
            char_mapping[char] += 1
        
        for char in t:
            if char not in char_mapping:
                char_mapping[char] = 0
            char_mapping[char] -= 1
        
        if any(char_mapping.values()):
            return False
        return True