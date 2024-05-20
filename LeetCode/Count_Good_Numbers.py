class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        odd = n//2
        even = n//2 + n%2
        def pow(x,n):
            res = 1
            while n > 0:
                if n==0:
                    return res
            
                if n%2==1:
                    res = (res * x) %mod
                x = (x * x)%mod
                n >>= 1
            return res
        
        return (pow(5,even)%mod * pow(4,odd)%mod)%mod