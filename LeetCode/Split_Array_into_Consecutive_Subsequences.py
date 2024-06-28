class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        arr = []
        for x in nums:
            while arr and (x>(arr[0][0]+1)):
                _,l= heapq.heappop(arr)
                if l<3:
                    return False

            if arr and arr[0][0] == x-1:
                y,l = heappop(arr)
                heappush(arr,(x,l+1))
            else:
                heappush(arr,(x,1))

        for a in arr:
            if a[1] < 3:
                return False
        return True