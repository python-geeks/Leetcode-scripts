# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower,
# 1 if my number is higher, otherwise return 0

# this function is just added to pass the flake8 code linter
# delete this function definition while using it on leetcode
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        # here start = 1 ans end = n
        # I supply mid as my pick and check with the original pick
        # if pick is not right, update start or end accodingly

        start = 1
        end = n
        while start <= end:

            mid = start + (end - start) // 2
            x = guess(mid)

            if x == 0:
                # element is found
                return mid

            elif x == -1:

                # guessed element is greater than actual element
                # search in the left of mid
                end = mid - 1
            else:
                # guessed element is less than actual element
                # search in the right of mid
                start = mid + 1
