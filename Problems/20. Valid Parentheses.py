s = input()

stack = []


def ValidParentheses(s, stack):
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif len(stack) >= 1:
            if s[i] == ')' and stack[len(stack)-1] == '(':
                stack.pop()
            elif s[i] == '}' and stack[len(stack)-1] == '{':
                stack.pop()
            elif s[i] == ']' and stack[len(stack)-1] == '[':
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


print(ValidParentheses(s, stack))
