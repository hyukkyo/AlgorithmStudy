import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))

    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]: # i는 now=1일때 (2,2)
            cost = dist + i[1] # (2,2)는 2노드로 2코스트 드니까 2코스트에 해당하는 i[1]

            if cost < distance[i[0]]: # (2,2)에서 2노드에 해당하는 i[0]
                distance[i[0]] = cost # 코스트 갱신
                heapq.heappush(q, (cost, i[0])) 

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])