class Solution:
    def reverse(self, x):
        range_ = range(-2**31, 2**31-1)
        y = str(abs(x))
        if x == 0 or x not in range_: return 0
        x = int('-' + y[::-1]) if x < 0 else int(y[::-1])
        return x if x in range_ else 0