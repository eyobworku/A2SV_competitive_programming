class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = "aeiou"
        prev = s[:k]
        temp = 0
        for c in prev:
            if c in vow:
                temp += 1
        maxi = temp
        for i,c in enumerate(s[k:],start=k):
            if c in vow:
                temp += 1
            if s[i - k] in vow:
                temp -= 1
            maxi = max(temp, maxi)
        return maxi