class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        comb = []
        self.backtrack(n,k,comb,arr,1)
        return arr

        
    def backtrack(self,n,k,comb,arr,start):
        if(k==len(comb)):
            arr.append(comb)
            comb = []
            return
        
        for a in range(start,n+1):
            if(a not in comb):
                self.backtrack(n,k,comb+[a],arr,a+1)
