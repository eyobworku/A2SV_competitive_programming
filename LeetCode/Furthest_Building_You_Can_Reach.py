class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        ans = 0
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                gap = heights[i] - heights[i-1]
                if ladders > 0:
                    ladders-=1
                    heappush(arr,gap)
                elif arr and arr[0] < gap and arr[0] <= bricks:
                    x = heappop(arr)
                    bricks-=x
                    heappush(arr,gap)
                elif gap <= bricks:
                    bricks-=gap
                else:
                    break
            ans = i
        return ans