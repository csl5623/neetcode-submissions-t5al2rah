class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = sorted(nums)
        # solution = set()
        # for i in range(len(nums)):
        #     l = i + 1
        #     r = len(nums) - 1
        #     SUM = 0
        #     while l < r:
        #         SUM = nums[i] + nums[l] + nums[r]
        #         if SUM < 0:
        #             l+=1
        #         elif SUM > 0:
        #             r-=1
        #         else:
        #             solution.add((nums[i], nums[l],nums[r]))
        #             l +=1
        #             r-=1
        # return list(solution)
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1
            
            while l < r:
                SUM = nums[i] + nums[l] + nums[r]
                if SUM < 0:
                    l+=1
                elif SUM > 0:
                    r-=1
                else:
                    res.append((nums[i], nums[l],nums[r]))
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res