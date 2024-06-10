class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for x in s:
            count[x]+=1
        res = 0
        odd = False
        for x in count.values():
            if x %2:
                odd = True
                x-=1
            res+=x
        if odd: res+=1
        return res