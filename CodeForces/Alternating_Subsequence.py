def sign(num):
    return num > 0
 
t = int(input())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n:
        j = i
        maxi = arr[i]
            
        while j < n and sign(arr[i]) == sign(arr[j]):
            maxi = max(maxi, arr[j])
            j += 1
            
        i = j
        ans += maxi
        
    print(ans)