# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        pre = defaultdict(set)
        inco = [0] * n

        for a,b in prerequisites:
            graph[a].append(b)
            inco[b]+=1
        q = deque([i for i in range(n) if inco[i] == 0])
        
        while q:
            cou = q.popleft()
            for nx in graph[cou]:
                pre[nx].add(cou)
                pre[nx].update(pre[cou])
                inco[nx]-=1
                if inco[nx] == 0: q.append(nx)
        ans = []
        for x,y in queries:
            ans.append(x in pre[y])
        return ans

