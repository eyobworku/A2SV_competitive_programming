# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int,input().split()))
n = int(input())
res = True
for i in range(n):
    b = set(map(int,input().split()))
    if not a.issuperset(b):
        res = False

print(res)
