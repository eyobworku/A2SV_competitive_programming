class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ac = Counter(arr1)
        arr1 = []
        for x in arr2:
            arr1 = arr1 + [x] * ac[x]
            del ac[x]
        sac = sorted(x for x in ac.keys())
        for x in sac:
            arr1 = arr1 + [x] * ac[x]
        return arr1 
        