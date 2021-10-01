import unittest


class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                        (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()
