class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hmap = {}

        for i in range(len(nums)):
            n = nums[i]

            if(n in hmap):
                if(i-hmap[n]<= k):
                    return True
            
            hmap[n] = i
        
        return False

        