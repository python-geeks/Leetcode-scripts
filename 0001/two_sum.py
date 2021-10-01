class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()

        # Iterating the list
        for i, num in enumerate(nums):

            # If the target-num in dict then, we found the solution
            try:
                hash_table[target - num]
                return [hash_table[target - num], i]
            except KeyError:
                hash_table[num] = i
