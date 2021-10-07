class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        dp = [0] * len(s)

        for idx in range(1, len(s)):
            if s[idx] == ")":
                if s[idx - 1] == "(":
                    if idx >= 2:
                        dp[idx] = dp[idx - 2] + 2
                    else:
                        dp[idx] = 2
                else:
                    matching_idx = idx - 1 - dp[idx - 1]
                    if matching_idx >= 0 and s[matching_idx] == "(":
                        if matching_idx >= 1:
                            dp[idx] = dp[idx - 1] + 2 + dp[matching_idx - 1]
                        else:
                            dp[idx] = dp[idx - 1] + 2

        return max(dp)
