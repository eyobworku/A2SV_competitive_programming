import sys
input = lambda:sys.stdin.readline().rstrip()
I = lambda:list(map(int,input().split()))

def solve(l, r):
    if r - l == 1:
        return 0
    
    mid = (l + r) // 2
    mal = max(arr[l:mid])
    mar = max(arr[mid:r])
    ans = 0
    
    if mal > mar:
        ans += 1
        for i in range(mid - l):
            arr[l + i], arr[mid + i] = arr[mid + i], arr[l + i]
    
    return solve(l, mid) + solve(mid, r) + ans

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    ans = solve(0, m)
    if arr == sorted(arr):
        print(ans)
    else:
      print(-1)