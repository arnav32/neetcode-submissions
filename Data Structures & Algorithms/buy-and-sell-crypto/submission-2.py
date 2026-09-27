class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        for r in range(len(prices)):
            for l in range(r):
                if prices[l] < prices[r]:
                    highest = max(highest, prices[r] - prices[l])
        return highest