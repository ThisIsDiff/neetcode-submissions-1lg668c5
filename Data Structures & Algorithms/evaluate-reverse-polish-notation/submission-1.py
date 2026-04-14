class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                t = num1 + num2
            elif t == '-':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                t = num1 - num2
            elif t == '*':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                t = num1 * num2
            elif t == '/':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                t = num1 / num2
            stack.append(int(t))

        return stack.pop()

        