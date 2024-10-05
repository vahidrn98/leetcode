class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        smap = {}

        for s in strs:
            string = "".join(sorted(s))
            print(string)
            if(string in smap):
                smap[string] = smap[string] + [s]
            else:
                smap[string] = [s]
        
        return list(smap.values())
        