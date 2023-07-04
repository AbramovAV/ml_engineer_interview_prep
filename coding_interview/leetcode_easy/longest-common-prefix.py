class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_len = len(min(strs, key=len))
        for i in range(min_len):
            if len(set([s[i] for s in strs])) == 1:
                prefix += strs[0][i]
            else:
                break
        return prefix