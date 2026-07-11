class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['[', '(', '{']: # if open then push
                stack.append(i)
            else: # else close, check for matching open
                if (len(stack) == 0
                    or (i == ']' and stack[-1] != '[')
                    or (i == ')' and stack[-1] != '(')
                    or (i == '}' and stack[-1] != '{')):
                    return False
                stack.pop()

        return len(stack) == 0