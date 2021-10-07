class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # search for target in the array => binary search
        # if target is found return index
        # else return start

        start = 0
        end = len(nums) - 1

        mid = start + (end - start) // 2

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                start = mid + 1

            else:
                end = mid - 1

        return start
