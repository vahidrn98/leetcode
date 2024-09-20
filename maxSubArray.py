class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = nums.copy()

        for n in range(1,len(nums)):
            dp[n] = max(nums[n]+dp[n-1],nums[n])
        
        return max(dp)
        