
# Logic: Every trailing zero comes prom a power of 10 and every 10 must contain a 5 
# so just count power of 5 gives us no. of trailing zeros.

class Solution:
    def trailingZeroes(self, n: int) -> int:

        a = 0

        while(n >= 5):
            n //= 5
            a += n
            
        return a