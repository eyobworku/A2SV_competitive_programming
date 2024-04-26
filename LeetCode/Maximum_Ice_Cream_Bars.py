class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs=sorted(costs)
        res=0
        for c in costs:
            if coins >= c:
                coins -=c
                res+=1
            else:
                break
        return res
        