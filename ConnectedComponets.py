class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        components = 0
        for i in range(len(isConnected)):
            if i not in visited:
                components+=1
                visited = self.visit(isConnected,i,visited)

        return components
            
    
    def visit(self,isConnected,i,visited):
        if i in visited:
            return visited
        
        visited.add(i)
        for node in range(len(isConnected[i])):
            if node not in visited and isConnected[i][node]==1 and i!=node:
                visited = self.visit(isConnected,node,visited)
        return visited
        
        