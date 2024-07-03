class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x1 , x2 = edges[0][0],edges[0][1]
        if edges[1][0] == x1 or edges[1][1] == x1:
            return x1
        return x2