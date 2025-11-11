# stack
stack = []

# queue
from collections import deque
queue = deque(range(1, 4))

# hash - 딕셔너리. 중복제거
hash_dict = {}

# heap - 우선순위 큐. 완전 이진트리 형태로 최소값이 0에 옴. 최대값 찾을땐 음수 활용
import heapq
nums = [2,3,1]
heapq.heapify(nums) #1,3,2
heapq.heappop(nums) #1

# sorting - 선택/삽입/버블/병합/힙/퀵
# 메모리 복잡도에 대한 개념 필요

# 구현, 시뮬레이션
# 브루트 포스 / 완전 탐색
# 천 - 4KB / 백만 - 4MB / 천만 - 40MB

# greedy
# 그 순간 최선을 선택하는게 최적 <- 이라는걸 캐치할 수 있어야함

# dp (dynamic programming)
# memoization(caching)
# 바텀업/탑다운 방식이 있음

# 그래프
# 인접 행렬과 인접 연결리스트
# 일반적으로 dfs bfs와 함께 사용

# dfs는 재귀
def dfs_recursive(graph, start, visited):
  visited[start] = True
  
  for neighbor in graph[start]:
    if not visited[neighbor]:
      dfs_recursive(graph, neighbor, visited)

# bfs는 큐
from collections import deque

def bfs(graph, start):
  visited = [False] * len(graph)
  queue = deque([start])
  visited[start] = True

  while queue:
    node = queue.popleft()
    
    for neighbor in graph[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append(neighbor)

# binary search
def binary_search(arr, target):
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

# binary search tree
# 왼쪽 노드값 < 부모 노드값 < 오른쪽 노드값

# backtracking
# 막히면 되돌아가서 다시 해를 찾는 기법

# lis/lcs

# 다익스트라: 한 지점에서 다른 지점까지 최단 경로 -> 그리디
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# 플로이드워셜: 모든 지점에서 다른 모든지점까지 최단경로 -> DP
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 초기화
    for i in range(n):
        dist[i][i] = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # 플로이드-워셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist