class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        N = len(nums)
        ans = {i:[0 ,0] for i in range(N)}

        def merge(left , right):
            L,R = len(left),len(right)
            l = L-1
            r = R-1
            while l > -1 and r > -1:
                if nums[left[l]] <= nums[right[r]]:
                    ans[right[r]][1] += ((L-1) - l)
                    r -= 1
                else:
                    l -= 1

            while r > -1:
                ans[right[r]][1] += L 
                r -= 1  

            l = 0
            r = 0
            res = []
            while l < L and r < R:
                if nums[left[l]] < nums[right[r]]:
                    res.append(left[l])
                    l += 1
                else:
                    ans[right[r]][0] += l
                    res.append(right[r])
                    r += 1
            while r < R:
                ans[right[r]][0] += l
                res.append(right[r])
                r += 1

            res.extend(left[l:])
            return res
            
        def split(l , r , arr):
            if l == r:
                return [arr[r]]
            
            mid = (l+r)//2

            left = split(l , mid , arr)
            right = split(mid+1 , r , arr)

            return merge(left , right)
        split(0 , N-1 , [i for i in range(N)])

        real_ans = 0
        for i in ans.keys():
            real_ans += min(ans[i])
        return real_ans % ((10**9) + 7)