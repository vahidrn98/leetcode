class Solution:
    def calculate(self, s: str) -> int:

        stack = []

        for c in s:
            if(c==" "):
                continue

            if(c.isnumeric()):
                if(stack):
                    prev = stack[-1]
                    if(prev !="("):
                        op = stack.pop()
                        match op:
                            case "+":
                                a = stack.pop()
                                b = c
                                r = int(a) + int(b)
                                stack.append(str(r))
                            case "-":
                                a = stack.pop()
                                b = c
                                r = int(a) - int(b)
                                stack.append(str(r))
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            elif(c=="(" or c=="+" or c=="-"):
                stack.append(c)
            else:
                current = c
                while(current!="("):
                    b = stack.pop()
                    x = stack.pop()
                    if(x=="("):
                        stack.append(b)
                        break
                    else:
                        a = stack.pop()
                        if(a=="("):
                            if(x=="-"):
                                stack.append(x)
                                stack.append(b)
                            break
                        else:
                            match x:
                                case "+":
                                    r = int(a) + int(b)
                                    stack.append(str(r))
                                case "-":
                                    r = int(a) - int(b)
                                    stack.append(str(r))

        return int(stack.pop())
                    





        