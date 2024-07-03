import sys
input = lambda:sys.stdin.readline().rstrip()
I = lambda :map(int,input().split())

n, = I()
graph = [[0,0] for _ in range(n)]
for j in range(n):
  li = list(I())
  for i in range(n):
    if li[i]:
      graph[j][0]+=1
      graph[i][1]+=1

sour = []
sink = []
for i in range(n):
  if graph[i][0]==0:
    sink.append(i+1)
  if graph[i][1]==0:
    sour.append(i+1)

print(len(sour),*sour)
print(len(sink),*sink)