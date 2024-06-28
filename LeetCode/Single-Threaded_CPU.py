class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(tasks[i][0],tasks[i][1],i) for i in range(len(tasks))]
        tasks.sort()
        heap = []
        ans = []
        time = 0
        print(tasks)
        for e,p,i in tasks:
            while heap and e > time:
                pt,inx = heappop(heap)
                ans.append(inx)
                time+=pt
            heappush(heap,(p,i))
            time = max(time,e)
        while heap:
            pt,inx = heappop(heap)
            ans.append(inx)
        return ans