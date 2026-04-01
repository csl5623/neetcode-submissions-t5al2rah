class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operations = ["+","-","*","/"]
        for t in tokens:
            if t in operations:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    if t == "+":
                        stack.append(a+b)
                    elif t == "-":
                       stack.append(a -b)
                    elif t == "*":
                         stack.append(a * b) 
                    elif t == "/":
                        stack.append(int(float(a) / b))
            else:
                stack.append(int(t))
        return stack[0]