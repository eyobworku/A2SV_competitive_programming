# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def l(x):
  return 0 if x&1 else l(x//2)+1
for _ in range(int(input())):
  n=int(input())
  s=sum([l(int(x))for x in input().split()])
  o=list(sorted(map(l,range(1,n+1))))
  i=n
  a=0
  while s<n and i:
    i-=1
    s+=o[i]
    a+=1
  print(-1 if s<n else a)