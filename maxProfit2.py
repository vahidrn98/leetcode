class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = inf
        profit = 0
        for p in prices:
            if p<=mini:
                mini=p
            else:
                profit = max(profit,p-mini)
        return profit
        