class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n==1:
            return 1
        
        ans = 2
        dic = Counter(fruits[:2])
        j=0
        for i in range(2,n):
            while fruits[i] not in dic and len(dic) > 1:
                dic[fruits[j]] -=1
                if dic[fruits[j]] == 0:
                    del dic[fruits[j]]
                j+=1
            dic[fruits[i]] = dic.get(fruits[i],0) + 1
            ans = max(ans,i-j+1)
        
        return ans