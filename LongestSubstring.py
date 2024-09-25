class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = j = 0
        chars = {}
        maxLen = 0
        while(j<len(s)):
            if s[j] in chars:
                if(chars[s[j]]>=1):
                    chars[s[i]] -=1
                    i +=1
                else:
                    chars[s[j]]+=1
                    j+=1
                    
            else:
                chars[s[j]] = 1
                j+=1

            maxLen = max(maxLen,j-i)

        return maxLen
        