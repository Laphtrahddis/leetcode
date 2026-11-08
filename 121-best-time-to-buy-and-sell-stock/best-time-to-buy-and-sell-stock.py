class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = -1
        mostProfit = 0
        for i in prices:
            if i < min or min == -1:
                min = i
            profit = i - min
            if mostProfit < profit:
                mostProfit = profit
        return mostProfit
