class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        ops = ["+","-","/","*"]

        for t in tokens:
            if(t not in ops):
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                match t:
                    case "+":
                        r = a+b
                    case "-":
                        r = b -a
                    case "*":
                        r = a*b
                    case "/":
                        r = b/a
                if(t=="/"):
                    if(r<0):
                        r = ceil(r)
                    else:
                        r = floor(r)
                s = str(r)
                stack.append(s)

        return int(stack[-1])
        
        