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

        # for i in s:
        #     if i in ['[', '(', '{']: # if open then push
        #         stack.append(i)
        #     else: # else close, check for matching open
        #         if (len(stack) == 0
        #             or (i == ']' and stack[-1] != '[')
        #             or (i == ')' and stack[-1] != '(')
        #             or (i == '}' and stack[-1] != '{')):
        #             return False
        #         stack.pop()

        # return len(stack) == 0