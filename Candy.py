class Solution:
    def candy(self, ratings: List[int]) -> int:
        inIsland = False
        candies = [1]*len(ratings)
        for r in range(len(ratings)):
            if((r>0 and ratings[r]>ratings[r-1]) ):
                candies[r] = candies[r-1]+1
            elif((r<len(ratings)-1 and ratings[r]>ratings[r+1])):
                candies[r] = candies[r+1]+1

            
        return sum(candies)
        