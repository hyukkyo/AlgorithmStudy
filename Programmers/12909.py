def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == ')' and len(stack) == 0:
            return False
        elif i == ')' and len(stack) > 0:
            stack.pop()
        elif i == '(':
            stack.append('(')

    if len(stack) > 0:
        return False
    return True