n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ans=[]
l=0
for i in range(m):
    while l < n and arr2[i] > arr1[l]:
        l+=1
    ans.append(l)
print(*ans)