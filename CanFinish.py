class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap = {}

        for p in prerequisites:
            if p[1] not in cmap:
                cmap[p[1]] = [p[0]]
            else:
                cmap[p[1]].append(p[0])

        visited = {}
        for c in cmap:
            if not self.dfs(c,cmap,visited):
                return False
        
        return True
        
    
    def dfs(self,course, cmap, visited):

        if(course in visited):
            return False
        
        if(course not in cmap):

            visited[course] = True
            return True
        
        visited[course] = True
        
        for c in cmap[course]:
            if not self.dfs(c,cmap,visited):
                return False
        
        return True