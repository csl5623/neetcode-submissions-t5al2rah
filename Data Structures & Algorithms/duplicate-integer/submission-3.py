class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()

        for i in nums:
            if i in duplicateSet:
                return True
            else:
                duplicateSet.add(i)
        return False