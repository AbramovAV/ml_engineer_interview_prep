class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]
        self.nums = nums
        return self.quickselect(0, len(nums), k-1)
        
    def partition(self, left, right, pivot):
        value = self.nums[pivot]
        self.nums[pivot], self.nums[right-1] = self.nums[right-1], self.nums[pivot]
        idx = left
        for i in range(left, right-1):
            if self.nums[i] > value:
                self.nums[idx], self.nums[i] = self.nums[i], self.nums[idx]
                idx += 1
        self.nums[right-1], self.nums[idx] = self.nums[idx], self.nums[right-1]
        return idx

    def quickselect(self, left, right, k):
        if left == right:
            return self.nums[left]
        pivot = self.partition(left, right, (left+right)//2)
        if pivot == k:
            return self.nums[pivot]
        elif pivot > k:
            return self.quickselect(left, pivot, k)
        else:
            return self.quickselect(pivot+1, right, k)