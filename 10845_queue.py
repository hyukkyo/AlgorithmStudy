import sys

que = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'pop':
        if len(que):
            print(que[0])
            del que[0]
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if len(que):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(que):
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(que):
            print(que[-1])
        else:
            print(-1)

# timeout
# input()을 쓰면 시간초과됨