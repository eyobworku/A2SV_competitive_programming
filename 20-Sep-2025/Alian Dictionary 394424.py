# Problem: Alian Dictionary - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import deque

class Solution:
    def findOrder(words):
        
        graph = [[] for _ in range(26)]     
        
        inDegree = [0] * 26 
        
        exists = [False] * 26
    
        for word in words:
            for ch in word:
                exists[ord(ch) - ord('a')] = True
    
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            j = 0
            while j < minlen and w1[j] == w2[j]:
                j += 1
    
            if j < minlen:
                u = ord(w1[j]) - ord('a')
                v = ord(w2[j]) - ord('a')
                graph[u].append(v)
                inDegree[v] += 1
            elif len(w1) > len(w2):
                return ""  
    
        q = deque([i for i in range(26) if exists[i] 
                                     and inDegree[i] == 0])
        result = []
    
        while q:
            u = q.popleft()
            result.append(chr(u + ord('a')))
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
    
        if len(result) != sum(exists):
            
            return ""  
    
        return ''.join(result)