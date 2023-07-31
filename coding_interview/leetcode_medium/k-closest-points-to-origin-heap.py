class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #building heap
        for i in range(len(points)//2, -1, -1):
            points = self.heapify(points, i)
        #pyramidal sorting
        for i in range(1, len(points) + 1):
            points[-i], points[0] = points[0], points[-i]
            points[:-i] = self.heapify(points[:-i], 0)
        return points[:k]

    def dist(self, point):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5

    def heapify(self, heap, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        largest_idx = idx
        if right_idx < len(heap) and self.dist(heap[right_idx]) > self.dist(heap[largest_idx]):
            largest_idx = right_idx
        if left_idx < len(heap) and self.dist(heap[left_idx]) > self.dist(heap[largest_idx]):
            largest_idx = left_idx
        if largest_idx != idx:
            heap[largest_idx], heap[idx] = heap[idx], heap[largest_idx]
            self.heapify(heap, largest_idx)
        return heap