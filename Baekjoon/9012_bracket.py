t = int(input())

for i in range(t):
    bracket = input()
    count = 0
    for j in bracket:
        if count < 0:
            break

        if j=='(':
            count = count + 1
        elif j==')':
            count = count - 1
            
    if count == 0:
        print("YES")
    else:
        print("NO")