class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        for i, num in enumerate(nums):
            if num == 0:
                continue

            # initialize slow and fast pointers
            slow, fast = i, i

            # move slow and fast pointers until they meet or go out of bounds
            while num * nums[fast] > 0 and num * nums[self._advance(nums, fast)] > 0:
                slow = self._advance(nums, slow)
                fast = self._advance(nums, self._advance(nums, fast))

                if slow == fast:
                    if slow == self._advance(nums, slow):
                        break
                    return True

            # set all elements in the cycle to 0
            slow, sign = i, num
            while sign * nums[slow] > 0:
                next = self._advance(nums, slow)
                nums[slow] = 0
                slow = next

        return False

    def _advance(self, nums: List[int], i: int) -> int:
        return (i + nums[i]) % len(nums)