class Solution:
    def decodeString(self, s: str) -> str:
        ## assuming a valid string is provided s != ("1[a", "2[[2ac]]")
        def get_char():
            res = ""
            while stack and not stack[-1] == '[':
                res = stack.pop() + res
            return res
        
        def get_num():
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            return num
                
        final= ""
        stack = []
        for ele in s:
            if ele == "]": # pop routine
                res = get_char()
                stack.pop()  # removing the "[" bracket
                num = get_num()
                if num:
                    res = int(num) * res
                if stack == []:
                    final += res
                else:
                    stack.append(res)
            else:
                stack.append(ele)
        if stack:
            final += ''.join(stack)
        return final
