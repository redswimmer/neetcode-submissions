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
                if stack and closeToOpen[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: # else opening
                stack.append(i)

        return len(stack) == 0