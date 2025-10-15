# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

import sys
# import math
# import  bisect
from collections import defaultdict,deque,Counter
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

x,y = RII()
a = [[0]*x for i in range(x)]
for i in range(y):
    b,c = RII()
    a[b-1][c-1]=a[c-1][b-1]=1
    
u=[-1]*x
u[0]=0
q=deque([0])
while q:
    z=q.popleft()
    for i in range(x):
        if(a[z][i]!=a[0][x-1]) and (u[i]==-1):
            u[i]=u[z]+1
            q.append(i)
print(u[x-1])