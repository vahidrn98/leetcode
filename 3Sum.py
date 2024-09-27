class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = []
        unique = set()
        k = len(nums) - 1
        i = 0
        j = 1
        while(i<j):
            if (i>0 and nums[i]==nums[i-1]):
                i+=1
                continue
            j = i+1
            k = len(nums) -1
            while(j<k):
                
                s = nums[i] + nums[j] + nums[k]
                if(s ==0):
                    string = (str(nums[i]) + str(nums[j]) + str(nums[k]))
                    if(string not in unique):
                        unique.add(string)
                        triplets.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif(s>0):
                    k-=1
                else:
                    j+=1
            i+=1
        
        return list(triplets)