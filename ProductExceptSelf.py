class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        after = []
        before = []

        prod = 1
        for i in range(n):
            prod *= nums[n-1-i]
            after.append(prod)
        after = after[::-1]

        prod = 1
        for i in range(n):
            prod *= nums[i]
            before.append(prod)
        for i in range(n):
            if(i==0):
                answer.append(after[1])
            elif(i==n-1):
                answer.append(before[n-2])
            else:
                answer.append(after[i+1]*before[i-1])
        return answer
