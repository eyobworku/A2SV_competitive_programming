n,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
 
ans=[]
l=0
r=0
while l < len(arr1) and r < len(arr2):
    if arr1[l] <= arr2[r]:
        ans.append(arr1[l])
        l +=1
    else:
        ans.append(arr2[r])
        r+=1
ans.extend(arr1[l:])
ans.extend(arr2[r:])
print(*ans)