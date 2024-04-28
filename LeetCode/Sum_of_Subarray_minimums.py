class Solution:
    def sumSubarrayMins(self, arr):
        l = [0] * len(arr)
        for i in range(len(arr)):
            l[i] = i - 1
            while l[i] > -1 and arr[i] < arr[l[i]]: l[i] = l[l[i]]

        r = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            r[i] = i + 1
            while r[i] < len(arr) and arr[i] <= arr[r[i]]: r[i] = r[r[i]]
        print(l,r)
        rs = 0
        for i in range(len(arr)):
            rs=(i - l[i]) * (r[i] - i)
            print(i,rs)
        m = 10**9 + 7
        res = sum((i - l[i]) * (r[i] - i) * arr[i] for i in range(len(arr))) % m
        return res