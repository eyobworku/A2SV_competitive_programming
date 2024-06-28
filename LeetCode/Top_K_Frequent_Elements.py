class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, r, pivot) -> int:
            pivot_frequency = count[unique[pivot]]#Move z pivot to end
            unique[pivot], unique[r] = unique[r], unique[pivot]  
            stor_idx = left #Move all less frequent elements to the left
            for i in range(left, r):
                if count[unique[i]] < pivot_frequency:
                    unique[stor_idx], unique[i] = unique[i], unique[stor_idx]
                    stor_idx += 1

            # 3. Move the pivot to its final place
            unique[r], unique[stor_idx] = unique[stor_idx], unique[r]  
            return stor_idx
        
        def quickselect(left, right, k_smallest) -> None:
            if left == right: 
                return
            pivot_index = random.randint(left, right)# Select a random pivot 
                            
            # Find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # If the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            elif k_smallest < pivot_index: # go left
                quickselect(left, pivot_index - 1, k_smallest)
            else:# go right
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique) 
        quickselect(0, n - 1, n - k)
        return unique[n - k:]