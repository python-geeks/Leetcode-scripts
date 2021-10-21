class Solution:
     def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:  return True
        return False
