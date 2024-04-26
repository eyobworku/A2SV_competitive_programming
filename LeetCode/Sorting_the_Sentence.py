class Solution:
    def sortSentence(self, s: str) -> str:
        ar = s.split()
        ar.sort(key=lambda x:x[-1])
        return ' '.join([x[:-1] for x in ar])
        