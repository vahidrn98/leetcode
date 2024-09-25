class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        candies = [1]*len(ratings)
        for r in range(len(ratings)):
            _ = self.assign(ratings,r,candies)
        
        return sum(candies)


    def assign(self,ratings,i,candies):
        if(i>=len(ratings) or i<0):
            return 0
        
        if(candies[i]>1):
            return candies[i]
        
        if(i<len(ratings)-1):
            if(ratings[i]>ratings[i+1]):
                candy_right = self.assign(ratings,i+1,candies)
                if(i>0):
                    if(ratings[i]>ratings[i-1]):
                        candy_left = self.assign(ratings,i-1,candies)
                        candies[i] = max(candy_left,candy_right)+1
                        return candies[i]
                    else:
                        candies[i] = candy_right+1
                        return candies[i]
                else:
                    candies[i] = candy_right+1
                    return candies[i]
            else:
                if(i>0):
                    if(ratings[i]>ratings[i-1]):
                        candy = self.assign(ratings,i-1,candies)
                        candies[i] = candy+1
                        return candies[i]
                    else:
                        return candies[i]
                else:
                    return candies[i]

        else:
            if(ratings[i]>ratings[i-1]):
                candy = self.assign(ratings,i-1,candies)
                candies[i]=candy+1
                return candies[i]
            else:
                return candies[i]