class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        ransomNoteDict = defaultdict(int)
        magazineDict = defaultdict(int)

        for char in ransomNote:
            ransomNoteDict[char] += 1
        for char in magazine:
            magazineDict[char] += 1
        
        if set(ransomNoteDict.keys()).issubset(set(magazineDict.keys())):
            for char, count in ransomNoteDict.items():
                if magazineDict[char] < ransomNoteDict[char]:
                    return False
            return True
        return False