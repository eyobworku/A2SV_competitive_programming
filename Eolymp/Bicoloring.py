import sys
input = lambda:sys.stdin.readline().rstrip()
I = lambda :map(int,input().split())

def solve(n):
  col = [-1] *(n+1)
  l, = I()
  res = True
  for _ in range(l):
    a,b = I()
    if col[a] == -1 and col[b] == -1:
      col[a] = 0
      col[b] = 1
    elif col[a] == -1 or col[b] == -1:
      if col[a]==-1:
        col[a] = col[b] ^ 1
      else:
        col[b] = col[a] ^ 1
    elif col[a] == col[b]:
      res = False
  print('BICOLOURABLE.' if res else 'NOT BICOLOURABLE.')

while True:
  n, = I()
  if n:
    solve(n)
  else:
    break