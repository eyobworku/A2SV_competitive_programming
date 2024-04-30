class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            interval1 = firstList[i]
            interval2 = secondList[j]
            start = max(interval1[0], interval2[0])
            end = min(interval1[1], interval2[1])
            if start <= end:
                res.append([start,end])
            if interval1[1] < interval2[1]:
                i += 1
            else:
                j += 1

        return res