class Solution:
    def trap(self, height: List[int]) -> int:
        st = [(0,0)]
        n = len(height)
        for i in range(1,n):
            if height[i-1] > st[-1][0]:
                st.append((height[i-1],i))
        l = 0
        res = 0
        for j in range(n-2,0,-1):
            if height[j+1]>l: l = height[j+1]
            while st[-1][1] > j: st.pop()
            ans = min(l,st[-1][0]) - height[j]
            if ans > 0:
                res+=ans

        return res