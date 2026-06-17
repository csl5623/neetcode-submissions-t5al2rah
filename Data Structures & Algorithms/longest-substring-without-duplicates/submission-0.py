class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_len = 0
        r = 0
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            max_len = max((r-l + 1),max_len)
            r+=1
        return max_len
            
                
