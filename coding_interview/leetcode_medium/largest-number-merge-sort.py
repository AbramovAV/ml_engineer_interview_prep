class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = self.merge_sort([str(num) for num in nums])
        if all([x=="0" for x in nums]):
            return "0"
        else:
            return "".join(nums)

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        left = self.merge_sort(nums[:len(nums)//2])
        right = self.merge_sort(nums[len(nums)//2:])
        merged = []
        left_idx = 0
        right_idx = 0
        while left_idx<len(left) and right_idx<len(right):
            first_op = left[left_idx] + right[right_idx]
            second_op = right[right_idx] + left[left_idx]
            if first_op > second_op:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        
        if left_idx<len(left):
            merged.extend(left[left_idx:])
        elif right_idx<len(right):
            merged.extend(right[right_idx:])
        return merged