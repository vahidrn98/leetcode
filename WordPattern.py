class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        if(len(pattern) != len(s)):
            return False

        hmap = {}

        i = 0
        for c in pattern:
            if(c in hmap):
                if(hmap[c]!=s[i]):
                    return False
            else:
                if(s[i] in hmap.values()):
                    return False
                else:
                    hmap[c] = s[i]
            
            i+=1
        
        return True
        