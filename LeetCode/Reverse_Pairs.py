class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def merge(left,right):
            L,R=len(left),len(right)
            l,r = L-1,R-1
            while l > -1 and r > -1:
                if left[l] > (2*right[r]):
                    self.count += (r+1)
                    l-=1
                else:
                    r-=1
            l,r=0,0
            res = []
            while l < L and r < R:
                if left[l] < right[r]:
                    res.append(left[l])
                    l+=1
                else:
                    res.append(right[r])
                    r+=1
            res.extend(left[l:])
            res.extend(right[r:])
            return res

        def divide(i,j):
            if i==j: return [nums[j]]
            m = (i+j)//2
            left = divide(i,m)
            right = divide(m+1,j)
            return merge(left,right)
        divide(0,len(nums)-1)
        return self.count