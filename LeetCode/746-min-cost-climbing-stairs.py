# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         memo = {}
#         l = len(cost)

#         memo[0] = 0
#         memo[1] = 0

#         def dp(n):
#             if n < 2:
#                 return memo[n]

#             if n not in memo:
#                 memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])

#             return memo[n]

#         return dp(l)
        


# s = Solution()
# print(s.minCostClimbingStairs([10,15,20]))
# print(Solution.minCostClimbingStairs(self=Solution, cost=[10,15,20]))

# 여기는 해설 영상
# cost = [10, 15, 20, 17, 1]
# memo = {}

# def dp(n):
#     if n == 0 or n == 1: 
#         return 0
#     if n not in memo:
#         memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])
#     return memo[n]

# print(dp(5))


# 바텀업 방식으로도 풀어보기

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost) #5
        table = [0] * (n+1) #6

        for i in range(2, n+1):
            table[i] = min(table[i-1]+cost[i-1], table[i-2]+cost[i-2])
        
        return table[-1]
    
s = Solution()
print(s.minCostClimbingStairs([10,15,20,17,1]))
