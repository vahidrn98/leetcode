
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        ans = []
        for p in points:
            dist.append([p[0]**2+p[1]**2,p[0],p[1]])
        
        dist.sort()
        ans = []
        i = 1
        for d in dist:
            if(i>k):
                break
            ans.append([d[1],d[2]])
            i+=1

        return ans
    
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        heapq.heapify(dist)
        ans = []

        size = 0
        for p in points:
            heapq.heappush(dist,(-(p[0]**2+p[1]**2),p))
            size+=1
            if(size>k):
                heapq.heappop(dist)
                size-=1
        ans = heapq.nsmallest(k,dist)
        return [a[1] for a in ans]

        

        