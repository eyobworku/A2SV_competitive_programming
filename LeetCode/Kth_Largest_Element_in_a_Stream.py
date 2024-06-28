class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap,self.k = nums,k
        heapify(self.heap)
        n = len(self.heap)
        while n>k:
            heappop(self.heap)
            n-=1

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]