# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        MAX_ = 10000
        def build_prime(n):
            tmp, primes = [True] * MAX_, []
            for num in range(2, MAX_-1):
                if tmp[num] == False: continue
                primes.append(num)
                t_num = num * num
                while t_num < MAX_:
                    tmp[t_num] = False
                    t_num += num
            return primes
        
        def variations(num):
            variants = []
            s = str(num)
            for i in range(len(s)):
                c_n = int(s[i])
                if c_n < 9:
                    variants.append(int(s[:i]+str(c_n+1)+s[i+1:]))
                if c_n > 0:
                    variants.append(int(s[:i]+str(c_n-1)+s[i+1:]))
            return variants
                

        primes = set(build_prime(max(n, m)))
        
        if n in primes or m in primes:
            return -1

        distance = [math.inf] *MAX_
        heap = [(n, n)]
        while heap:
            total, num = heapq.heappop(heap)
            if num in primes:
                continue
            if total >= distance[num]:
                continue
            if num == m:
                return total
            distance[num] = total
            for n_num in variations(num):
                heapq.heappush(heap, (total+n_num, n_num))

        return -1