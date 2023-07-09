class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            k = len(nums)-1
            j = i+1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum>0:
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
        return triplets