class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # We'll use a stack to track the open brackets we've seen so far.
        stack = []

        # As we encounter each closed bracket, we'll use this map to
        # help us determine if we've seen its corresponding open bracket.
        bracket_map = {')': '(',
                       ']': '[',
                       '}': '{'}
        
        for bracket in s:
            
            # If we see an open bracket, add it to the top of the stack.
            if bracket not in bracket_map:
                stack.append(bracket)
            
            # If we see a closed bracket, check if its corresponding
            # open bracket is at the top of the stack. If so, pop it off.
            elif stack and bracket_map[bracket] == stack[-1]:
                stack.pop(-1)
            
            # Otherwise, the string is not valid.
            else:
                return False
                
        # If the resulting stack is empty, then we have a valid string.
        return stack == []
