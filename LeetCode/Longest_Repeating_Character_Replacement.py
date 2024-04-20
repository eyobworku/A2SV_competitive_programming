class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        res=0
        n,j = len(s),0
        for i in range(n):
            ch = s[i]
            count[ch] = count.get(ch, 0) + 1
            val = dic.values()
            if sum(val) - max(val) <= k:
                res=max(res,i-j+1)
            else:
                ch2=s[j]
                dic[ch2]-=1
                j+=1
        return res

        