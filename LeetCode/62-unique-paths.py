# class Solution(object):
#     def uniquePaths(self, m, n):
#         M = m-1
#         N = n-1
#         K = M if N < M else N

#         denominator = 1 # 분모
#         numerator = 1 # 분자

#         for i in range(0, K):
#             numerator *= (i+1)
#             denominator *= (M+N-i)
        
#         return int(denominator / numerator)

# s = Solution()
# print(s.uniquePaths(3, 7))
# print(s.uniquePaths(3, 2))

# 경우의 수로 풀었음




# DP로 풀어보기. 우선 탑다운 형식으로

# memo = {} # 딕셔너리 선언

# def dp(M, N):
#     m = M-1
#     n = N-1

#     if m == 0 or n == 0:
#         # memo[(m, n)] = 1
#         return 1

#     unique_paths = 0
#     if (m, n) not in memo:
#         if m-1 >= 0:
#             unique_paths += dp(M-1, N)
#         if n-1 >= 0:
#             unique_paths += dp(M, N-1)

#         memo[(m, n)] = unique_paths #딕셔너리의 key에는 튜플 순서쌍이 들어가도 된다.

#     return memo[(m, n)]


# print(dp(3,7))


# 2차원 배열(리스트)로도 짤수있음

# def dp(M, N):
#     m = M-1
#     n = N-1

#     memo = [[-1]*N for _ in range(M)]

#     if m == 0 or n == 0:
#         return 1

#     unique_paths = 0
#     if memo[m][n] == -1:
#         if m-1 >= 0:
#             unique_paths += dp(M-1, N)
#         if n-1 >= 0:
#             unique_paths += dp(M, N-1)
    
#         memo[m][n] = unique_paths


#     return memo[m][n]

# print(dp(3,7))



# 바텀업 방식으로 짜보자

def dp(M, N):
    table = [[1]*N for _ in range(M)]

    for i in range(1, M):
        for j in range(1, N):
            table[i][j] = table[i-1][j] + table[i][j-1]

    return table[M-1][N-1]

print(dp(3,7))