# Enter your code here. Read input from STDIN. Print output to STDOUT
int(input())
eng = set(map(int,input().split()))
int(input())
fre = set(map(int,input().split()))
res = eng.union(fre)

print(len(res))
