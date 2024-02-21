# 다익스트라
import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        # 그래프 구현
        # graph = {}
        # for time in times:
        #     graph[time[0]] = []
        # for time in times:
        #     graph[time[0]].append((time[2], time[1]))
        # print(graph)

        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))
            
        # 다익스트라 알고리즘
        costs = {}
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))


        # 방문 못한 노드 찾기
        for node in range(1, n+1):
            if node not in costs:
                return -1

        # 최대값 구하기
        return max(costs.values())

s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))