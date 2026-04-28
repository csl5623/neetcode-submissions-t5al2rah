class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        operands = ["+","-","*","/"]
        for i in range(len(tokens)):
            char = tokens[i]
            if char in operands:
                    result = 0
                    value1 = stack.pop()
                    value2 = stack.pop()
                    if char == "+":
                        result = value1 + value2
                    elif char == "-":
                        result = value2 - value1
                    elif char == '*':
                        result = value1 * value2
                    else:
                        result = value2 / value1
                    stack.append(int(result))
            else:
                stack.append(int(char))
        return stack[0]