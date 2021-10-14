
# **Search in Rotated Sorted Array**
## **Problem Statement:**

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

## **Example 1:**
### **Input: nums=[4,5,6,7,0,1,2]**
## **target:4**
## **Output:4**

## **Example 2:**
### **Input: nums=[4,5,6,7,0,1,2]**
### **target: 3**
### **Output:-1**

# **Solution:**
To find the target element .in log(N) time.We have to use a Binary search function.But it only works on
Sorted array. Because our list is rotated , it is not sorted anymore.
So we have to make a slight change in binary search function.
## **Changes in Code snippet**
```angular2html
            if nums[mid] == target:
                return mid
            elif nums[low] > nums[mid]://Reassign the variables if the array is not sorted
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

```
