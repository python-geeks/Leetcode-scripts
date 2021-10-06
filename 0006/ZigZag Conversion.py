# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:00:21 2021

@author: saulp
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if (numRows <= 1 or len(s) <= numRows ):
            return s
        
        result = [""]*numRows
        counter = 0
        reverse = False
        
        for i in range(len(s)):
            result[counter] = result[counter] + s[i]
            
            if reverse == False:
                counter += 1
            else:
                counter -= 1
                
            if (counter == numRows - 1 or counter == 0):
                reverse = not reverse
                
        return ''.join(result)
