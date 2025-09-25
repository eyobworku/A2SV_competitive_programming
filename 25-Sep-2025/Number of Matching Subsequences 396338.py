# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        tire  = {'.':0}
        for word in words:
            d = tire
            for c in word:
                if c not in d:
                    d[c] = {'.':0}
                d = d[c]
            d['.'] +=1
        q = deque([(0, tire)])

        result = 0
        while q:
            i, node = q.popleft()
            if node['.'] > 0:
                result += node['.']
                node['.'] = 0  

            for c in node.keys():
                idx = s.find(c , i)
                if idx != -1:
                    q.append((idx + 1, node[c]))
                    
        return result
