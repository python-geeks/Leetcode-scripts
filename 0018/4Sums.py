class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                lo = j + 1
                hi = len(nums) - 1
                while lo < hi:
                    s = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if s == target:
                        ans.add((nums[i], nums[j], nums[lo], nums[hi]))
                        lo += 1
                    elif s < target:
                        lo += 1
                    else:
                        hi -= 1
        return list(ans)