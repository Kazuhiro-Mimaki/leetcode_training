class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        ans = 0
        for p in prices:
            profit = p - minimum
            if p < minimum:
                minimum = p
            if profit > ans:
                ans = profit
        return ans
