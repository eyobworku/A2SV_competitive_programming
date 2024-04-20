class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr),0,-1):
            x = arr.index(i)
            if x!=i-1:
                arr1 = arr[:x+1][::-1]
                arr = arr1 + arr[x+1:]
                arr = arr[:i][::-1] + arr[i:]
                ans.append(x+1)
                ans.append(i)
        return ans