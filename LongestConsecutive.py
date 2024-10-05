class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        visited = {}
        for n in nums:
            if(n in visited):
                continue
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    visited[n+length] = True
                    length += 1
                
                longest = max(longest, length)
        
        return longest
