class Solution:

    def col(self,grid,i):
        return [grid[j][i] for j in range(len(grid))]

    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i]==self.col(grid,j)):
                    pairs +=1
        return pairs