import sys

li = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        li.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        li.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
            del li[0]
    elif command[0] == 'pop_back':
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
    elif command[0] == 'front':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    elif command[0] == 'back':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])