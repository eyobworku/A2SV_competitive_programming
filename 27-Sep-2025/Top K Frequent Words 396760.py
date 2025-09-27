# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        arr = [(-x,y) for y,x in count.items()]
        heapify(arr)
        ans = []
        for _ in range(k):
            _,y=heappop(arr)
            ans.append(y)
        return ans 