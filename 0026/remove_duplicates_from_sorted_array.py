class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        :type nums: list[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            i = 0
            for j in range(1, len(nums)):
                # If the elements are not duplicated, then keep adding them
                # at the starting of the array in their relative order.
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]

        return i + 1
