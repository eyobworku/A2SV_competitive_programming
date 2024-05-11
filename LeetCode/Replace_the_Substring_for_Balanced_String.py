class Solution:
    def balancedString(self, s: str) -> int:
        res = len(s)
        dic = Counter(s)
        extra={}
        n = len(s)//4

        for c in dic:
            if dic[c] > n: extra[c] = dic[c]-n
        distincts = len(extra)
        if not extra: return 0
        i=0
        for j in range(len(s)):
            if s[j] in extra: 
                extra[s[j]] -= 1

                if extra [s[j]] == 0: distincts -= 1
            
            while distincts == 0:
                res = min(res, j - i + 1)
                if s[i] in extra:
                    extra[s[i]] += 1
                    
                    if extra [s[i]] == 1: distincts += 1 
                i += 1

        return res
        