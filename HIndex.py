class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_c = max(citations)+1
        h_arr = [0]*max_c
        for c in citations:
            for a in range(c+1):
                h_arr[a]+=1

        h_index = 0
        for h in range(len(h_arr)):
            if(h_arr[h]>=h and h>h_index):
                h_index = h

        return h_index