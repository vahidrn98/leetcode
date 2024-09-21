class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf]*len(nums)

        return self.numJump(nums,dp,0)
        
    def numJump(self,nums,dp,i):

        if(i>=len(nums)-1):
            return 0

        if(dp[i]!=inf):
            return dp[i]

        minimum = inf
        for a in range(1,nums[i]+1):
            minimum = min(minimum,self.numJump(nums,dp,i+a))

        dp[i] = 1 + minimum

        return dp[i]

        