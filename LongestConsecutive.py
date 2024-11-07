class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        a = nums[0]
        length = 1
        maxLen = 1
        if(len(nums)>1):
            for n in nums[1:]:
                if n==a+1:
                    length +=1
                    maxLen = max(maxLen,length)
                elif(n>a+1):
                    length=1
                a = n
        
        return maxLen


        