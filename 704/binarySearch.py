class Solution:
    def search(self, arr, target: int) -> int:
        # simple Binary Search Algorithm

        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
