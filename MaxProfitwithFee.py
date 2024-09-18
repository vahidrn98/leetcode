class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        return self.profit(prices,fee,None,0)

    def profit(self,prices,fee,i,j):
        if(j==len(prices)):
            return 0
        if(i==None):
            return max(self.profit(prices,fee,j,j+1)-prices[j]-fee,self.profit(prices,fee,None,j+1))
        
        if(prices[i]<prices[j]):
            return max(self.profit(prices,fee,None,j+1)+prices[j]-fee,self.profit(prices,fee,i,j+1))

        return self.profit(prices,fee,i,j+1)
        
        