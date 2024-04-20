class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winer = set()
        loser= {}
        for n in matches:
            winer.add(n[0])
            loser[n[1]] = loser.get(n[1],0) + 1
        print(winer,loser)
        win =[]
        lose=[key for key, value in loser.items() if value == 1]
        for i in winer:
            if not loser.get(i):
                win.append(i)
        return [sorted(win),sorted(lose)]