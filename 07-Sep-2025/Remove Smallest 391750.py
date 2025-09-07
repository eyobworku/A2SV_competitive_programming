# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    res = True
    if n > 1:
        for i in range(n-1):
            if a[i+1]-a[i] > 1:
                res = False
                break
    print("YES" if res else "NO")