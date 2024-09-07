class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i_s = 0
        j_s = 1
        k_s = 2
        if(len(nums)<3):
            return False
        for i in range(i_s,len(nums)-2):
            j_s = i+1
            for j in range(j_s,len(nums)-1):
                k_s = j+1
                if(nums[i] < nums[j]):
                    for k in range(k_s,len(nums)):
                        # print(i,j,k)
                        if nums[j] < nums[k]:
                            return True
        return False
        