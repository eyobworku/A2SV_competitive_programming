class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        visted = set()
        q.append(0)
        while q:
            room = q.popleft()
            if room not in visted:
                visted.add(room)
                for r in rooms[room]:
                    q.append(r)
        return len(visted) == len(rooms)