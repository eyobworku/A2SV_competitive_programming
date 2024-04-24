def sieve(upto):
    p = [True] * (upto + 1)
    p[0] = False
    p[1] = False
    for i in range(2, int(upto ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, upto + 1, i):
                p[j] = False
    return p

def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

def main():
    n = int(input())
    primes = sieve(1000000)

    ans = [0] * 1000001
    s = 0
    for k in range(1000001):
        if primes[k] and primes[digit_sum(k)]:
            s += 1
        ans[k] = s
        
    #for i in range(1,101):
     #   if ans[i] > ans[i-1]:
      #      print(i,ans[i])

    for _ in range(n):
        t1, t2 = map(int, input().split())
        s = ans[t2] - ans[t1]
        if primes[t1] and primes[digit_sum(t1)]:
            s += 1
        print(s)

main()
#print(sieve(100))
