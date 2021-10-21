class Solution:
    def reverse(self, x: int) -> int:
        val = 0
        pro = 1 if x>0 else -1
        x = abs(x)
        while x:
            val=val*10+x%10
            x//=10
        return val*pro  if (val<=2**31 -1 and val>=-2**31 ) else 0