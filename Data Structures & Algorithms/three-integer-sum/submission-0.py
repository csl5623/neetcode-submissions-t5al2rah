class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        tripletList = []
        nums.sort()


        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums [i -1]:
                continue
        
            l = i + 1
            r = len(nums) -1
           
            while l < r:
                sum3 = nums[r] + nums[l] + nums[i]
                if sum3 == 0:
                    tripletList.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums [l -1] and l < r:
                        l +=1
                elif sum3 < 0:
                    l +=1
                else:
                    r -=1

        return tripletList