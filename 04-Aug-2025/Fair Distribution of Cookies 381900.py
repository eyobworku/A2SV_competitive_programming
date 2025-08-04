# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float('inf')
        children = [0] * k  
        
        def backtrack(i):
            nonlocal res
            if i == len(cookies):
                res = min(res, max(children))
                return
            for j in range(k):
                children[j] += cookies[i]
                
                if max(children) < res:
                    backtrack(i + 1)
                children[j] -= cookies[i]
                
                if children[j] == 0:
                    break

        backtrack(0)
        return res