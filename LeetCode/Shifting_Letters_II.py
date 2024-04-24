class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        res=''
        sumi=0
        pre = [0] * (n+1)
        for a,b,c in shifts:
            if c==0:
                c = -1
            pre[a] += c
            pre[b+1] -= c

        for i in range(n):
            sumi+=pre[i]
            ch = ord(s[i]) - 97
            ch = (ch+sumi)%26
            res+=chr(ch+97)
        return res