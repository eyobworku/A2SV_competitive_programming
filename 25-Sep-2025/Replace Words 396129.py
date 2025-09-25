# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tire  = {}
        for word in dictionary:
            d = tire
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['.'] = '.'
        sentence = sentence.split()
        res = []
        for word in sentence:
            node = tire
            i = 0
            myword = ''
            while i < len(word):
                if word[i] in node:
                    myword+=word[i]
                    node = node[word[i]]
                    i+=1
                    if '.' in node:
                        break
                else:
                    myword=word
                    break
            if myword=='' or len(myword)>len(word):
                res.append(word)
            else:
                res.append(myword)
            
        return ' '.join(res)