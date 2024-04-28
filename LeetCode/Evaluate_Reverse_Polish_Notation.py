class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for x in tokens:
            if x in ("+", "-", "*", "/"):
                b = st.pop()
                a = st.pop()
                if x == "+":
                    res = a + b
                elif x == "-":
                    res = a - b
                elif x == "*":
                    res = a * b
                else:
                    res = math.trunc(a / b)
                st.append(res)
            else:
                st.append(int(x))
        return st[0]