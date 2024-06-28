class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left==1:left+=1
        def primeInrange(limit):#sieve_of_eratosthenes
            primes = []
            sieve = [True] * (limit + 1)
            p = 2

            while p * p <= limit:
                if sieve[p] == True:
                    for i in range(p * p, limit + 1, p):
                        sieve[i] = False
                p += 1
            for p in range(left, limit + 1):# range(2,limit+1)
                if sieve[p]:
                    primes.append(p)

            return primes
        primes = primeInrange(right)
        if len(primes) < 2:
            return [-1,-1]
        else:
            dis = primes[1] - primes[0]
            res = [primes[0],primes[1]]
            for i in range(2,len(primes)):
                if primes[i] - primes[i-1] < dis:
                    dis = primes[i] - primes[i-1]
                    res = [primes[i-1],primes[i]]
            return res