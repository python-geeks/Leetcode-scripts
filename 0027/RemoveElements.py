from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for n in range(len(nums)):

            if nums[n] != val:
                nums[k] = nums[n]
                k += 1

        return k
