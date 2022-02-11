class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        max = 0
        for i in range(1, len(prices)):
            print(prices[i])
            if curr > prices[i]:
                curr = prices[i]
            else:
                diff = prices[i] - curr
                if diff > max:
                    max = diff
        return max
