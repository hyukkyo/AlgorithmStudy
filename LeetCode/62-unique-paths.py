class Solution(object):
    def uniquePaths(self, m, n):
        M = m-1
        N = n-1
        K = M if N < M else N

        denominator = 1 # 분모
        numerator = 1 # 분자

        for i in range(0, K):
            numerator *= (i+1)
            denominator *= (M+N-i)
        
        return int(denominator / numerator)

s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))

# 경우의 수로 풀지말고 dp로 풀어보기?