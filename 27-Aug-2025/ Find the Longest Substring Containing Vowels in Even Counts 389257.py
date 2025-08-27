# Problem:  Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_bit = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        mask = 0
        pos = {0: -1} 
        length = 0
        
        for i, ch in enumerate(s):
            if ch in vowel_bit:
                mask ^= vowel_bit[ch]
            
            if mask in pos:
                length = max(length, i - pos[mask])
            else:
                pos[mask] = i
        return length