from collections import defaultdict,deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = self.buildGraph(equations,values)
        ans = []

        for q in queries:
            val = self.bfs(q,adj)
            ans.append(val)
        
        return ans
    
    def buildGraph(self,equations,values):

        g = defaultdict(dict)
        for i,e in enumerate(equations):
            g[e[0]][e[1]] = values[i]
            g[e[1]][e[0]] = 1.0/values[i]
        
        return g

    def bfs(self,query,adj):
        dividend,divisor = query

        if dividend not in adj or divisor not in adj:
            return -1.0
        
        q = deque([(dividend,1.0)])
        visited = set()

        while q:
            node, value = q.popleft()

            if node == divisor:
                return value

            visited.add(node)

            for neighbor,val in adj[node].items():
                if(neighbor not in visited):
                    q.append((neighbor,value*val))

        return -1.0
        