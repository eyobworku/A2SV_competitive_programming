class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = {i:0 for i in range(N)}
        def merge(left,right):
            L = len(left)
            R = len(right)
            l = L-1
            r = R-1
            while l > -1 and r > -1:
                if nums[left[l]] > nums[right[r]]:
                    ans[left[l]]+=(r+1)
                    l-=1
                else:
                    r-=1
            l = 0
            r = 0
            res = []
            while l < L and r < R:
                if nums[left[l]] < nums[right[r]]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res.extend(left[l:])
            res.extend(right[r:])
            return res
        def split(l,r,arr):
            if l==r:
                return [arr[r]]

            mid = (l+r)//2
            left = split(l,mid,arr)
            right = split(mid+1,r,arr)
            return merge(left,right)
        split(0,N-1,[i for i in range(N)])
        return ans.values()