class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1 
        profit = 0
        while r < len(prices):
            if r < len(prices) and l < len(prices) and prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                profit = max(curr,profit)
            else:
                l = r
            r+=1
        return profit