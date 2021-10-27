class Solution:class Solution:
    def decodeString(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        
        stack  = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                print(stack)
                string = ""
                num = ""
                temp = ""

                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                for i in range(int(num)):
                    temp += string
                stack.append(temp)
        return "".join(stack)
