class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = {x:i for i,x in enumerate(wordDict)}
        segmented = {}
        return self.isInDict(s,wd,segmented)
    
    def isInDict(self,s,wordDict,segmented):
        if(s in segmented):
            return segmented[s]
        for i in range(len(s)):
            if(s[:i+1] in wordDict):
                if(i+1 == len(s) or self.isInDict(s[i+1:],wordDict,segmented)):
                    segmented[s] = True
                    return True
        segmented[s] = False
        return False