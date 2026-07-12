class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        itemSet = set()

        for i in nums:
            if i in itemSet:
                return i
            itemSet.add(i)