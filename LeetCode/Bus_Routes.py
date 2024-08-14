class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        m = defaultdict(set)
        for i, route in enumerate(routes):
            for node in route:
                m[node].add(i)
                
        ans = -1
        vis = set()
        q = deque([source])
        while q:
            ans += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return ans
                for bus in m[cur]:
                    if bus not in vis:
                        vis.add(bus)
                        q.extend(routes[bus])
        return -1