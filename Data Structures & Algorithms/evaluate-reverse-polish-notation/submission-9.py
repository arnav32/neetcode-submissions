class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            elif len(stack) >= 2:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if t == "+":
                    stack.append(num2 + num1)
                elif t == "-":
                    stack.append(num2 - num1)
                elif t == "*":
                    stack.append(num2 * num1)
                elif t == "/":
                    stack.append(int(num2 / num1))
        return stack[0]
                    

