class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = {x:i for i,x in enumerate(wordDict)}

        return self.isInDict(s,wd)
    
    def isInDict(self,s,wordDict):

        for i in range(len(s)):
            if(s[:i+1] in wordDict):
                if(i+1 == len(s) or self.isInDict(s[i+1:],wordDict)):
                    return True
        
        return False