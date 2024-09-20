class Solution:
    def maxArea(self, height: List[int]) -> int:

        A = 0
        i = 0
        j = len(height)-1
        while(i<j):
            A = max(A,min(height[i],height[j])*(j-i))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1

        return A
        