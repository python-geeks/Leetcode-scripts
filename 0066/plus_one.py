class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # check array in reverse order
        # if digit is less than 9: increment 1 in digits[i]
        # if digit is 9: assign the digit[i] = 0
        # check if the val is in position 1 i.e i==0
        # if yes, then rem = 1
        # if rem is 1, then add rem value to the 1 position of the digits list
        # return the list
        
        rem = 0
        for i in range(len(digits)-1,-1,-1):
            if(digits[i] == 9):
                if(i == 0):
                    rem = 1
                digits[i] = 0
            else:
                digits[i] = digits[i]+1
                break
        if(rem == 1):
            digits.insert(0,rem)
        return(digits)
