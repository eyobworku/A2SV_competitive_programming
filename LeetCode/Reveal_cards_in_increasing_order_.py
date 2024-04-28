class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        dq = deque()
        n = len(deck)
        dq.appendleft(deck[0])
        print(dq)
        for i in range(1, n):
            x = dq.pop()
            print(x)
            dq.appendleft(x)
            dq.appendleft(deck[i])
            print(dq)
        return list(dq)