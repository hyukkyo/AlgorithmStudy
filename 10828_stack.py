import sys

li = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        li.append(int(command[1]))
    elif command[0] == 'pop':
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop())
    elif command[0] == 'size':
        print(len(li))
    elif command[0] == 'empty':
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])