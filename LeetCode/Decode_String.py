class Solution:
    def decodeString(self, s: str) -> str:
        if not s: 
            return ""
        i = 0 # pointer to go through string
        start = "" # characters at the start of the string
        while s[i].isalpha():
            start += s[i]
            i += 1
            if i == len(s):
                return start
        k = "" # k -- the number of times to repeat the next segment
        while s[i].isdigit():
            k += s[i]
            i += 1
        j = i+1 # we must have hit a "[", so skip past it
        num = 1 # number of open "["
        while num: # while there is a "[" open
            j += 1
            num = num + (s[j] == "[") - (s[j] == "]") # add to num if we find a "[", subtract if we find a "]"
        return start + int(k) * self.decodeString(s[i+1:j]) + self.decodeString(s[j+1:]) 
        