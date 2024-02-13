# 탑다운) 재귀 -> memoization

cost = [10, 15, 20]
memo = {}

def dp(n):
    if n == 0 and n == 1:
        return 0
    if n not in memo:
        memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])
    return memo[n]

print(dp(3))

# 바텀업) 배열에 저장하기