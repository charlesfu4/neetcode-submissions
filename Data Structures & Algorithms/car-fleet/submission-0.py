class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ps_sets = []

        for i in range(len(position)):
            ps_sets.append((position[i], speed[i]))
        
        ps_sets.sort(reverse=True)

        stack = []

        for p, s in ps_sets:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
