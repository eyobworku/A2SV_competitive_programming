class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        l = 2**(n-1)
        if k<=l//2:
            return self.kthGrammar(n-1,k)
        
        if n%2==0:
            return 1-self.kthGrammar(n-1,k-(l//2))
        else:
            return self.kthGrammar(n-1,l-k+1)