import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        max_k = r
        while l <= r:
            mid = (l+r) // 2
            curr_hours = 0
            for i in piles:
                curr_hours += math.ceil((i/mid))
            if curr_hours <= h:
                if mid <= max_k:
                    max_k = mid
                r = mid - 1
            else:
                l = mid + 1
        return max_k


            

            

                

         


        