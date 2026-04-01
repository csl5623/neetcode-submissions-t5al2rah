class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        for i in nums:
            if i in dupMap:
                return True
            dupMap[i] = 1
        return False