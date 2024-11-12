class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = []
        post = []
        mini = float("inf")
        maxi = -float("inf")

        for p in prices:
            if p < mini:
                mini = p
            pre.append(mini)

        for p in prices[::-1]:
            if p>maxi:
                maxi = p
            post.append(maxi)
        
        maxProfit = 0
        post.reverse()
        for mi,ma in zip(pre,post):
            maxProfit = max(maxProfit,ma-mi)

        return maxProfit
