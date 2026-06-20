class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = {}
        freq2 ={}
        for i in s1:
            freq1[i] = 1 + freq1.get(i,0)
        
        l = 0

        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r],0)
            if freq2 == freq1:
                return True
            while ((r - l + 1) >= len(s1)):
                freq2[s2[l]] -=1
                if freq2[s2[l]] == 0:
                    freq2.pop(s2[l])
                l+=1
        return False
            
       
            

