# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        max_l = len(bin(max(nums)))-2
        for i in range(max_l)[::-1]:
            ans <<=1
            prefixes = {num >> i for num in nums}
            ans += any(ans^1 ^ p in prefixes for p in prefixes)
        return ans