class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res,Q,n = [],[],len(nums2)

        for x in nums1:
            heappush(Q, [x + nums2[0], 0])

        while k > 0 and Q:
            pair = heappop(Q)
            s, inx = pair[0], pair[1]  
            res.append([s - nums2[inx], nums2[inx]]) 

            if inx + 1 < n:
                heappush(Q, [s - nums2[inx] + nums2[inx + 1], inx + 1])

            k -= 1

        return res 