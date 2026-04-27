class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_closed = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in range(len(s)):
            if s[i] in open_closed:
                if stack:
                    currElement = stack.pop()
                else:
                    currElement = "."
                if open_closed[s[i]] != currElement:
                    return False
            else:
                stack.append(s[i])
            print(stack)
        if len(stack) > 0:
            return False
        else:
            return True

