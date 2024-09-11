
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        ans = []
        for p in points:
            dist.append(p[0]**2+p[1]**2)
        h = dist.copy()
        h.sort()
        j = -1
        for i in range(k):
            el = h[i]
            j = dist[j+1:].index(el)
            ans.append(points[j])

        return ans

        

        