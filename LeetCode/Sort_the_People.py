class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n-1):
            min_in = i
            for j in range(i+1,n):
                if heights[j] > heights[min_in]:
                    min_in=j
            heights[i], heights[min_in] = heights[min_in], heights[i]
            names[i], names[min_in] = names[min_in], names[i]
        return names