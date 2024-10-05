class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if(len(intervals)==1):
            return intervals

        intervals.sort()

        newlist = []
        newlist.append(intervals[0])

        for i in range(1,len(intervals)):
            if(intervals[i][0]<=newlist[-1][1]):
                newi = [min(newlist[-1][0],intervals[i][0]),max(newlist[-1][1],intervals[i][1])]
                newlist.pop()
                newlist.append(newi)
            else:
                newlist.append(intervals[i])

        return newlist

        