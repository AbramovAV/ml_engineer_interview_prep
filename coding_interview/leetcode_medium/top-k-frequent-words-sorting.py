class Solution:
    from collections import Counter
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        pairs = [item[::-1] for item in counter.items()]
        pairs.sort(key=lambda x: (-x[0], x[1]))
        return [p[1] for p in pairs[:k]]