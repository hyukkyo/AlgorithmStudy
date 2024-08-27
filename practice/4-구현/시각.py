import sys
input = sys.stdin.readline

n = int(input())
# n시 59분 59초까지의 모든 시각 중, 3이 하나라도 포함되는 경우의 수

# 0시 59분 59초 -> 03초, 13초, 23초, 33초, 43초, 53초, 03분, 13분...

# 어차피 하루는 86400초이기 때문에 그냥 매초 탐색해도 상관이 없다.

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)