class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces += [len(s), 0]
        return " ".join(s[spaces[i-1]:spaces[i]] for i in range(len(spaces)-1))