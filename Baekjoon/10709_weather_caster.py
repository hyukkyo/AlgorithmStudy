import sys
input = sys.stdin.readline

h, w = map(int, input().split())

grid = []
result = [[-1]*w for _ in range(h)]


for i in range(h):
    line = list(input().strip())
    grid.append(line)
    for j in range(w):

        if line[j] == 'c':
            result[i][j] = 0


for i in range(h):
    for j in range(1, w):
        if result[i][j] == -1 and result[i][j-1] != -1:
            result[i][j] = result[i][j-1] + 1


for i in range(h):
    for j in range(w):
        print(result[i][j], end=" ")
    print()