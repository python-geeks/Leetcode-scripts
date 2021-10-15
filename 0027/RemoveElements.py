from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for n in range(len(nums)):

            # checks which element in the array does not match with val
            if nums[n] != val:
                nums[k] = nums[n]
                k += 1  # increments the value of k by 1

        return k
