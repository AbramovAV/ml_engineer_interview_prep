class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_symbols = set()
        symbols = []
        max_len = 0
        for symbol in s:
            while symbol in unique_symbols:
                unique_symbols.remove(symbols.pop(0))
            symbols.append(symbol)
            unique_symbols.add(symbol)
            max_len = max(max_len, len(unique_symbols))
        return max_len