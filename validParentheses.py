class Solution(object):
    def isValidParentheses(self, s):
        stack=[]
        for ch in s:
            # press stack
            if ch == '{' or ch == '[]' or ch == '()':
                stack.append(ch)
            else:
                # stack should be not NULL
                if not stack:
                    return False
                # judge is stack top is fit
                if ch == ']' and stack[-1] !='[' or ch == ')' and stack[-1] !='(' or ch == '}' and stack[-1]!='{':
                    return False
                # pop stack
            stack.pop()
    return not stack
