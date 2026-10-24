class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        for c in s:
            if c in dict1:
                if stack and dict1[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False

        return True