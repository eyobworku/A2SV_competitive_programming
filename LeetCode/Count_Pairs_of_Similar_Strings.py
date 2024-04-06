class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wdic = collections.defaultdict(set)
        for idx, wd in enumerate(words):
            wdic[idx] = set(wd)
        
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(wdic[i].symmetric_difference(wdic[j])) == 0:
                    ans += 1
        return ans