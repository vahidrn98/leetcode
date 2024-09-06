class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sorted_array = sorted(nums)
        first_half = sorted_array[:len(sorted_array)//2]
        second_half = sorted_array[len(sorted_array)//2:]
        
        j = 0
        for a in first_half:
            nums[j] = a
            j+=2

        j = 1
        for b in second_half:
            nums[j] = b
            j+=2
            