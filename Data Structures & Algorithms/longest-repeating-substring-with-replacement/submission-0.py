class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        freq = dict()
        res = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            maxf = max(freq[s[r]],maxf)
            ##r-l_1 is the size of the window
            ##window is invalid when ## of non frwequent chracters in > k
            while(r-l +1 - maxf > k):
                freq[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
        return res