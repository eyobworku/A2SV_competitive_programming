class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        res = []
        n = len(digits)
        phone = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
        
        def back(combin,l):
            if n == l:
                res.append(combin)
            else:
                for letter in phone[digits[l]]:
                    back(combin+letter,l+1)
        back('',0)
        return res