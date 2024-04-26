class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for row in image:
            res.append([1 ^ i for i in reversed(row)])
        return res