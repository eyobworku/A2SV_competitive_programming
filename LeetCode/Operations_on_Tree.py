class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [0] * len(parent)
        self.graph = defaultdict(list)
        for i in range(len(parent)): self.graph[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != 0: return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user: return False
        self.locked[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != 0: return False
        if not self.have_locked_desc(num): return False
        if self.have_locked_ances(num): return False
        self.lock(num, user)

        stack = [num for num in self.graph[num]]
        while stack:#unlock all desc
            node = stack.pop()
            self.locked[node] = 0
            stack.extend(self.graph[node])

        return True

    def have_locked_desc(self, num: int) -> bool:
        stack = [n for n in self.graph[num]]
        while stack:
            node = stack.pop()
            if self.locked[node] != 0: return True
            stack.extend(self.graph[node])
        return False


    def have_locked_ances(self, num: int) -> bool:
        while self.parent[num] != -1:
            if self.locked[self.parent[num]] != 0: return True
            num = self.parent[num]
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)