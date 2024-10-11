class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        comb = ""
        self.backtrack(n,0,0,comb,arr)
        return arr


    def backtrack(self,n,nl,nr,comb,arr):
        
        if(len(comb)==n*2):
            arr.append(comb)
            comb = ""
            return

        
        if(nl==n):
            
            if(nr<n):
                self.backtrack(n,nl,nr+1,comb+")",arr)
            return
        elif(nl<n):
            if(nl>nr):
                self.backtrack(n,nl,nr+1,comb+")",arr)
                self.backtrack(n,nl+1,nr,comb+"(",arr)
            elif(nl==nr):
                
                self.backtrack(n,nl+1,nr,comb+"(",arr)
        else:
            raise "out of range"

        