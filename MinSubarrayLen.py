class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0

        s = nums[0]
        min_length = inf

        while(i!=len(nums)-1 or j!=len(nums)-1):
            if(s==target):
                min_length = min(min_length,j-i+1)
                if(min_length==1):
                    return 1
    
                if(i<len(nums)):
                    s-=nums[i]
                i+=1
                j+=1
                if(j<len(nums)):
                    s+= nums[j]
                j = min(len(nums)-1,j)
            elif(s>target):
                s-=nums[i]
                i+=1
            else:
                j+=1
                if(j<len(nums)):
                    s+=nums[j]
                j = min(len(nums)-1,j)
        if(min_length==inf):
            min_length = 0
        return min_length