class Solution:
    def sortColors(self, nums):
        low = 0
        high = len(nums) - 1
        self.mergeSort(nums, low, high)
    
    def mergeSort(self, arr, low, high):
        if low == high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, high, mid)
    
    def merge(self, arr, low, high, mid):
        a = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                a.append(arr[left])
                left += 1
            else:
                a.append(arr[right])
                right += 1
        while left <= mid:
            a.append(arr[left])
            left += 1
        while right <= high:
            a.append(arr[right])
            right += 1
        for i in range(len(a)):
            arr[low + i] = a[i]