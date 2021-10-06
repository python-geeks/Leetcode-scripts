class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend = int(dividend / divisor)
        if dividend > 2 ** 31 - 1:
            return 2147483647
        elif dividend < -2 ** 31:
            return 2147483648
        else:
            return dividend
