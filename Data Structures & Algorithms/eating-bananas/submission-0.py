class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_value = max(piles)
        l = 1
        r = max_value
        result = []
        while l <= r:
            k = (l + r) // 2
            print(k)
            current_hours = 0
            for i in range(len(piles)):
                rate = math.ceil(piles[i]/k)
                current_hours += rate
            if current_hours <= h:
                result.append(k)
                r = k - 1
            else:
                l = k + 1
        return min(result)

            

            

                

         


        