class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []

    def addNum(self, num: int) -> None:
        if self.minH and num >= self.minH[0]:
            heappush(self.minH, num)
            while len(self.minH)>len(self.maxH):
                x = heappop(self.minH)
                heappush(self.maxH,-x)
        else:
            heappush(self.maxH,-num)
            while len(self.maxH)>len(self.minH)+1:
                x = -heappop(self.maxH)
                heappush(self.minH,x)

    def findMedian(self) -> float:
        if len(self.maxH) > len(self.minH):
            return -float(self.maxH[0])
        else:
            return (-self.maxH[0] + self.minH[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()