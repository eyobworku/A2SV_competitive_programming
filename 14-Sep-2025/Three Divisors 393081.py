# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        nums  = set()
        for i in range(1, int(math.sqrt(n))+1):
            if n %i ==0:
                nums.add(i)
                nums.add(n//i)
        return len(nums)==3