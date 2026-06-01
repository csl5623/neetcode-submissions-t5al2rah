class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 0 
        profit = 0
        while l < len(prices) and r < len(prices):
            r = l + 1
            print(r)
            while r < len(prices) and l <len(prices) and prices[l] < prices[r]:
                print(profit)
                print("here")
                curr = prices[r] - prices[l]
                profit = max(curr,profit)
                r += 1
            l = r
        return profit