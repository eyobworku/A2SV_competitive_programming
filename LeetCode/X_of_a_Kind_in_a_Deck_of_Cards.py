class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        res = math.gcd(*list(count.values()))
        return res != 1
