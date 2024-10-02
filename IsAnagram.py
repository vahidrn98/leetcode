from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False

        s = Counter(s)
        t = Counter(t)

        for c in s:
            if(s[c]!=t[c]):
                return False
        
        return True