class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(set)
        n = len(bombs)

        for i in range(n):
            xi, yi, ri = bombs[i]

            for j in range(n):
                if i == j: continue
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:#reachableFromI
                    graph[i].add(j)

        def dfs(n, seen):
            if n in seen: return
            seen.add(n)
            for nxt in graph[n]:
                dfs(nxt, seen)

        ans = 0
        for i in range(n):
            seen = set()
            dfs(i, seen)
            ans = max(ans, len(seen))
        return ans        