class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagrams = defaultdict(list)
        for string in strs:
            letters = tuple(sorted(list(string)))
            anagrams[letters].append(string)
        
        return list(anagrams.values())