class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        window = {}
        have = 0
        res = [-1, -1]
        resLen = float("infinity")
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        l = 0
        need = len(countT)
        for i in range(len(s)):
            r = s[i]
            if r in countT:
                window[r] = 1 + window.get(r,0) 
            if r in countT and countT[r] == window[r]:
                have+=1
            while need == have:
                if i - l + 1 < resLen:
                    res = [l,i]
                    resLen = i - l + 1
                if s[l] in countT:
                    window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        if resLen != float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""
