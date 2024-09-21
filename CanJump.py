class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        s = [0]
        while(len(s)>0):
            i = s.pop()
            if(i==len(nums)-1):
                return True
            if(nums[i]>0):
                for a in range(1,nums[i]+1):
                    if(i+a>=len(nums)-1):
                        return True
                    if(i+a not in s):
                        s.append(i+a)
        return False