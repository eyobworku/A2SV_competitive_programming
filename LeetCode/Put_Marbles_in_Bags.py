class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:   
        n = len(weights)
        pair_w = [0] * (n - 1)
        for i in range(n - 1):
            pair_w[i] = weights[i] + weights[i + 1]
        pair_w.sort()

        ans = 0
        for i in range(k - 1):
            ans += pair_w[n - 2 - i] - pair_w[i]
            
        return ans