# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            l = nums[i]
            for j in range(i, n):  
                l = lcm(l,nums[j])
                if l == k:
                    res += 1
                if l > k:
                    break
            
        return res