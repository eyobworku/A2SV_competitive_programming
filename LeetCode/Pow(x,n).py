class Solution:
    def solve(self, x, n):
        if n == 0:
            return 1 
        
        temp = self.myPow(x, n // 2)
        temp = temp * temp
        
        if n % 2 == 0:
            return temp
        else:
            return temp * x  
    
    def myPow(self, x, n):
        ans = self.solve(x, abs(n))
        if n < 0:
            return 1 / ans
        return ans