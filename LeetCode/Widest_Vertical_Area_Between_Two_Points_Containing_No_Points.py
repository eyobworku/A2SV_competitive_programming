class Solution:
    def maxWidthOfVerticalArea(self, points):
        arr = [point[0] for point in points]
        arr.sort()
        res = 0
        for i in range(1, len(arr)):
            res = max(res, arr[i] - arr[i - 1])

        return res