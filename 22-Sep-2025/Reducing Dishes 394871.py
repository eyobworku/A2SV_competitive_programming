# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        res = 0
        pre = 0
        for i in satisfaction:
            pre += i
            if pre > 0:
                res += pre
            else:
                break
        return res