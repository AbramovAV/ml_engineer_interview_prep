class Solution:
    def longestPalindrome(self, s: str) -> str:
        from collections import deque
        s_len = len(s)
        palindromes = deque([(idx, idx+1) for idx in range(s_len)])
        longest = s[0]
        max_len = 1
        while palindromes:
            start, end = palindromes.pop()
            if (end-start) > max_len:
                longest = s[start:end]
                max_len = len(longest)
            if end-start == 1:
                if end<s_len and s[start]==s[end]:
                    palindromes.append((start, end+1))
                elif start > 0 and s[start-1]==s[start]:
                    palindromes.append((start-1, start))
            if start>0 and end < s_len and s[start-1]==s[end]:
                palindromes.append((start-1, end+1))

        return longest