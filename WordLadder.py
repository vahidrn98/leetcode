from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord,1)])
        wordList = self.toDict(wordList)
        visited = {}

        while q:
            word,level = q.popleft()

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordList and newWord not in visited and   newWord != word:
                        if(newWord==endWord):
                            return level +1
                        
                        q.append((newWord,level+1))
                        visited[newWord] = True

        return 0
        
    def toDict(self,lst):
        d = {}
        for x in lst:
            d[x] = True
        return d