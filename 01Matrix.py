class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dist = [[inf]*n]*m
        for a in range(m):
            for b in range(n):
                self.findDist(mat,dist,a,b,m,n)
        return dist

    def findDist(self,mat,dist,i,j,m,n):
        if(i>=m or j>=n or i<0 or j<0):
            return 0

        if(dist[i][j]!=inf):
            return dist[i][j]

        if(mat[i][j]==0):
            dist[i][j] = 0
            return 0
        
        dist[i][j] =  1 + min(self.findDist(mat,dist,i+1,j,m,n),self.findDist(mat,dist,i-1,j,m,n),self.findDist(mat,dist,i,j+1,m,n),self.findDist(mat,dist,i,j-1,m,n))

        return dist[i][j]
        