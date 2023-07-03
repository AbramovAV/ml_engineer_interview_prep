class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        chars = Counter(s)
        
        max_odd = max(filter(lambda x: x%2, chars.values()), default=0)
        palindrome_len = sum(filter(lambda x: not x%2, chars.values()))
        
        for count in chars.values():
            if count % 2 == 1 and count <= max_odd:
                palindrome_len += (count-1)

        if max_odd:
            palindrome_len += 1
        return palindrome_len