class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values_map = {}

        for i in range(len(nums)):
                values_map[nums[i]] = i
            

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in values_map and values_map[diff] != i:
                return [i,values_map[diff]]

            