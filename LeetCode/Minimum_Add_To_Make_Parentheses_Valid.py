class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for x in s:
            if x=='(':
                st.append(x)
            else:
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(x)
        return len(st)