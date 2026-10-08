class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = [] # Monotonically decreasing stack
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # only push to stack if item is less than or equal to top
            if not mono_stack or temp <= mono_stack[-1][1]:
                mono_stack.append((i, temp))
            else:
                # keep popping while current is greater than popped item
                while mono_stack and temp > mono_stack[-1][1]:
                    popped = mono_stack.pop()
                    result[popped[0]] = i - popped[0]
                mono_stack.append((i, temp))

        return result
        # [30,38,30,36,35,40,28]
        # [0, 1, 2, 3, 4, 5, 6 ]
        
