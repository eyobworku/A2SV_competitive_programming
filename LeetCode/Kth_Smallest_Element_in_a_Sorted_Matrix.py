class Solution:
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
                print('c',c)
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1 #try to looking for a smaller value in left
            else:
                left = mid + 1 #try to looking for a bigger value in right

        return ans