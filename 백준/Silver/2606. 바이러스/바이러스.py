from collections import deque
import sys
input = sys.stdin.readline

num_computers = int(input())
num_computer_pairs = int(input())

graph = [[] for i in range(num_computers + 1)]

for _ in range(num_computer_pairs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (num_computers + 1)
visited[1] = True
queue = deque([1])
count = 0
while queue:
    target_computer = queue.popleft()
    for next_computer in graph[target_computer]:
        if not visited[next_computer]:
            visited[next_computer] = True
            queue.append(next_computer)
            count += 1

print(count)