class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False

        s_en = ""
        t_en = ""

        schars = {}
        tchars = {}

        scounter = 0
        for c in s:
            if(c in schars):
                s_en += str(schars[c])
            else:
                scounter += 1
                schars[c] = scounter
                s_en += str(schars[c])
        
        tcounter = 0
        for c in t:
            if(c in tchars):
                t_en += str(tchars[c])
            else:
                tcounter += 1
                tchars[c] = tcounter
                t_en += str(tchars[c])
        
        return s_en == t_en