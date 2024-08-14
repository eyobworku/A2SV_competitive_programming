class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {
            "0": "1","1": "2","2": "3","3": "4","4": "5",
            "5": "6","6": "7","7": "8","8": "9","9": "0",
        }
        prev_slot = {
            "0": "9","1": "0","2": "1","3": "2","4": "3",
            "5": "4","6": "5","7": "6","8": "7","9": "8",
        }

        visited = set(deadends)
        q = deque()

        turns = 0

        if "0000" in visited:
            return -1

        q.append("0000")
        visited.add("0000")

        while q:
            l = len(q)
            for _ in range(l):
                current_combination = q.popleft()
                if current_combination == target:
                    return turns

                for i in range(4):
                    new_combination = list(current_combination)
                    new_combination[i] = next_slot[new_combination[i]]
                    new_combination_str = "".join(new_combination)
                
                    if new_combination_str not in visited:
                        q.append(new_combination_str)
                        visited.add(new_combination_str)

                    new_combination = list(current_combination)
                    new_combination[i] = prev_slot[new_combination[i]]
                    new_combination_str = "".join(new_combination)
                    if new_combination_str not in visited:
                        q.append(new_combination_str)
                        visited.add(new_combination_str)

            turns += 1
        return -1