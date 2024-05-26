class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=t=0
        for b in bills:
            if b==5:
                f+=1
            elif b==10:
                if f < 1:
                    return False
                t+=1
                f-=1
            else:
                if f>0 and t>0:
                    t-=1
                    f-=1
                elif f>2:
                    f-=3
                else:
                    return False
        return True
                
        