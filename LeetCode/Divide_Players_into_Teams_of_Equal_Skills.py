class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        result = 0
        pair = skill[0] + skill[n-1]
        i = 0
        j = n-1
        while i < j:
            if skill[i] + skill[j] == pair:
                temp = skill[i] * skill[j]
                result += temp
                i += 1
                j -= 1
            else:
                return -1

        return result