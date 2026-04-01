class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ##set that remove duplicates
        ##if value already in set, return false
        number_set = set()
        for i in nums:       
            if i not in number_set:
                number_set.add(i)
            else:
                return True
        return False