class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x!=0 and x%10 ==0 :
            return False
        dig = [int(d) for d in str(x)]
        res = False
        j = len(dig)-1
        for i in range(len(dig)):
            if dig[i] == dig[j]:
                res = True
            else:
                return False
            j-=1
            if i+1 >= j:
                return res
            