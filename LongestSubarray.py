class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0

        ones = 0
        max_ones = 0
        zeros = 0
        deleted = False

        while(j<len(nums)):
            if(nums[j]==1):
                ones+=1
                max_ones = max(ones,max_ones)
            else:
                
                if(zeros==0):
                    zeros+=1
                    deleted = True
                else:
                    zeros+=1
                    if(nums[i]==0):
                        zeros-=1
                    else:
                        ones -=1
                    i +=1
            j+=1

        
        max_ones = max(max_ones,ones) 

        if(not deleted):
            max_ones-=1  

        return max_ones