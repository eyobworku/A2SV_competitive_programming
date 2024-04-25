class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for x, y in ranges:
            for num in range(x, y + 1):
                s.add(num)
    
        for num in range(left, right + 1):
            if num not in s:
                return False
    
        return True