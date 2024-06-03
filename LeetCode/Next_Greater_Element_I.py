class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict(int) 
        for i in range(len(nums1)):
            d[nums1[i]]=i 
            
        stack = []
        ans = [0]*len(nums1) 
        for j in range(len(nums2)-1,-1,-1):
            if nums2[j] in d:
                if stack==[]:
                    ans[d[nums2[j]]]=-1 
                elif stack!=[] and stack[-1]>nums2[j]:
                    ans[d[nums2[j]]]=stack[-1] 
                elif stack!=[] and stack[-1]<=nums2[j]:
                    while stack!=[] and stack[-1]<=nums2[j]:
                        stack.pop() 
                    if stack==[]:
                        ans[d[nums2[j]]]=-1 
                    else:
                        ans[d[nums2[j]]]=stack[-1]
            stack.append(nums2[j]) 
        return ans