def isPalindrome(self, x: int) -> bool:
	if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
		return False
	
	result = 0
	while x > result:
		result = result * 10 + x % 10
		x = x // 10
		
	return True if (x == result or x == result // 10) else False
