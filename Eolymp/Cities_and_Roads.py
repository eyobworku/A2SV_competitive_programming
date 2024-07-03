import sys
input = lambda:sys.stdin.readline().rstrip()
I = lambda :map(int,input().split())

n, = I()
ro = 0
for j in range(n):
  li = list(I())
  for i in range(n):
    if li[i]:
      ro+=1

print(ro//2)