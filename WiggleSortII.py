class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_array = sorted(nums)
        
        first_half = sorted_array[:int(math.ceil(len(sorted_array)/2))]
        second_half = sorted_array[int(math.ceil(len(sorted_array)/2)):]
        second_half = second_half[::-1]
        first_half = first_half[::-1]
        # print(second_half)
        
        j = 0
        for a in first_half:
            nums[j] = a
            j+=2

        j = 1
        for b in second_half:
            if j<len(nums):
                nums[j] = b
                j+=2
            
        
        