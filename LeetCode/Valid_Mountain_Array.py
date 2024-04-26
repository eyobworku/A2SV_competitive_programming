class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j = 0, len(arr) - 1
        while i < j and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == j:
            return False
            
        while j > i and arr[j - 1] > arr[j]:
            j -= 1

        return i == j