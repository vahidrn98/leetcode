class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        if(n1==0 or n2==0):
            return ""

        largest = ""
        if(n1<=n2):
            for i in range(n1):
                c = str1[:i+1]
                if(str1 == c*(n1//(i+1))):
                    if(str2 == c*(n2//(i+1))):
                        largest = str1[:i+1]
        elif(n2<n1):
            for i in range(n2):
                c = str2[:i+1]
               
                if(str2 == c*(n2//(i+1))):
                    if(str1 == c*(n1//(i+1))):
                        largest = str2[:i+1]
        return largest