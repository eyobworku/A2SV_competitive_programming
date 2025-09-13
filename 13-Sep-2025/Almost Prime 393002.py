# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

from math import sqrt


def check(num):
    i=2
    count=0
    while i<=sqrt(num):
        if num%i==0:
            count+=1
            while num%i==0:
                num=num//i
        i+=1
    if num>1:
        count+=1
    return count
def check2(num):
    count2=0
    for i in range(2,num+1):
        if check(i)==2:
            count2+=1
    return count2        
    
num=int(input())
print(check2(num))
    