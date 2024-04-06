class Solution:
    def freqAlphabets(self, s: str) -> str:
        jum = 0
        fin_re=''
        res=''
        for i in range(len(s)-1,-1,-1):
            if jum!=0:
                res = str(s[i]) + res
                if jum==2:
                    fin_re = chr(96 + int(res)) + fin_re
                    res=''
                jum = 2 if jum==1 else 0
                continue
            if s[i]=="#":
                jum +=1
                continue
            fin_re = chr(96 + int(s[i])) + fin_re
        return fin_re
        