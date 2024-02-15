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

# 경우의 수로 풀지말고 dp로 풀어보기



memo = {} # 2차원 리스트를 써도 되긴 함
unique_paths = 0

def dp(r, c):
    if r == 0 and c == 0:
        memo[(r, c)] = 1
        return memo[(r, c)]

    if (r, c) not in memo:
        if r-1 >= 0:
            unique_paths += dp(r-1, c)
        if c-1 >= 0:
            unique_paths += dp(r, c-1)

        memo[(r, c)] = unique_paths

    return memo[(r, c)]