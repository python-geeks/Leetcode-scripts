from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            # check if val is in nums list
            if val in nums:
                # removes the val from nums list
                nums.remove(val)

        return nums  # returns nums list with remaining elements
