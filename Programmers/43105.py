# DP
# 정수 삼각형

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    l = len(triangle)
    memo = [[0] * l for _ in range(l)]

    memo[0][0] = triangle[0][0]

    for i in range(1, l):
        row = triangle[i]
        for j in range(0, len(row)):
            if j == 0:
                memo[i][j] = triangle[i][j] + memo[i-1][j]
            else:
                memo[i][j] = max(
                    triangle[i][j] + memo[i-1][j],
                    triangle[i][j] + memo[i-1][j-1]
                )
    return max(memo[-1])

print(solution(triangle))