import heapq

INF = int(1e9)

n,m,c = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        # 남은 애들중에 가장 거리가 짧은 애가 튀어나옴
        dist, now = heapq.heappop(q)

        # 현재 최단거리보다 큰애가 나오면 걍 넘어감
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            # 2에 들어있는 최단거리보다, 1을 거치고 2를 간 cost가 더 빠르면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)

# 어렵다