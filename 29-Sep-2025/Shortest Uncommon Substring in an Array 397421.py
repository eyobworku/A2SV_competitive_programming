# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = set()
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word,num):
        lengh = len(word)
        for i in range(lengh):
            cur = self.root
            for j in word[i:]:
                if j not in cur.children:
                    cur.children[j] = TrieNode()
                cur = cur.children[j]
                cur.isWord.add(num)
    def find(self,word):
        lengh = len(word)
        ans = []
        for i in range(lengh):
            cur = self.root
            cur_str = ''
            for j in word[i:]:
                cur_str += j
                cur = cur.children[j]
                if len(cur.isWord) == 1:
                    ans.append(cur_str)
                    break
        return sorted(ans,key=lambda x:(len(x),x))[0] if ans else ''
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        t = Trie()
        for idx,word1 in enumerate(arr):
            t.insert(word1,idx)

        ans = []
        for word2 in arr:
            ans.append(t.find(word2))
        return ans