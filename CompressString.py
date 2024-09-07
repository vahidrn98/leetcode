class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 0
        arr = []
        group_count = 1
        for char in chars:
            if(c==0):
                arr.append(char)
            else:
                if(chars[c]==chars[c-1]):
                    group_count+=1
                    if(c==len(chars)-1):
                        arr.append(str(group_count))
                else:
                    if(group_count!=1):
                        arr.append(str(group_count))
                    arr.append(char)
                    group_count=1
            c+=1
        # print(arr)
        compressed = "".join(arr)
        for i in range(len(compressed)):
            chars[i] = compressed[i]
        return len(compressed)