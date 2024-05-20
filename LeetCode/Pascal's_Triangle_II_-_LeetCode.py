class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mp = {}

        def help(n, r):
            if n < 2 or r == 0 or r == n:
                return 1
            if (n - 1, r - 1) in mp:
                f = mp[(n - 1, r - 1)]
            else:
                f = help(n - 1, r - 1)
                mp[(n - 1, r - 1)] = f

            if (n - 1, r) in mp:
                s = mp[(n - 1, r)]
            else:
                s = help(n - 1, r)
                mp[(n - 1, r)] = s
            return f + s

        res = []
        for i in range(rowIndex + 1):
            res.append(help(rowIndex, i))

        return res
