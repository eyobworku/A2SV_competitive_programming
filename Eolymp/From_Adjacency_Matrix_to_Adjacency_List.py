import sys
from collections import defaultdict
input = lambda:sys.stdin.readline().rstrip()
I = lambda :map(int,input().split())

n, = I()
graph = defaultdict(list)
for j in range(n):
  li = list(I())
  for i in range(n):
    if li[i]:
      graph[j].append(i+1)


for i in range(n):
  print(len(graph[i]),*graph[i])