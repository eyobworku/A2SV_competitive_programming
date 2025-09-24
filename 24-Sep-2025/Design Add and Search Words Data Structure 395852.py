# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.tire = {}        

    def addWord(self, word: str) -> None:
        d = self.tire
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        return self.recursiveSearch(self.tire,word,0)

    def recursiveSearch(self,node,word,idx):
        if idx==len(word):
            return "." in node
        if word[idx]==".":
            for x in node:
                if x!='.' and self.recursiveSearch(node[x],word,idx+1):
                    return True
        elif word[idx] in node:
            return self.recursiveSearch(node[word[idx]],word,idx+1)
        return False       


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)