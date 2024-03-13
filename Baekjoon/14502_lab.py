import sys
from collections import deque
input = sys.stdin.readline()

n, m = map(int, input())

grid = []
for i in range(n):
    column = list(map(int, input()))
    grid.append(column)


# 1. 벽 3개 넣기
# 2. 값이 2인곳에서 2로 BFS
# 3. 값이 0인곳에서 BFS하면서 갯수를 뱉음.
# 4. 최댓값 갱신
    
def make_walls(num):
    pass

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
