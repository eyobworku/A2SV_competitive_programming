from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        strs=sorted(strs)
        fir=strs[0]
        las=strs[-1]
        for i in range(min(len(fir),len(las))):
            if(fir[i]!=las[i]):
                return res
            res+=fir[i]
        return res 
        