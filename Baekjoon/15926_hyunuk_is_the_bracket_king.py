n = int(input())

str = input()
stack = []
arr = [0] * n

blen = 0
res = 0

for i in range(n):
    if str[i] == '(':
        stack.append(i)
    elif str[i] == ')':
        if len(stack) != 0:
            arr[stack.pop()] = 1
            arr[i] = 1

for j in arr:
    if j == 1:
        blen += 1
        res = max(res, blen)
    else:
        blen = 0

print(res)