# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kthGrammarZeroIndexed(y):
            if y == 0:
                return 0
            if y % 2 == 0:
                return kthGrammarZeroIndexed(y >> 1)
            else:
                return 0 if kthGrammarZeroIndexed(y >> 1) == 1 else 1
        return kthGrammarZeroIndexed(k-1)