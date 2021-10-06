from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking if numbers are repeated in each row. If yes, return false
        for row in board:
            for num in row:
                # if the element is a dot, move to the next element
                if num == '.':
                    continue
                # if the element is a number, check if its count exceeds 1.
                if row.count(num) > 1:
                    return False
                
        # checking if numbers are repeated in each column. If yes, return false
        for col in range(len(board)):
            temp = []
            for row in range(len(board[0])):
                # Gather all the numbers in a column in a separate list - temp
                if board[row][col] != '.':
                    temp.append(board[row][col])
            # Checking if there are any duplicates. If yes, rule 2 is violated.
            if len(set(temp)) != len(temp):
                return False
            
        # checking if numbers are repeated in each 3 * 3 box.
        for i in range(0, len(board)-2, 3):
            for j in range(0, len(board[0])-2, 3):
                # Storing 3*3 box elements in temp
                p = board[i][j:j+3]
                q = board[i+1][j:j+3]
                r = board[i+2][j:j+3]
                temp = p+q+r
                # Checking if any number is repeated. If yes, return false
                for k in temp:
                    if k != '.':
                        if temp.count(k) > 1:
                            return False
        
        # If none of the rules are violated, return true
        return True
        