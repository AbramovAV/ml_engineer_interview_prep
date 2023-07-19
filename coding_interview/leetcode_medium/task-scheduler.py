class Solution:
    from collections import Counter
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [[-count, word] for (word, count) in counter.items()]
        heapq.heapify(heap)
        total_time = 0
        while heap:
            k_most_freq = []
            for i in range(min(n+1,len(heap))):
                k_most_freq.append(heapq.heappop(heap))
            for k in k_most_freq:
                if k[0] < -1:
                    k[0] += 1
                    heapq.heappush(heap, k)
            
            if len(heap) > 0:
                total_time += (n + 1)
            else:
                total_time += len(k_most_freq)
        return total_time