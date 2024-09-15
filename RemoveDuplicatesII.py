class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        repeat = 0
        current = 0
        i = 0
        for j in range(len(nums)):
            if(nums[j]==nums[current]):
                repeat +=1
                if(repeat>2):
                    continue
                else:
                    nums[i] = nums[j]
            else:
                repeat = 1
                current = j
                nums[i] = nums[j]
            i+=1
        
        return i