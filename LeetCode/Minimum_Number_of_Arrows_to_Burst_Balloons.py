class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 1
        pos = points[0][1]
        for point in points:
            if point[0] <= pos:
                continue
            res += 1
            pos = point[1]
        return res