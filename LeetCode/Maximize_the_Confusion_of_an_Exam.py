class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        cs = Counter(s[:k])
        maxi = k
        i , j = 0,k
        while j < len(s):
            cs[s[j]] +=1
            if len(cs) == 2 and min(cs.values()) > k:
                cs[s[i]] -=1
                i+=1
            maxi = max(maxi,j-i+1)
            j+=1
        return maxi