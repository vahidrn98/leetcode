class Solution:
    def calculate(self, s: str) -> int:

        number =0
        sign = 1
        stack = []
        result = 0

        for c in s:
            if(c.isnumeric()):
                number = number*10 + int(c)
            elif(c in "+-"):
                result +=number *sign
                sign = -1 if c=="-" else 1
                number = 0
            elif(c=="("):
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif(c==")"):
                result += sign*number
                result *= stack.pop()
                result += stack.pop()
                number = 0
            
        

        return result + sign*number