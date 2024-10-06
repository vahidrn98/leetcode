class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap = {}

        for x in prerequisites:
            a,b = x
            cmap[b] = a

        visited = {}


        for i in range(numCourses):
            if(i in cmap):
                visited[i] = True
        
        for i in range(numCourses):
            if(i in cmap and cmap[i] in visited):
                return False
        
        return True


        