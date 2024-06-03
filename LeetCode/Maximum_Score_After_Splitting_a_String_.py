class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        pz = [0] * (n+1)
        for i in range(n):
            if s[i]=='0':
                pz[i+1] = pz[i]+1
            else:
                pz[i+1]=pz[i]
                
        r = 0
        po = 1 if s[-1]=='1' else 0
        for i in range(n-2,-1,-1): 
            r = max(r,pz[i+1]+po)
            if s[i]=='1':
                po+=1
        return r