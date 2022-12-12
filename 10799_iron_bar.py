S = input()

bar = 0
i = 0
level = -1
while i < len(S):

    if S[i] == '(':
        level += 1

    
    elif S[i] == ')':
        if S[i-1] == '(':
            # 레이저임
            bar += level
        else:
            #레이저 아님
            bar += 1
        level -= 1


    i += 1

print(bar)