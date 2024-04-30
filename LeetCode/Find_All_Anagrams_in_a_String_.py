class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        pc = Counter(p)
        sc = Counter(s[:n])
        res = []
        j=0
        if pc == sc:
            res.append(j)

        for i in range(n,len(s)):
            sc[s[i]] = sc.get(s[i],0)+1
            sc[s[j]] -=1
            if sc[s[j]]==0:
                del sc[s[j]]
            j+=1
            if pc == sc:
                res.append(j)
        
        return res