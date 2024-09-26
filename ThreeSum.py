class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = []
        unique = set()
        
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):

                    s = nums[i] + nums[j] + nums[k]
                    if(s ==0):
                        string = (str(nums[i]) + str(nums[j]) + str(nums[k]))
                        if(string not in unique):
                            unique.add(string)
                            triplets.append([nums[i], nums[j], nums[k]])
                    elif(s>0):
                        break
        
        return list(triplets)