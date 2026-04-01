class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##sort the strings
        s = sorted(s)
        t = sorted(t)
        ##check if both strings are the same
        return s == t

