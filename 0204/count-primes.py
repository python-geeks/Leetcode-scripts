
# I have used sieve of erato algorithm to solve this problem

def seive(Max):
    primes = []
    isprime = [False] * (Max)
    maxN = Max
    if maxN < 2:
        return 0
    if maxN >= 2:
        isprime[0] = isprime[1] = True
    for i in range(2, maxN):
        if (isprime[i] is False):
            for j in range(i * i, maxN, i):
                isprime[j] = True
    for i in range(Max):
        if isprime[i] is False:
            primes.append(i)
    return len(primes)


class Solution:
    def countPrimes(self, n: int) -> int:
        return seive(n)
