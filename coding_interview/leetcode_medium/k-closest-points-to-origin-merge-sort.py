class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 1:
            return points
        else:
            left_points = self.kClosest(points[:len(points)//2], k)
            right_points = self.kClosest(points[len(points)//2:], k)
            merged = []
            while left_points and right_points:
                if self.dist(left_points[0]) <= self.dist(right_points[0]):
                    merged.append(left_points.pop(0))
                else:
                    merged.append(right_points.pop(0))
            merged.extend(left_points)
            merged.extend(right_points)
            return merged[:k]


    def dist(self, point):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5

    def heapify(self, heap, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        smallest_idx = idx
        if right_idx < len(heap) and self.dist(heap[right_idx]) < self.dist(heap[smallest_idx]):
            smallest_idx = right_idx
        if left_idx < len(heap) and self.dist(heap[left_idx]) < self.dist(heap[smallest_idx]):
            smallest_idx = left_idx
        if smallest_idx != idx:
            heap[smallest_idx], heap[idx] = heap[idx], heap[smallest_idx]
            self.heapify(heap, smallest_idx)
        return heap
        

    