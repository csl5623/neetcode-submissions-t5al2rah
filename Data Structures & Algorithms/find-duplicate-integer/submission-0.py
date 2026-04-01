class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            r = i + 1
            while r < len(nums):
                if nums[r] == nums[i]:
                    return nums[i]
                else:
                    r +=1

