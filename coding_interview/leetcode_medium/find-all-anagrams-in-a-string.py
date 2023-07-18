class Solution:
    from collections import Counter
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = dict.fromkeys(s, 0)
        indices = []
        len_p = len(p)
        p_counter = dict.fromkeys(s+p, 0)
        for char in p:
            p_counter[char] += 1
        for i in range(len(s)-len_p+1):
            if i==0:
                for char in s[i:i+len_p]:
                    counter[char] += 1
            else:
                counter[s[i-1]] -= 1
                counter[s[i+len_p-1]] += 1
            if p_counter == counter:
                indices.append(i)
        return indices