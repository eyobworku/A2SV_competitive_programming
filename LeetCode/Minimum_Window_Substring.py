class Solution:
    def minWindow(self, s: str, t: str) -> str:
            k=Counter(t)
            l,r,minLen,si,c=0,0,10**100,-1,0

            while r<len(s):
                if s[r] not in k:k[s[r]]=0
                if k[s[r]]>0 : c+=1
                k[s[r]] -= 1
                while c==len(t):
                    if r-l+1 < minLen:
                        minLen= r-l+1
                        si=l
                    k[s[l]] +=1
                    if k[s[l]]>0:c-=1
                    l+=1
                r+=1
            if si==-1:
                return ""
            return s[si:si+minLen]