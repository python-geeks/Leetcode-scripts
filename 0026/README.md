# Remove Duplicates from Sorted Array

### Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are k elements after removing the duplicates, then the first k elements of `nums` should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

### Solution

- The array will be traversed with two pointers i and j.
- Initially, j starts incrementing.
- As long as `nums[i] = nums[j]`, we increment j to skip the duplicate element.
- While incrementing j, if `nums[i]` is not equal to `nums[j]`, then we place the non redundant element captured at index j into the place with index (i + 1), i.e., ahead of the latest non-redundant element.
- The process loops till the array `nums` is traversed completely.
- Finally, we return the upper bound of the range in which non-redundant elements are stored.

### Link to the problem

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
