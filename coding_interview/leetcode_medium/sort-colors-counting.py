class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {
            0:0,
            1:0,
            2:0
        }
        for i in nums:
            counter[i] += 1
        
        cur_pos = 0
        for key in counter:
            for _ in range(counter[key]):
                nums[cur_pos] = key
                cur_pos += 1