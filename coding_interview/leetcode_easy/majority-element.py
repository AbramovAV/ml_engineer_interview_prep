class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = 0
        counter = 0
        for num in nums:
            if counter == 0:
                majority_element = num
                counter += 1
            elif majority_element == num:
                counter += 1
            else:
                counter -= 1
        return majority_element