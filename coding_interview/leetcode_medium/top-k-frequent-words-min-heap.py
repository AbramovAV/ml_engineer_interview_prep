class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        cntr = Counter(words)
        for word, count in cntr.items():
            heapq.heappush(heap, (count, word))
        k_words = [pair[1] for pair in heapq.nsmallest(k, heap, key=lambda x: (-x[0], x[1]))]
        return k_words