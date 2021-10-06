class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """        
        rem = 0
        
        # Iterate array in reverse order
        for i in range(len(digits)-1,-1,-1):
            # If digit is 9: assign the digit[i] = 0
            if(digits[i] == 9):
                # if digits[i] in first position i.e 0
                if(i == 0):
                    rem = 1 #update rem
                digits[i] = 0
            
            # digit is less than 9: increment 1 in digits[i] and break the loop
            else:
                digits[i] = digits[i]+1
                break
                
        # if rem is 1, then add rem value to the 1 position of the digits list
        if(rem == 1):
            digits.insert(0,rem)
        return(digits)
