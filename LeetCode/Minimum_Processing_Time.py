class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxi = 0
        for i,x in enumerate(processorTime):
            maxi = max(maxi,x+tasks[i*4])
        return maxi
        