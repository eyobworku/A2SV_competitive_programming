class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        n = len(palindrome)

        for i in range(n//2):
            if ord(palindrome[i]) != 97:
                return palindrome[:i]+'a'+palindrome[i+1:]
    
        return palindrome[:n-1]+'b'