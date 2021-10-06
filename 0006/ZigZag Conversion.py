class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # trivial solution
        if (numRows <= 1 or len(s) <= numRows ):
            return s
        
        result = [""]*numRows 
        counter = 0             # Counter for row number
        reverse = False         # If going downwards reverse = False, else if going upwards reverse = True
        
        # iterate over each character in the string
        for i in range(len(s)):
            result[counter] = result[counter] + s[i] # store characters
            
            if reverse == False:
                counter += 1
            else:
                counter -= 1
            # change direction    
            if (counter == numRows - 1 or counter == 0):
                reverse = not reverse
        
        return ''.join(result) # join the characters
    
