class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        ops = 0
        while(j>i):
            if(nums[i]+nums[j]==k):
                ops+=1
                j-=1
                i+=1
            elif(nums[i]+nums[j]>k):
                j-=1
            else:
                i+=1
        return ops

        