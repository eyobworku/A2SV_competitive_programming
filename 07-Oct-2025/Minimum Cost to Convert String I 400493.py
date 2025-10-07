# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        n = len(original)
        for i in range(n):
            graph[original[i]].append((changed[i],cost[i]))
        def sp(s):
            pq = [(0,s)]
            min_cost = {}
            while pq:
                co,ch = heappop(pq)
                if ch in min_cost:
                    continue
                min_cost[ch] = co
                for nch,nco in graph[ch]:
                    heappush(pq,(co+nco,nch))
            return min_cost
        res = 0
        min_costs = {c:sp(c) for c in set(source)}
        for i in range(len(source)):
            if target[i] not in min_costs[source[i]]:
                return -1
            res+=min_costs[source[i]][target[i]]
        return res
        