class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = [] # Monotonically decreasing stack
        # only push to stack if item is less than or equal to
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            # next_t = temperatures[i+1]

            if not mono_stack or temp <= mono_stack[-1][1]:
                mono_stack.append((i, temp))
            else:
                # keep popping while current is greater than popped item
                while mono_stack and temp > mono_stack[-1][1]:
                    popped = mono_stack.pop()
                    result[popped[0]] = i - popped[0]
                mono_stack.append((i, temp))

        return result




                # popped = mono_stack.pop()
                # # popped_i = popped[0]
                # popped_temp = popped[1]

                
                # # result is difference between input index of popped
                # result[i] = popped[0] - mono_stack[-1][0]
        # [30,38,30,36,35,40,28]
        # [0, 1, 2, 3, 4, 5, 6 ]
        
