import sys
input = sys.stdin.readline

h, w = map(int, input().split())

grid = []
for i in range(h):
    line = input()
    w = []
    for j in range(w):
        w.append(line[j])
        
    

print(grid)