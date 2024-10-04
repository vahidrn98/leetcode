class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        
        for r in board:
            digits = {}
            for d in r:
                if(d!= "." and d in digits):
                    return False
                elif(d!="."):
                    digits[d] = True

        # check cols

        for i in range(len(board)):
            digits = {}
            for j in range(len(board)):
                if(board[j][i]!="." and (board[j][i] in digits)):
                    
                    return False
                elif(board[j][i]!="."):
                    digits[board[j][i]] = True


        for i in range(len(board)//3):
            for j in range(len(board)//3):
                start_i = i*3
                start_j = j*3
                # check the square starting with i and j
                digits = {}
                for a in range(3):
                    for b in range(3):
                        d = board[start_i+a][start_j+b]
                        if(d!= "." and d in digits):
                            print(start_i+a,start_j+b)
                            return False
                        elif(d!="."):
                            digits[d] = True

        return True



        