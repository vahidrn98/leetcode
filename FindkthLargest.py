import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[0:k]
        heapq.heapify(h)

        for n in nums[k:]:
            heapq.heappushpop(h,n)
        
        return heapq.heappop(h)
        