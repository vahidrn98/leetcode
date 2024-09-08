from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if(len(word1)!=len(word2)):
            return False
        
        if(set(word1.split())==set(word2.split())):
            return True

        if(set(Counter(word1).values())==set(Counter(word2).values())):
            print(set(Counter(word1).values()))
            print(set(Counter(word2).values()))
            return True
        
        return False

        