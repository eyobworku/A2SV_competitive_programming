class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=''
        for d in s:
            if ord(d)<123 and ord(d)>96:
                res+=d
            elif d in '0123456789':
                res+=d
        i = 0
        j = len(res)-1
        print(res)
        while i < j:
            if res[i] == res[j]:
                i+=1
                j-=1
            else:
                return False
        return True