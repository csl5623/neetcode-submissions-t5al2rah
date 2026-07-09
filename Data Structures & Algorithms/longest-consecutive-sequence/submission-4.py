class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        streak = 0
        for num in nums:
            if num - 1 not in hashset:
                item_exist = num + 1
                local_streak = 1
                while item_exist in hashset:
                    local_streak+=1
                    item_exist +=1
                print(local_streak)
                streak = max(streak,local_streak)
        return streak
