class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two pointer approach , time complexity O(n), space complexity O(1)
        max_len = -float("inf")
        max_ind = [-1, -1]

        # odd lenth palindromes
        for k in range(len(s)):
            i = k
            j = k
            while(i >= 0 and j <= len(s) - 1):
                if s[i] == s[j]:
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        max_ind = [i, j]

                    i -= 1
                    j += 1

                else:
                    break

        # even lenth palindromes
        for k in range(len(s) - 1):
            i = k
            j = k + 1
            while(i >= 0 and j <= len(s) - 1):
                if s[i] == s[j]:
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        max_ind = [i, j]

                    i -= 1
                    j += 1

                else:
                    break

        return s[max_ind[0]:max_ind[1] + 1]

        # Dynamic Programming approach ,
        # Time complexity O(n^2), Space complexity O(n^2)

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # sub string of length 1
        for i in range(len(s)):
            dp[i][i] = 1

        # substring of length 1 id always a palindrome
        max_len = 1
        max_ind = [0, 0]

        # sub string of length 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                if max_len == 1:
                    max_len = 2
                    max_ind[0] = i
                    max_ind[1] = i + 1

        # sub string of length greater than 2
        for j in range(2, len(s)):
            for i in range(0, len(s) - j):
                k = j + i
                if (s[k] == s[i]) and (dp[i + 1][k - 1] == 1):
                    dp[i][k] = 1
                    if (k - i + 1) > max_len:
                        max_len = k - i + 1
                        max_ind = [i, k]

        return s[max_ind[0]:max_ind[1] + 1]
