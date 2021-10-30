class Solution:
    def Palindrome(self, a: int) -> bool:

        t = a
        r = 0

        while( a > 0 ):

            q = a % 10  
            r = r * 10 + q 
            a = a // 10

        if ( t == r ):  
            return True
        else:  
            return False
