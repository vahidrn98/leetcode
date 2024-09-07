class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        table = []

        for i in range(n):
            table.append([])
            for j in range(n):
                table[i].append(None)
        
        for i in range(n):
            for j in range(i,n):
                if(table[i][j]==None):
                    if(i==j):
                        table[i][j] = nums[i]
                    else:
                        table[i][j] = table[i][j-1]*nums[j]
        # print(table)
        for i in range(n):
            if(i==0):
                # print(i+1)
                # print(n-1)
                answer.append(table[i+1][n-1])
            elif(i==n-1):
                answer.append(table[0][i-1])
            else:
                answer.append(table[0][i-1] * table[i+1][n-1])
        return answer
