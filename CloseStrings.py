from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if(len(word1)!=len(word2)):
            return False
        
        same_chars = set(list(word1))==set(list(word2))

        if(not same_chars):
            return False

        if(set(Counter(word1).values())==set(Counter(word2).values())):
            return True
        
        
        
        return False

        