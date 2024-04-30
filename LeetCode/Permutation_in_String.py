class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        map1 = Counter(s1)
        map2 = Counter(s2[:n])
        if map1 == map2:return True
        for i in range(n,len(s2)):
            l_ch,r_ch = s2[i-n],s2[i]

            map2[l_ch]-=1
            if map2[l_ch] ==0:del map2[l_ch]

            map2[r_ch]=map2.get(r_ch,0) + 1
            if map1 == map2:return True
        return False
        