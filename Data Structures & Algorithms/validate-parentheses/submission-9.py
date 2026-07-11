class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in closeToOpen: # if closing
                if len(stack) == 0 or closeToOpen[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else: # else opening
                stack.append(i)

        return len(stack) == 0