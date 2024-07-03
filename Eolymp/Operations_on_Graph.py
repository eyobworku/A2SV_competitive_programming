from collections import defaultdict

n = int(input())
li = defaultdict(list)
for _ in range(int(input())):
    a = list(map(int,input().split()))
    if a[0]==1:
      li[a[1]].append(a[2])
      li[a[2]].append(a[1])
    else:
      if li[a[1]]:
        print(*li[a[1]])