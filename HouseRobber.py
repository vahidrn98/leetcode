class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [None]*len(nums)
        return self.maxRob(nums,0,money)

    def maxRob(self,nums,i,money):
        if(i>=len(nums)):
            return 0
        if(money[i]!=None):
            return money[i]
        money[i] = max(nums[i]+self.maxRob(nums,i+2,money),self.maxRob(nums,i+1,money))
        return  money[i]
        