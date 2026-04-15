import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        l = 0
        r = len(string) - 1
        while l < r:
            while not string[l].isalnum() and l < r:
                l+=1
            while not string[r].isalnum() and r > l:
                r-=1
            if string[l] != string[r]:
                return False
            l+=1
            r-=1
        return True

