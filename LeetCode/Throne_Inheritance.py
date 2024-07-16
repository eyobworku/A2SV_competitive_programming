class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
	    self.root[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        visted = set()
        inher = []
        
        if self.king not in self.dead:
            inher.append(self.king)

        def dfs(par):
            if par not in visted:
                visted.add(par)
                for ch in self.root[par]:
                    if ch not in self.dead:
                        inher.append(ch)
                    dfs(ch)
        dfs(self.king)
        return inher

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()