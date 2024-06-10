class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = Counter(answers)
        res = 0
        for x,y in s.items():
            res+= ceil(y/(x+1)) * (x+1)
        
        return res