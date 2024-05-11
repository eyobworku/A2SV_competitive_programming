class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        wind = ans = sum(cardPoints[:k])

        for i in range(k):
            wind = wind - cardPoints[k-i-1] + cardPoints[n-i-1]
            ans = max(ans,wind)
        
        return ans