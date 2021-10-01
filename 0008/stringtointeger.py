class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = 1
        index = 0
        s = s.strip() # deleting all leading spaces
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        while index < len(s) and s[index].isdigit():
            ans = ans * 10 + int(s[index])
            index += 1
        ans = min(max(sign*ans, -2**31), 2**31-1)
        return ans