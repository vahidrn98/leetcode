class Solution:
    def hammingWeight(self, n: int) -> int:
        res = (n) & 1
        for i in range(31):
            n = n >> 1
            if(n)&1:
                res+=1

        return res