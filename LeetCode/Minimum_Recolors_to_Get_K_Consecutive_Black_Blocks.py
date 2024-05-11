class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        dic = Counter(blocks[:k])
        ans = dic['W']
        j = 0
        for i in range(k,n):
            dic[blocks[i]]+=1
            dic[blocks[j]]-=1
            j+=1
            ans = min(ans,dic['W'])
        return ans