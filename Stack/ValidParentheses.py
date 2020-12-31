def _isValidParentheses(expression):
    stack = []
    length = len(expression)
    for i in range(0,length):
        if expression[i] == '{' or expression[i] == '[' or expression[i] == '(':
            stack.append(expression[i])
        elif expression[i] == '}' and not len(stack) ==0 and stack[-1] == '{':
            stack.pop()
        elif expression[i] == ']' and not len(stack) ==0 and stack[-1] == '[':
            stack.pop()
        elif expression[i] == ')' and not len(stack) ==0 and stack[-1] == '(':
            stack.pop()
        else:
            return False
    return len(stack) ==0

print(_isValidParentheses('[()(){}]'))