# top-down 방식, 재귀 사용
# memo = {}
# def climbStairs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     memo[n] = climbStairs(n-1) + climbStairs(n-2)
#     return memo[n]

# bottom-up 방식
memo = {
    1:1,
    2:2,
}
def climbStairs(n):
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]
# 이때는 memoization이라고 안하고 dp table이라고 함


print(climbStairs(3))