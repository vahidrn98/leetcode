class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0
        c = 0
        while(j<len(nums)):
            if(nums[j]==val):
                j+=1
                c+=1
            else:
                nums[i]=nums[j]
                i+=1
                j+=1
        
        return len(nums)-c
        