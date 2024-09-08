class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = ""
        chars = ""
        decoded = ""
        for c in s:
            if c.isnumeric():
                number+=c
            elif(c=="["):
                stack.append(int(number))
                number=""
                stack.append(c)
            elif(c.isalpha()):
                chars+=c
            else:
                e = stack.pop()
                while(e.isalpha()):
                    chars = e + chars
                    e = stack.pop()

                chars = chars * stack.pop()
                decoded = decoded + chars
                chars = ""
        decoded = decoded+chars
        return decoded
                
                


        