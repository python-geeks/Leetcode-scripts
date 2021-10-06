class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # trivial solution
        if (numRows <= 1 or len(s) <= numRows):
            return s
        result = [""] * numRows

        # Counter for row number
        nRow = 0
        # If going downwards reverse = False, elif going upwards reverse = True
        reverse = False

        # iterate over each character in the string
        for i in range(len(s)):
            result[nRow] = result[nRow] + s[i]  # store characters
            if reverse is False:
                nRow += 1
            else:
                nRow -= 1
            # change direction
            if (nRow == numRows - 1 or nRow == 0):
                reverse = not reverse

        # join the characters
        return ''.join(result)
