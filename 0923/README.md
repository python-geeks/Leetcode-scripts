# Problem Statement
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
As the answer can be very large, return it modulo 109 + 7.

## Example 1:
```
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
```

## Example 2:
```
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
```

# Solution
## Approach 1: Counting with Cases
### Intuition and Algorithm
Let count[x] be the number of times that x occurs in A. For every x+y+z == target, we can try to count the correct contribution to the answer. 

## Approach 2: Three Pointer
### Intuition and Algorithm
Sort the array. For each i, set T = target - A[i], the remaining target. We can try using a two-pointer technique to find A[j] + A[k] == T. This approach is the natural continuation of trying to make the two-pointer technique we know from previous problems, work on this problem.
Because some elements are duplicated, we have to be careful. In a typical case, the target is say, 8, and we have a remaining array (A[i+1:]) of [2,2,2,2,3,3,4,4,4,5,5,5,6,6]. We can analyze this situation with cases.

Whenever A[j] + A[k] == T, we should count the multiplicity of A[j] and A[k]. In this example, if A[j] == 2 and A[k] == 6, the multiplicities are 4 and 2, and the total number of pairs is 4 * 2 = 8. We then move to the remaining window A[j:k+1] of [3,3,4,4,4,5,5,5].

As a special case, if A[j] == A[k], then our manner of counting would be incorrect. If for example the remaining window is [4,4,4], there are only 3 such pairs. In general, when A[j] == A[k], we have (M/2) = (M*(M-1))/2 pairs (j,k) (with j < k) that satisfy A[j] + A[k] == T, where MM is the multiplicity of A[j] (in this case M=3M=3).

