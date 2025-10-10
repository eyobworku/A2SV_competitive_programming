# Problem: Count Cells in Overlapping Horizontal and Vertical Substrings - https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/

class Solution:
    def getLPS(self, s: str) -> list:
        n = len(s)
        LPS = [0] * n
        for i in range(1, n):
            j = LPS[i - 1]
            while j > 0 and s[i] != s[j]:
                j = LPS[j - 1]
            if s[i] == s[j]:
                j += 1
            LPS[i] = j
        return LPS
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        n = len(grid)
        m = len(grid[0])
        sz = len(pattern)

        # Create the horizontal string
        horizontalString = ''.join(''.join(row) for row in grid)
        
        # Create the vertical string
        verticalString = ''.join(grid[j][i] for i in range(m) for j in range(n))

        horizontalPatternString = pattern + '#' + horizontalString
        lps1 = self.getLPS(horizontalPatternString)

        verticalPatternString = pattern + '#' + verticalString
        lps2 = self.getLPS(verticalPatternString)

        scan1 = [0] * (len(lps1) + 1)
        for i in range(len(lps1)):
            if lps1[i] == sz:
                scan1[i - sz + 1] += 1
                scan1[i + 1] -= 1

        scan2 = [0] * (len(lps2) + 1)
        for i in range(len(lps2)):
            if lps2[i] == sz:
                scan2[i - sz + 1] += 1
                scan2[i + 1] -= 1

        visited = [[False] * m for _ in range(n)]

        count1 = 0
        for i in range(len(scan1) - 1):
            count1 += scan1[i]
            if count1 > 0:
                idx = i - sz - 1
                if idx >= 0:
                    row = idx // m
                    column = idx % m
                    visited[row][column] = True

        ans = 0
        count2 = 0
        for i in range(len(scan2) - 1):
            count2 += scan2[i]
            if count2 > 0:
                idx = i - sz - 1
                if idx >= 0:
                    row = idx % n
                    column = idx // n
                    if visited[row][column]:
                        ans += 1

        return ans