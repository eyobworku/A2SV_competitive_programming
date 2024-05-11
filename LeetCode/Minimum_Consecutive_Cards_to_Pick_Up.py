class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = 10e6
        seen = defaultdict(int)
        for i,card in enumerate(cards):
            if card in seen:
                ans = min(ans,i-seen[card]+1)
            seen[card] = i
        return -1 if ans == 10e6 else ans