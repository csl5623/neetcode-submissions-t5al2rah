class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceMap = {}
        for index,value in enumerate(nums):
            if value not in differenceMap:
                 differenceMap[value] = index

        for index,value in enumerate(nums):
            diff = target - value
            if diff in differenceMap and index != differenceMap[diff]:
                return sorted([index,differenceMap[diff]])
        return None 
            