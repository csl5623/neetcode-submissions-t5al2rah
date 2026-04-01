class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapCloseOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in mapCloseOpen:
                if stack and stack[-1] == mapCloseOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False