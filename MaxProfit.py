class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        for i in range(1,len(prices)):
            diff = prices[i]-prices[i-1]
            if(diff>0):
                s+=diff
        return s
        