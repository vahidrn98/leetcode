class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        return self.lcs(text1,text2,0,0,dp)

    def lcs(self,text1,text2,i,j,dp):
        if i == len(text1) or j == len(text2):
                return 0
        if((i,j) in dp):
            return dp[(i,j)]
        if(text1[i]==text2[j]):
            return 1 + self.lcs(text1,text2,i+1,j+1,dp)
        result = max(self.lcs(text1,text2,i+1,j,dp),self.lcs(text1,text2,i,j+1,dp))
        dp[(i,j)] = result
        return result
        
        