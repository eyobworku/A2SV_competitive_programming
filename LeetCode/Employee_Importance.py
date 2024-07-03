"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {}
        for i in range(len(employees)):
            emp[employees[i].id] = [employees[i].importance,employees[i].subordinates]
        def dfs(id):
            return emp[id][0] + sum(dfs(i) for i in emp[id][1])
        
        return dfs(id)