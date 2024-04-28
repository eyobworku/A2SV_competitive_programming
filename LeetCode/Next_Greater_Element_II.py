class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vec = [0] * n
        st = list(reversed(nums[:-1]))
        
        for i in range(n-1, -1, -1):
            if not st:
                vec[i] = -1
            elif nums[i] < st[-1]:
                vec[i] = st[-1]
            elif nums[i] >= st[-1]:
                while st and nums[i] >= st[-1]:
                    st.pop()
                if not st:
                    vec[i] = -1
                else:
                    vec[i] = st[-1]
            st.append(nums[i])
        
        return vec