class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        sum = 0
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = 1 + res[i - 1]
        sum = res[n - 1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], 1 + res[i + 1])
            sum += res[i]
        return sum
