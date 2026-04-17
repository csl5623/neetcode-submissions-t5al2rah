class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            SUM = 0
            while l < r:
                SUM = nums[i] + nums[l] + nums[r]
                if SUM < 0:
                    l+=1
                elif SUM > 0:
                    r-=1
                else:
                    solution.add((nums[i], nums[l],nums[r]))
                    l +=1
                    r-=1
        return list(solution)