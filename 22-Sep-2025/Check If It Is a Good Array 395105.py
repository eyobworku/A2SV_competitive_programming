# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gd = nums[0]
        for num in nums:
            gd=gcd(gd,num)
        return gd == 1