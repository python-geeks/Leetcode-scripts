# We declare a stack of unmatched parentheses. As we move, if it is a 
# closing parenthesis, we will check if it matches the parentheses on the top 
# of the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        pair = dict(('()', '[]', '{}'))
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif len(st) == 0 or x != pair[st.pop()]:
                return False
        return len(st) == 0