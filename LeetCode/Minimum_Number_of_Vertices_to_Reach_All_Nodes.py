class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inc = [0] * n
        for x,y in edges:
            inc[y]+=1

        ans = []
        for i in range(n):
            if inc[i] == 0:
                ans.append(i)
        return ans