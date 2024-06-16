class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x

        while l <= r:
            m = l + (r-l)//2
            m_squre = m*m

            if m_squre == x: return m
            if m_squre > x:
                r = m-1
            else:
                l = m+1
        return r