# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        sb = a

        while len(sb) < len(b):
            sb += a
            count += 1

        if b in sb:
            return count

        if b in sb + a:
            return count + 1

        return -1