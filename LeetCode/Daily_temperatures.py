class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and temp[i] >= temp[st[-1]]:
                st.pop()
            if st and temp[i] < temp[st[-1]]:
                ans[i] = st[-1] - i
            st.append(i)
        return ans
        